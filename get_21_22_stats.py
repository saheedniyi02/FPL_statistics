import requests

general_info = requests.get(
    "https://fantasy.premierleague.com/api/bootstrap-static/"
).json()
player_infos = general_info["elements"]
gameweek = 1
all_stats = []
for player_info in player_infos:
    id = player_info["id"]
    link = f"https://fantasy.premierleague.com/api/element-summary/{id}/"
    try:
        print(id)
        stats_summary = requests.get(link).json()
        stats_2022 = stats_summary["history_past"][-1]
        all_stats.append(stats_2022)
    except:
        pass

import pandas as pd

df = pd.DataFrame(all_stats)
df.to_csv("cleaned_players_21_22_2.csv")
