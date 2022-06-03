import ssl

import pandas as pd
import json
import urllib.request

h2h_leagueID = 1527695
h2h_name = 'Juwang';
firstGameweek = 1
lastGameweek = 38

data = []
df = []

for i in range(firstGameweek, lastGameweek+1):
    base = "https://fantasy.premierleague.com/api/leagues-h2h-matches/league/" + str(h2h_leagueID) + "/?page=1&event=" + str(i)
    page = urllib.request.urlopen(base)
    data.append(json.load(page))

df = pd.DataFrame(columns=['GW', 'Host Team', 'Host Score', 'Away Score', 'Away Team'])

for i in range(0, len(data)):
    nb_of_games_per_gw = len(data[i]["results"])
    for match in range(0, nb_of_games_per_gw):
        entry_1_name = data[i]["results"][match]["entry_1_name"]
        entry_1_points = data[i]["results"][match]["entry_1_points"]
        entry_2_name = data[i]["results"][match]["entry_2_name"]
        entry_2_points = data[i]["results"][match]["entry_2_points"]

        d = pd.DataFrame({'GW': firstGameweek+i, 'Host Team':entry_1_name, 'Host Score':entry_1_points, 'Away Score':entry_2_points, 'Away Team':entry_2_name}, index=[i])
        df = df.append(d)

print(df)
outputpath='h2h_score_' +str(h2h_name) + '.xlsx'
df.to_excel(outputpath,index=False,header=True)