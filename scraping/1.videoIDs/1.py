import re
from yt_dlp import YoutubeDL

input_file = "1.in.playlists.txt"
output_file = "1.out.video_ids.txt"

print("Opening:", input_file)

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 🔹 Pass 1: count playlists
playlist_urls = []
for line in lines:
    pid_match = re.search(r"list=([A-Za-z0-9_-]+)", line)
    if pid_match:
        pid = pid_match.group(1)
        playlist_urls.append(pid)

total = len(playlist_urls)
print("Playlists found:", total)


ydl_opts = {
    "quiet": True,
    "extract_flat": True
}

print("Processing...")

count = 0  # current progress

with YoutubeDL(ydl_opts) as ydl, open(output_file, "w", encoding="utf-8") as out:

    for line in lines:
        stripped = line.rstrip("\n")
        out.write(stripped + "\n")

        pid_match = re.search(r"list=([A-Za-z0-9_-]+)", line)
        if not pid_match:
            continue

        # 🔹 Progress update
        count += 1
        pid = pid_match.group(1)
        url = f"https://www.youtube.com/playlist?list={pid}"

        print(f"\nProcessing playlist {count}/{total}")

        indent = re.match(r"\s*", line).group()

        try:
            info = ydl.extract_info(url, download=False)
        except Exception as e:
            print("ERROR:", e)
            continue

        playlist_name = info.get("title", "UNKNOWN_PLAYLIST")
        entries = info.get("entries", [])

        print("Title:", playlist_name)
        print("Videos:", len(entries))

        for video in entries:
            if video:
                vid = video.get("id", "UNKNOWN_ID")
                title = video.get("title", "UNKNOWN_TITLE")
                out.write(f"{indent}    {vid}    |    {title}\n")

        out.write("\n")

print("\nFinished.")
print("Saved to:", output_file)