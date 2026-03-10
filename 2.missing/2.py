import re

all_uploads_file = "2.in.allUploads.txt"
playlist_ids_file = "2.in.videoIDs.txt"
output_file = "2.out.missing.txt"

print("Reading full upload list...")

with open(all_uploads_file, "r", encoding="utf-8") as f:
    all_ids = {line.strip() for line in f if line.strip()}

print("Total uploads:", len(all_ids))

print("Reading playlist video IDs...")

playlist_ids = set()

with open(playlist_ids_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        # detect 11-character youtube IDs
        if re.fullmatch(r"[A-Za-z0-9_-]{11}", line):
            playlist_ids.add(line)

print("Video IDs listed in playlists:", len(playlist_ids))

missing = sorted(all_ids - playlist_ids)

print("Missing IDs:", len(missing))

with open(output_file, "w", encoding="utf-8") as f:
    for vid in missing:
        f.write(vid + "\n")

print("Saved missing IDs to:", output_file)