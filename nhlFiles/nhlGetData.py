import requests
from bs4 import BeautifulSoup
import sqlite3
from nhlData import *
import os

dirname = os.path.dirname(__file__)

def nhldb(team,year):
    year = year
    data = []
    s = 'stats'
    a = 0
    content = requests.get('https://www.hockey-reference.com/teams/{}/{}_gamelog.html'.format(team.upper(),year))
    soup = BeautifulSoup(content.content, 'html.parser')
    td = soup.find_all('td')
    for td1 in td:
        data.append(td1.text)
        Date = data[0::31]
        h_a = data[1::31]
        Opponent = data[2::31]
        GF = data[3::31]
        GA = data[4::31]
        W_L = data[5::31]
        blank1 = data[6::31]
        blank2 = data[7::31]
        S = data[8::31]
        PIM = data[9::31]
        PPG = data[10::31]
        PPO = data[11::31]
        SHG = data[12::31]
        blank3 = data[13::31]
        oS = data[14::31]
        oPIM = data[15::31]
        oPPG = data[16::31]
        oPPO = data[17::31]
        oSHG = data[18::31]
        blank4 = data[19::31]
        CF = data[20::31]
        CA = data[21::31]
        CFP = data[22::31]
        FF = data[23::31]
        FA = data[24::31]
        FFP = data[25::31]
        FOW = data[26::31]
        FOL = data[27::31]
        FOP = data[28::31]
        oZS = data[29::31]
        PDO = data[30::31]
        conn = sqlite3.connect("{}-{}-hockey.db".format(team,year))
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Stats(Name TEXT,Date TEXT,h_a TEXT, Opponent TEXT,GF TEXT,GA TEXT,W_L TEXT,S TEXT,PIM TEXT,PPG TEXT, PPO TEXT,SHG TEXT,oS TEXT,oPIM TEXT,oPPG TEXT, oPPO TEXT,oSHG TEXT,CF TEXT ,CA TEXT,CFP TEXT,FF TEXT,FA TEXT,FFP TEXT,FOW TEXT,FOL TEXT,FOP TEXT,oZS TEXT,PDO TEXT)')
    for x in range(int(len(data) / 31)):
        Date1 = Date[a]
        h_a1 = h_a[a]
        Opponent1 = Opponent[a]
        GF1 = GF[a]
        GA1 = GA[a]
        W_L1 = W_L[a]
        S1 = S[a]
        PIM1 = PIM[a]
        PPG1 = PPG[a]
        PPO1 = PPO[a]
        SHG1 = SHG[a]
        oS1 = oS[a]
        oPIM1 = oPIM[a]
        oPPG1 = PPG[a]
        oPPO1 = PPO[a]
        oSHG1 = SHG[a]
        CF1 = CF[a]
        CA1 = CA[a]
        CFP1 = CFP[a]
        FF1 = FF[a]
        FA1 = FA[a]
        FFP1 = FFP[a]
        FOW1 = FOW[a]
        FOL1 = FOL[a]
        FOP1 = FOP[a]
        oZS1 = oZS[a]
        PDO1 = PDO[a]
        cur.execute('INSERT INTO Stats(Name,Date,h_a,Opponent,GF,GA,W_L,S,PIM,PPG,PPO,SHG,oS,oPIM,oPPG,oPPO,oSHG,CF,CA,CFP,FF,FA,FFP,FOW,FOL,FOP,oZS,PDO) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(team,Date1,h_a1,Opponent1,GF1,GA1,W_L1,S1,PIM1,PPG1,PPO1,SHG1,oS1,oPIM1,oPPG1,oPPO1,oSHG1,CF1,CA1,CFP1,FF1,FA1,FFP1,FOW1,FOL1,FOP1,oZS1,PDO1))
        conn.commit()
        print(FA1)
        try:
            a += 1
        except:
            pass

def getStats(team,year):
    a = 0
    for x in team:
        if a > 0:
            x = x.lower()
        a += 1
    filename = os.path.join(dirname, f'nhlDb/{team}-{year}-stats.db')
    filename2 = os.path.join(dirname, f'nhlDb/{team.upper()}-{year}-stats.db')
    filename3 = os.path.join(dirname, f"nhlDb/{team.upper()}-{year}-hockey.db")
    try:
        conn = sqlite3.connect(filename)
    except:
        try:
            conn = sqlite3.connect(filename2)
        except:
            conn = sqlite3.connect(filename3)
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM Stats")
    except:
        cur.execute("SELECT * FROM Stats2")
    rows = cur.fetchall()
    return rows