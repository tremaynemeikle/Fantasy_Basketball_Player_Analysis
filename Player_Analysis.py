# %%
import Basketball_Ref_API as nba
import pandas as pd

data = nba.Basketball_Reference()

# Get player stats for given seasons

player_stats = data.Player_Data(year_start = 2022, year_end = 2023, stat = "per_game")

table = player_stats.sort_values(by = "TRB", ascending = False)


# Table data type correction

object_columns = ["Pos", "Tm"]
int_columns = ["Age", "G", "GS", "Season", "Rk"]
float_columns = [i for i in table.columns if i not in int_columns and i not in object_columns]

for i in table.columns:

    if i in int_columns:
        table[i] = table[i].astype(int)

    elif i in float_columns:
        table[i] = table[i].astype(float)
    
    else:
        table[i] = table[i].astype(object)


# Current season with players that play more than 10 minutes per game and played more than 25 games

# current_season = table.loc[(table["Season"] == 2023) & (table["MP"] > 30) & (table["G"] > 40)]
current_season = table.loc[(table["Season"] == 2023)]
current_season.reset_index(drop = False, inplace = True)



current_season.to_pickle("Dashboard/data/player_data.pkl") 

# Get position averages
basic_info = ["Player", "G", "MP", "Pos", "Tm"]
fantasty_category = ["FG%", "FT%", "3P", "PTS", "TRB", "AST", "BLK", "STL", "TOV"]
drop_list = [x for x in current_season.columns if x not in fantasty_category and x not in basic_info]
current_season.drop(labels = drop_list, axis = 1, inplace = True)


position_average = {}

for i in current_season["Pos"].unique():
    position_table = current_season.loc[current_season["Pos"] == i]

    for j in fantasty_category:
        position_average[i + "-" + j] = position_table[j].mean()

current_season.reset_index(drop = True, inplace = True)

percentage_stats = current_season.copy()

for i in range(0, percentage_stats.shape[0]):
    for j in fantasty_category:

            difference = percentage_stats.loc[i, [j]] - position_average[percentage_stats.loc[i]["Pos"] + "-" + j] 
            percentage_stats.loc[i, [j]] = ((difference / position_average[percentage_stats.loc[i]["Pos"] + "-" + j]) * 100)
            percentage_stats.loc[i, [j]] = round(percentage_stats.loc[i][j], 2)

percentage_stats.to_pickle("Dashboard/data/percentage_data.pkl") 
# %%
