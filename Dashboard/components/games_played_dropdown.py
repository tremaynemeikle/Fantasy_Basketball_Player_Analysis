# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids


#data = pd.read_pickle("/Users/trey/Desktop/Python Projects/Spotify EDA/Dashboard/components/data/playlist_data.pickle")

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    
    game_number_options = [number for number in range(0, 82)]
    
    return html.Div(children = [html.H5("Minimum Games Played"), 
                                dcc.Dropdown(
                                            id = ids.GAMES_PLAYED_DROPDOWN,
                                            options = [{"label": games, "value": games} for games in game_number_options],
                                            multi = False,
                                            value = 0
                                            ),
                                
                                ]
                    )
# %%
