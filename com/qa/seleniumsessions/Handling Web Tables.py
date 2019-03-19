import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

playerdata=playerdatasaved=""
soup = make_soup("http://www.basketball-reference.com/players/a/")
for record in soup.findAll("tr"):
    playerdata=""
   # print(record.text)
    for data in record.findAll("td"):
        print(data.text)
        playerdata=playerdata+","+data.text
    if len(playerdata)!=0:
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]


header ="Player, From, To, Pos, Ht, Wt, Birth, Date, College"
file = open(os.path.expanduser("Basketball.csv"), "wb")
file.write(bytes(header, encoding="ascii", errors="ignore"))
file.write(bytes(playerdatasaved, encoding="ascii", errors="ignore"))

print(playerdatasaved)
