import csv

def get_links_from_csv(filepath: str) -> dict:
    dict_of_urls = dict()
    with open(filepath, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_of_urls[int(row["index"])] = row["url"]
    return dict_of_urls