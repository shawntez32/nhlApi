from fastapi import FastAPI
import sys, os
sys.path.append(os.path.dirname((__file__)) + "/nhlFiles/")
from nhlGameLines import *
from nhlGetData import *

app = FastAPI()

@app.get("/")
def home():
    return {"Data":"Set"}

@app.get("/nhl/gamelines")
def get_lines():
    return {"Data":nhl_game_lines}
a = 0
@app.get("/nhl/{team}/{year}")
def get_stats(team,year):
    results = []
    try:
        results = getStats(team,year)
        return {"Team_Stats":results}
    except:
        data = 'wait'
        return {"Data":data}
    print(results)

@app.get("/nhl/{team}/{year}")
def get_stats(team,year):
    results = []
    try:
        results = getPitching(team,year)
        return {"Team_Stats":results}
    except:
        data = 'wait'
        return {"Data":data}
