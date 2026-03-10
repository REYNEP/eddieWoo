# Get VideoID's from a list of PlayLists

import re
from yt_dlp import YoutubeDL

input_file = "1.in.playlists.txt"
output_file = "1.out.video_ids.txt"

print("Opening:", input_file)

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

playlist_urls = []

print("Scanning playlist links...")

for line in lines:
    pid_match = re.search(r"list=([A-Za-z0-9_-]+)", line)
    if pid_match:
        pid = pid_match.group(1)
        playlist_urls.append(f"https://www.youtube.com/playlist?list={pid}")

print("Playlists found:", len(playlist_urls))

ydl_opts = {
    "quiet": True,
    "extract_flat": True
}

with YoutubeDL(ydl_opts) as ydl, open(output_file, "w", encoding="utf-8") as out:

    for i, url in enumerate(playlist_urls, start=1):

        print(f"\nProcessing playlist {i}/{len(playlist_urls)}")

        try:
            info = ydl.extract_info(url, download=False)
        except Exception as e:
            print("ERROR:", e)
            continue

        playlist_name = info.get("title", "UNKNOWN_PLAYLIST")
        entries = info.get("entries", [])

        print("Title:", playlist_name)
        print("Videos:", len(entries))

        out.write(f"\"{playlist_name}\"     [{url}]\n")

        for video in entries:
            if video:
                vid = video["id"]
                out.write(f"    {vid}\n")

        out.write("\n")

print("\nFinished.")
print("Saved to:", output_file)