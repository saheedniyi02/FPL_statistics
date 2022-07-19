import requests

id=4
player_info=requests.get(f"https://fantasy.premierleague.com/api/element-summary/4/")
player_info=player_info.json()

print(player_info["history"])
