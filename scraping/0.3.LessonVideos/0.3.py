import re
import html

input_file = "input.txt"
output_file = "output.txt"

print("Reading HTML...")

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

print("Searching for playlist links...")

pattern = r'<a[^>]+href="(https://www\.youtube\.com/playlist\?list=[^"]+)"[^>]*>(.*?)</a>'

matches = re.findall(pattern, text, re.DOTALL)

playlists = []

for url, name in matches:
    name = html.unescape(name)
    name = re.sub(r"<.*?>", "", name).strip()  # remove nested tags
    playlists.append((name, url))

print("Playlists found:", len(playlists))

print("Writing output...")

with open(output_file, "w", encoding="utf-8") as f:
    for name, url in playlists:
        f.write(f"{name} | {url}\n")

print("Done.")