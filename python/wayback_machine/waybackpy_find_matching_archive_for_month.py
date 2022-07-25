from numpy import average, number
from waybackpy import WaybackMachineCDXServerAPI
import csv
import os
import time
#set active directory to wherever abspath is
abspath = os.path.abspath("C:\\Users\\nathan\\OneDrive\\Documents\\l2c\\research_halfond\\python\\wayback_machine\\waybackpytest.py")
dname = os.path.dirname(abspath)
os.chdir(dname)

#convert csv into a list of urls and a dict of urls mapping to indexes
list_of_urls = list()
dict_of_urls = dict()
with open('random_urls.csv', 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_of_urls.append(row["url"])
        dict_of_urls[row["url"]] = int(row["index"])

#some global variables
YEAR = "2016"
YEAR2 ="2019"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

#initialize variables to keep track of availabiliy data

number_of_urls = 500



#initialize month specific variables
subjects_in_each_month_year = dict()
subjects_in_each_month_year2 = dict()
matches_in_each_month = dict()
matching_sum_of_index_in_each_month = dict()
matching_average_index_in_each_month = dict()
for i in range(1,13):
    subjects_in_each_month_year[i] = 0
    subjects_in_each_month_year2[i] = 0
    matches_in_each_month[i] = 0
    matching_sum_of_index_in_each_month[i] = 0
    matching_average_index_in_each_month[i] = 0

month = 0
for i in "01 02 03 04 05 06 07 08 09 10 11 12".split():
    print("weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee " + i)
    month += 1
    temp_year = YEAR + i
    temp_year = int(temp_year)

    temp_year2 = int(YEAR2+i)
    for url in list_of_urls:
        #get archive for YEAR
        time.sleep(0.15)
        cdx_api = WaybackMachineCDXServerAPI(url, user_agent, start_timestamp=temp_year, end_timestamp=temp_year)
        value = cdx_api.oldest()

        #get archive for YEAR2
        time.sleep(0.15)
        cdx_api2 = WaybackMachineCDXServerAPI(url, user_agent, start_timestamp=temp_year2, end_timestamp=temp_year2)
        value2 = cdx_api2.oldest()

        temp_year = str(temp_year)
        temp_year2 = str(temp_year2)
        if value == None:
            print(temp_year + " is missing " + url)
        else:
            print(url + " is in " + temp_year)   
            subjects_in_each_month_year[month]+=1

        if value2 == None:
            print(temp_year2 + " is missing " + url)
        else:
            print(url + " is in " + temp_year2)   
            subjects_in_each_month_year2[month]+=1

        if value is not None and value2 is not None:
            print(url + " is in both")
            matches_in_each_month[month]+= 1
            matching_sum_of_index_in_each_month[month] += dict_of_urls[url]

        print()


    matching_average_index_in_each_month[month] = matching_sum_of_index_in_each_month[month]/ matches_in_each_month[month]

    



print("\n\n")

for i in range(1,13):
    print("Year: " + YEAR + " " + "month: " + str(i) + " has " + str(subjects_in_each_month_year[i]) + " archives")

print()

for i in range(1,13):
    print("Year: " + YEAR2 + " " + "month: " + str(i) + " has " + str(subjects_in_each_month_year2[i]) + " archives")

print()
print("matching:")
for i in range(1,13):
   print("month: " + str(i) + " has " + str(matches_in_each_month[i]) + " matches between both years")

print()
print("average index")
for i in range(1,13):
   print("month: " + str(i) + "'s average index of matching archived urls is " + str(matching_average_index_in_each_month[i]))


"""
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

for 2019
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
3258 of subjects have waybackmachine archive
2742 of subjects don't have waybackmachine archive
average archive rate is: 0.543
average index of successful urls is: 3209490.314
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