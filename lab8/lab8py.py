#!/usr/bin/python3


import json
import pandas as pd

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

list1 = []
for x in range(5):
    list1.append([file[x]["name"], file[x]["html_url"],file[x]["updated_at"], file[x]["visibility"]])  

df = pd.DataFrame(list1)
df.to_csv('chacon.csv')
