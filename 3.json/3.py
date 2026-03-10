import json

# === CONFIG ===
input_files = [
    "3.in.IDs.LessonVideos.txt",
    "3.in.IDs.TIME.txt",
    "3.in.IDs.TOPIC.txt"
]

all_ids_file = "3.in.allVideoIDs.txt"
output_file = "3.out.videoID_to_playlists.json"


# === STEP 1: Parse playlist files ===
video_to_playlists = {}

for filename in input_files:
    with open(filename, "r", encoding="utf-8") as f:
        current_playlist_name = None
        current_playlist_url = None

        for line in f:
            line = line.strip()
            if not line:
                continue

            # playlist header
            if line.startswith('"') and 'https://www.youtube.com/playlist' in line:
                parts = line.split('[')
                current_playlist_name = parts[0].strip().strip('"')
                current_playlist_url = parts[1].strip(' ]') if len(parts) > 1 else ""
                continue

            # video ID
            if current_playlist_name and current_playlist_url:
                vid = line

                if vid not in video_to_playlists:
                    video_to_playlists[vid] = []

                entry = (current_playlist_name, current_playlist_url)

                if entry not in video_to_playlists[vid]:
                    video_to_playlists[vid].append(entry)


# === STEP 2: Load IDs + names ===
final_mapping = {}

with open(all_ids_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        vid, name = line.split("|", 1)

        vid = vid.strip()
        name = name.strip()

        final_mapping[vid] = {
            "name": name,
            "playlists": video_to_playlists.get(vid, [])
        }


# === STEP 3: Save JSON ===
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(final_mapping, f, indent=4, ensure_ascii=False)

print("Done! JSON saved to", output_file)