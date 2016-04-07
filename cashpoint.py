from bs4 import BeautifulSoup
import html5lib
import urllib
siteName = "cashpoint"
html_doc = urllib.urlopen('https://www.cashpoint.dk/da/site/index.html').read()
soup = BeautifulSoup(html_doc, 'html.parser')

matches = soup.findAll("div", { "class" : "live_row_container clearfix" })

matchDict = {}

for i in matches:
    homeTeam = i.find("div", { "class" : "live_group1" }).text.strip()
    awayTeam = i.find("div", { "class" : "live_group2" }).text.strip()
    matchName = homeTeam+" - "+awayTeam  
    
    test = i.findAll("div", { "class" : "live_td live_odds_container" })
    counter = 0
    oddsList = []
    for j in test:
        oddsList.append(j.text.strip())
        counter +=1
        if counter == 3:
            break

    matchDict[matchName] = [oddsList,siteName]
        
        
