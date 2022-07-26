from numpy import average, number
from waybackpy import WaybackMachineCDXServerAPI
import csv
import os
import time


def update_current_directory():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

def read_csv_output_urls(filename):
    list_of_urls = list()
    dict_of_urls = dict()

    with open(filename, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_of_urls.append(row["url"])
            dict_of_urls[row["url"]] = int(row["index"])
    return list_of_urls, dict_of_urls

def get_wayback_archive(url, user_agent, start, end):
        time.sleep(0.15)
        cdx_api = WaybackMachineCDXServerAPI(url, user_agent, start_timestamp=start, end_timestamp=end)
        value = cdx_api.oldest()
        return value



def main():
    update_current_directory()
    list_of_urls, dict_of_urls = read_csv_output_urls('random_urls.csv')
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

    YEAR1 = "2016"
    YEAR2 = "2019"
    sum_match = 0
    sum_of_index_match = 0

    for url in list_of_urls:
        #get archive for year1
        value1 = get_wayback_archive(url, user_agent=user_agent, start=YEAR1, end=YEAR1)
        #get archive for YEAR2
        value2 = get_wayback_archive(url,user_agent=user_agent, start=YEAR2, end=YEAR2)

        YEAR = str(YEAR)
        YEAR2 = str(YEAR2)
        
        #if both archives exist, increment value of total matches
        if value1 is not None and value2 is not None:
            sum_match += 1
            sum_of_index_match += dict_of_urls[url]

    #calculate the average rank of the page
    average_index_match = sum_of_index_match/sum_match


    #output data
    print("number of matches = " + str(sum_match))
    print("average index = " + str(average_index_match))

if __name__ == "__main__":
    main()