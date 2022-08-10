import sys,os
sys.path.append("C:\\Users\\nathan\\OneDrive\\Documents\\l2c\\research_halfond\\scripts_for_a11y_study\\python\\useful_functions")

import csv

from get_links_from_csv import get_links_from_csv
from detect_language import detect_language

def export_data_csv(output_file: str, list_index_url_lang:list):
    with open(output_file, "w", encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["index", "url", "language"])
        for index, url, language in list_index_url_lang:
            writer.writerow([index, url, language])


def main():
    dict_of_urls = get_links_from_csv("C:\\Users\\nathan\\OneDrive\\Documents\\l2c\\research_halfond\\scripts_for_a11y_study\python\\random_urls.csv")
    list_index_url_lang = list()
    for index, url in dict_of_urls.items():
        lang =  detect_language("http://"+url)
        list_index_url_lang.append((index, url,lang))
        print(lang)
    export_data_csv("output_languages.csv", list_index_url_lang)



if __name__ == "__main__":
    main()
    
