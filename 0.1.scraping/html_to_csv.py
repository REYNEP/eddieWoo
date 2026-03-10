from bs4 import BeautifulSoup
import csv

# input html file
input_file = "All EddieWoo Uploads - March10 2026.htm"

# output csv file
output_file = "All EddieWoo Uploads - March10 2026.csv"

with open(input_file, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

rows = []

for a in soup.find_all("a"):
    link = a.get("href")

    span = a.find("span")
    if span:
        title = span.text.strip()
        rows.append([link, title])

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["link", "title"])
    writer.writerows(rows)

print("CSV exported to", output_file)