import re

video_file = "1.in.video_ids.txt"
reysort_file = "4.in.REYSort.txt"
output_file = "5.out.txt"


# =========================
# STEP 1: Parse REYSort (NEW FORMAT)
# =========================
video_to_playlists = {}
current_playlist = None

with open(reysort_file, "r", encoding="utf-8") as f:
    for line in f:
        raw = line.rstrip("\n")
        line = raw.strip()

        if not line:
            continue

        # Playlist header: "0.00 - Kids 1" [url]
        if line.startswith('"') and "youtube.com/playlist" in line:
            current_playlist = line.split('"')[1]
            continue

        # Video line: id | title
        match = re.match(r"^([A-Za-z0-9_-]{11})\s*\|\s*(.+)$", line)
        if match:
            vid = match.group(1)

            video_to_playlists.setdefault(vid, []).append(current_playlist)


# =========================
# Helper: process one section
# =========================
def process_section(section_lines, out):
    max_rey_len = 0
    parsed = []

    # First pass → compute max width
    for line in section_lines:
        match = re.match(r"^(\s*)([A-Za-z0-9_-]{11})\s*\|\s*(.+)$", line)

        if match:
            indent, vid, title = match.groups()

            rey = video_to_playlists.get(vid, [])
            rey = list(dict.fromkeys(rey))

            rey_str = "".join([f"[{p}]" for p in rey]) or "[]"

            max_rey_len = max(max_rey_len, len(rey_str))

            parsed.append(("video", indent, vid, rey_str, title))
        else:
            parsed.append(("raw", line))

    # Second pass → write aligned
    ID_WIDTH = 14
    REY_WIDTH = max_rey_len + 2

    for item in parsed:
        if item[0] == "video":
            _, indent, vid, rey_str, title = item

            out.write(
                f"{indent}"
                f"{vid:<{ID_WIDTH}} | "
                f"{rey_str:<{REY_WIDTH}} | "
                f"{title}\n"
            )
        else:
            out.write(item[1] + "\n")


# =========================
# STEP 2: Read + split into sections
# =========================
with open(video_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:

    current_section = []

    for raw_line in fin:
        line = raw_line.rstrip("\n")

        # Detect NEW section (playlist line)
        if line.strip().startswith("|") and "youtube.com/playlist" in line:
            # process previous section first
            if current_section:
                process_section(current_section, fout)
                current_section = []

        current_section.append(line)

    # last section
    if current_section:
        process_section(current_section, fout)


print("Done. Section-wise alignment complete 🔥")
print("Saved to:", output_file)