import requests
from bs4 import BeautifulSoup
import time


def pageScraper(search):
    r = requests.get(search)
    totaltime = 0
    soup = BeautifulSoup(r.text, "html.parser")
    time = soup.findAll("span", {"class": "runtime"})
    
    for i in time:
        i = str(i)[22:-7]
        if "hr" in i and "min" in i:
            totaltime += int(i[0]) * 60
            if i[6] == " ":
                totaltime += int(i[5]) 
            else:
                totaltime += int(i[5:7])
        if int(i[0]) >= 2 and len(i) == 4:
            totaltime += int(i[0]) * 60
    try:
        nextpage = "https://www.imdb.com/" + soup.findAll("a", {"class": "flat-button lister-page-next next-page"})[0].attrs["href"]
    except IndexError:
        return totaltime
    
    if nextpage != None:
        return pageScraper(nextpage) + totaltime
         
search = input("paste link to IMDB rating list: ")

result = str(pageScraper(search) / 60).split(".") 

final = f"{result[0]} hrs {str(round((int(result[1]) * 60) / 10))[0:-2]} min"
    


print(final)
time.sleep(2000)


