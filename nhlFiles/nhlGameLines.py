import requests
import bs4
from bs4 import BeautifulSoup

url = 'https://www.espn.com/nhl/lines'

teams = []
lines = []
nhl_game_line = {'home':'','away':'','home_ats':'','away_ats':'',
                 'home_ml':'','away_ml':'', 'home_spread':'','away_spread':'',
                 'over':'','under':''}
nhl_game_lines = []
a = 0

content = requests.get(url)
soup = BeautifulSoup(content.content, 'html.parser')

td = soup.find_all('td')
for td1 in td:
    for i in td1:
        if type(i) == bs4.element.Tag:
            names = i.find_all('a', attrs={'class': 'AnchorLink'})
            for name in names:
                for u in name:
                    if type(u) != bs4.element.Tag:
                        teams.append(u)
        else:
            lines.append(i)
        a += 1

home_ats = lines[0::8]
away_ats = lines[4::8]
home_ml = lines[6::8]
away_ml = lines[2::8]
away_odds = lines[3::8]
home_spread = lines[5::8]
#away_spread = home_spread * -1
over = lines[1::8]
home_odds = lines[7::8]

for e in range(len(home_ats)):
    try:
        hTM = teams[e + 1]
    except:
        hTM = 'idk'
    aTM = teams[e]
    hAts = home_ats[e]
    aAts = away_ats[e]
    hMl = home_ml[e]
    aMl = away_ml[e]
    hSpr = home_spread[e]
    oV = over[e]
    try:
        if float(hSpr) < 0: 
            nhl_game_line = {'home':hTM,'away':aTM,'home_ats':hAts,'away_ats':aAts,
                    'home_ml':hMl,'away_ml':aMl, 'home_spread':hSpr,'away_spread':float(hSpr) * -1,
                    'over':oV,'under':float(oV) * -1}
            nhl_game_lines.append(nhl_game_line)
        elif hMl[0] == '+':
            nhl_game_line = {'home':hTM,'away':aTM,'home_ats':hAts,'away_ats':aAts,
                    'home_ml':hMl,'away_ml':aMl, 'home_spread':float(oV) * -1,'away_spread':oV,
                    'over':hSpr,'under':float(hSpr) * -1}
            nhl_game_lines.append(nhl_game_line)     
        else:
            nhl_game_line = {'home':hTM,'away':aTM,'home_ats':hAts,'away_ats':aAts,
                    'home_ml':hMl,'away_ml':aMl, 'home_spread':oV,'away_spread':float(oV) * -1,
                    'over':hSpr,'under':float(hSpr) * -1}
            nhl_game_lines.append(nhl_game_line)
    except:
        pass

class GameLine:
    def __init__(self,home,away,home_ats,away_ats,home_ml,away_ml,home_spread,away_spread,over,under,home_odds,away_odds):
        self.home = home
        self.away = away
        self.home_ats = home_ats
        self.away_ats = away_ats
        self.home_ml = home_ml
        self.away_ml = away_ml
        self.home_spread = home_spread
        self.away_spread = away_spread
        self.over = over
        self.under = under
        self.home_odds = home_odds
        self.away_odds = away_odds

    def gamelines(self):
        pass

