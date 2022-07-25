#command to activate venv  wayback\Scripts\Activate.ps1
import wayback as wb
import waybackpy as wbpy
import csv
client = wb.WaybackClient()

results = client.search('https://www.pathofexile.com/game')

i =0
for record in results:
    i +=1
print(i)


#iterate through all the archived pages from oldest to most recent
for record in results:
    pass

#get the momento (html response) from the record object
html_response = client.get_memento(record)


with html_response:
    #The body of the archived HTTP response in bytes.
    content = html_response.content
    #The body of the archived HTTP response decoded as a string.
    text = html_response.text

    print(content)

