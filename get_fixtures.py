import requests

fixtures=requests.get("https://fantasy.premierleague.com/api/fixtures/")
fixtures=fixtures.json()

print(fixtures)
