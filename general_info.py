import requests

general_information=requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
general_information=general_information.json()
#player_info1
#print(general_information["elements"][0])
#id=id
#position
#print(general_information["element_types"])

