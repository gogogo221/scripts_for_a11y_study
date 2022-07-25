import os
import csv
import pandas as pd
import random

#this script generates a csv containing random sites from the tranco in random order
#to run, you will need to download the tranco list of the top 1 million websites 
#from this website: https://tranco-list.eu/

#set directory script is in a current directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


#generate a list of n random numbers to select from 1m TDOO_______________________________!_!_!_!_!_!_!_!_!
NUMBER_OF_RANDOM_SITES_GENERATED = 500
list_random_int = list()
used_ints = set()


for i in range(500):
    randint = -1
    #generate a random int that isnt already chosen
    while(True):
        randint = random.randint(1,1000000)
        if randint not in used_ints:
            break
    list_random_int.append(randint)
    used_ints.add(randint)



index_to_url =  dict()
i =0
with open('top-1m.csv', 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        index_to_url[int(row[0])] = row[1]

with open("random_urls.csv", "w", newline='') as csvfile:
    #fieldnames = ["index", "url"]
    writer = csv.writer(csvfile, delimiter=",")


    writer.writerow(["index", "url"])
    #iterate through the randomly generated indexes
    for index in list_random_int:
        #iterate through the accptable domains
        writer.writerow([index, index_to_url[index]])

print("done")