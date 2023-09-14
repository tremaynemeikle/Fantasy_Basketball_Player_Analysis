import pandas as pd

import requests

from bs4 import BeautifulSoup as bsoup


class Basketball_Reference:
    
    def __init__(self):
        pass
         
    def Player_Data(self, year_start, year_end, stat, write = False, path = "~/Desktop/"):
        
        stat_table = {"total": "totals",
                      "per_game": "per_game",
                      "per100": "per_poss",
                      "adv": "advanced",
                      "shooting": "shooting"
                     }
        
        html_id = {"total": "totals",
                   "per_game": "per_game_stats",
                   "per100": "per_poss_stats",
                   "adv": "advanced_stats",
                   "shooting": "shooting_stats"
                    }
        
        chosen_table = stat_table[stat]
        chosen_id = html_id[stat]
        
        years = list(range(year_start, year_end + 1))
        total_table = []

        for year in years:
   
           # Only uncomment to if there is a need to write new data
            html = requests.get(f"https://www.basketball-reference.com/leagues/NBA_{year}_{chosen_table}.html").text
           # time.sleep(random.randint(3,7))

           # with open(f"/Users/trey/Desktop/NBA/Nba Data/Page Scrape/adv_player_stats_{year}.html", "w+") as f:
           #        f.write(html)

           # print(f"Written advanced player stats for year {year}")

            #with open(f"/Users/trey/Desktop/NBA/Nba Data/Page Scrape/leagues/NBA_{year}_totals") as f:
            #    html = f.read()

            soup = bsoup(html, "html.parser")
    
            table = soup.find_all("table", id = f"{chosen_id}")

            header = soup.find_all("tr", class_ = "over_header")

            for tag in header:
                tag.decompose()

            table = pd.read_html(str(table))[0]

            table["Season"] = year

            total_table.append(table)

        total_table = pd.concat(total_table)
        total_table.reset_index(drop = True, inplace = True)


        # Strip all "*" characters
        for i in range(0, total_table.shape[0]):
            total_table["Player"][i] = total_table["Player"][i].rstrip("*")

        total_table.drop(total_table.loc[total_table["Rk"] == "Rk"].index, inplace = True)

        total_table = total_table.dropna(axis = 1, how = "all")
        total_table.set_index("Player", inplace = True)

        total_table = total_table.fillna(0)
        total_table.isna().sum()
        
       
        if stat == "shooting":
            total_table = total_table.rename(columns={"FG%": "FG%_Team",
                                                      '2P': '2P_%_FGA_by_distance', 
                                                      '0-3': '0-3_%_FGA_by_distance',
                                                      "3-10": "3-10_%_FGA_by_distance",
                                                      "10-16": "10-16_%_FGA_by_distance",
                                                      "16-3P": "16-3P_%_FGA_by_distance",
                                                      "3P": "3P_%_FGA_by_distance",
                                                      '2P.1': '2P_%_FG_by_distance', 
                                                      '0-3.1': '0-3_%_FG_by_distance',
                                                      "3-10.1": "3-10_%_FG_by_distance",
                                                      "10-16.1": "10-16_%_FG_by_distance",
                                                      "16-3P.1": "16-3P_%_FG_by_distance",
                                                      "3P.1": "3P_%_FG_by_distance",
                                                      "2P.2": "2P_%_FG_Ast'd",
                                                      "3P.2": "3P_%_FG_Ast'd",
                                                      "%FGA": "%FGA_Dunks",
                                                      "Md.": "Md_Dunks",
                                                      "%FGA.1": "%FGA_Layups",
                                                      "Md..1": "Md_Layups",
                                                      "%3PA": "%3PA_Corner",
                                                      "3P%": "3P%_ Corner",
                                                      "Att.": "Att_Heaves",
                                                      "Md..2": "Md_Heaves"

                                                     })
        else:
            pass
        
        if write == True:
            
            from pathlib import Path
            
            filepath = Path(f"{path}{stat}_{year_start}_{year_end}.csv")  
            #filepath = Path("/Users/trey/Desktop/Nba/Nba Data/csv/player_per_100_2012-2018.csv")  
            filepath.parent.mkdir(parents=True, exist_ok=True)  
            total_table.to_csv(filepath) 
        
        else:
            pass
        
        return total_table

        