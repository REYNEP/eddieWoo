import re

input_file = "All EddieWoo Uploads - March10 2026.htm"
output_file = "All EddieWoo Uploads - March10 2026.names.txt"

pattern = re.compile(
    r'watch\?v=([A-Za-z0-9_-]{11}).*?<span[^>]*>(.*?)</span>',
    re.DOTALL
)

with open(input_file, "r", encoding="utf-8") as f:
    html = f.read()

matches = pattern.findall(html)

with open(output_file, "w", encoding="utf-8") as out:
    for vid, title in matches:
        title = title.strip()
        out.write(f"{vid}     |     {title}\n")

print(f"Extracted {len(matches)} videos.")
print("Saved to:", output_file)