#!/usr/bin/python3


import json
import csv
import pandas as pd

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)


with open('chacon.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'html_url', 'updated_at', 'visibility']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    for x in range(5):
        writer.writerow({'name': data[x]["name"], 'html_url':data[x]["html_url"],'updated_at':data[x]["updated_at"], 'visibility':data[x]["visibility"]})

#list1 = []
#for x in range(5):
#    list1.append([file[x]["name"], file[x]["html_url"],file[x]["updated_at"], file[x]["visibility"]])  

#df = pd.DataFrame(list1)
#df.to_csv('chacon.csv')


