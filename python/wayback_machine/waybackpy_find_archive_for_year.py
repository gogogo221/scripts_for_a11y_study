from numpy import average, number
from waybackpy import WaybackMachineCDXServerAPI
import csv
import os
import time
abspath = os.path.abspath("C:\\Users\\nathan\\OneDrive\\Documents\\l2c\\research_halfond\\python\\wayback_machine\\waybackpytest.py")
dname = os.path.dirname(abspath)
os.chdir(dname)

list_of_urls = list()
dict_of_urls = dict()
with open('random_urls.csv', 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_of_urls.append(row["url"])
        dict_of_urls[row["url"]] = int(row["index"])


url = "https://github.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

subjects_with_log = list()
subjects_without_log = list()
sum_index_success = 0
sum_index_total = 0
number_of_urls = 500
YEAR = "2016"
YEAR2 = "2019"
sum_match = 0
sum_of_index_match = 0


for url in list_of_urls:
    #get archive for YEAR
    time.sleep(0.15)
    cdx_api = WaybackMachineCDXServerAPI(url, user_agent, start_timestamp=YEAR, end_timestamp=YEAR)
    value = cdx_api.oldest()

    #get archive for YEAR2
    time.sleep(0.15)
    cdx_api2 = WaybackMachineCDXServerAPI(url, user_agent, start_timestamp=YEAR2, end_timestamp=YEAR2)
    value2 = cdx_api2.oldest()

    YEAR = str(YEAR)
    YEAR2 = str(YEAR2)
    

    if value is not None and value2 is not None:
        print(url + " is in both")
        sum_match+= 1
        sum_of_index_match += dict_of_urls[url]

    print()

average_index_match = sum_of_index_match/sum_match


print("\n\n")

print("number of matches = " + str(sum_match))
print("average index = " + str(average_index_match))


"""print(str(len(subjects_with_log)) + " of subjects have waybackmachine archive")
print(str(len(subjects_without_log)) + " of subjects don't have waybackmachine archive" )
print("average archive rate is: " + str(len(subjects_with_log)/(len(subjects_with_log)+len(subjects_without_log))))
average_index_of_success = sum_index_success/number_of_urls
print("average index of successful urls is: " + str(average_index_of_success))
"""




"""
2022
archive ratio of websites from all time     
491 of subjects have waybackmachine archive
9 of subjects don't have waybackmachine archive
average archive rate is: 0.982
average index of successful urls is: 494324.568

2021
469 of subjects have waybackmachine archive
31 of subjects don't have waybackmachine archive
average archive rate is: 0.938
average index of successful urls is: 467897.102

archive ratio of websites from 2020
411 of subjects have waybackmachine archive
89 of subjects don't have waybackmachine archive
average archive rate is: 0.822
average index of successful urls is: 412746.496


2019:
393 of subjects have waybackmachine archive
107 of subjects don't have waybackmachine archive
average archive rate is: 0.786
average index of successful urls is: 391381.684
month: 1 has 313
month: 2 has 253
month: 3 has 261
month: 4 has 271
month: 5 has 295
month: 6 has 273
month: 7 has 282
month: 8 has 286
month: 9 has 275
month: 10 has 282
month: 11 has 227
month: 12 has 300

2016
378 of subjects have waybackmachine archive
122 of subjects don't have waybackmachine archive
average archive rate is: 0.756
average index of successful urls is: 378288.522
month: 1 has 349
month: 2 has 257
month: 3 has 345
month: 4 has 276
month: 5 has 258
month: 6 has 259
month: 7 has 245
month: 8 has 252
month: 9 has 228
month: 10 has 354
month: 11 has 247
month: 12 has 188



"""