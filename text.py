import pandas as pd
import numpy as np
df=pd.read_csv("cleaned_merged_seasons.txt")

#print(df.columns)
df_cut=df[["name","season_x","team_x","opp_team_name","position","assists","bonus","bps","clean_sheets","fixture","goals_conceded","goals_scored","kickoff_time","minutes","own_goals","penalties_missed","penalties_saved","red_cards","saves","selected","team_a_score","team_h_score","transfers_in","transfers_out","value","was_home","yellow_cards","total_points"]]

print(df_cut.dropna()["season_x"].value_counts())
#print(df_cut[df_cut["team_x"]==pd.NA])
#for i in df_cut.columns:
#	print(df[i].value_counts())
