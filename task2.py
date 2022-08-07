from bs4 import BeautifulSoup
import requests , json
from pprint import pprint

file2=open("task1.json","r")
movies=json.load(file2)

def group_by_year(movies):
    dict1={}
    for i in movies:
        y=i["year"]
        if y not in dict1:
            dict1[y]=[]
        else:
            dict1[y].append(i)
    with open('task2.json','w') as f3:
        json.dump(dict1,f3,indent=4)
        return dict1       
pprint(group_by_year(movies))
    