import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/user/oritokarn/about"

r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
        print "<a href='%s'>%s</a>" %(link.get("href") , link.text)

g_data = soup.find_all("button" , {"class": "channel-msg-button"})

link_google = ""

for item in g_data:
    print item
    #link_google = item.get("href")


secondurl = link_google

rsecond = requests.get(secondurl)

soup = BeautifulSoup(rsecond.content)



