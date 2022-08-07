from task4 import scrape_movie_details
import requests,json
from pprint import pprint
from bs4 import BeautifulSoup

with open("task1.json","r") as f5:
    ff5=json.load(f5)    
def get_movie_list_details():
    task5=[]
    for i in ff5[:10]:
        task5.append(scrape_movie_details(i["url"]))
    f=open("imdb_movie_detailT5.json","w")
    json.dump(task5,f,indent=4)
    f.close()
    return task5    
pprint(get_movie_list_details())