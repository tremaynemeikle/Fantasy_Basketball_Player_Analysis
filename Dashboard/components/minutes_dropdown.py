# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids


#data = pd.read_pickle("/Users/trey/Desktop/Python Projects/Spotify EDA/Dashboard/components/data/playlist_data.pickle")

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    
    minute_options = [number for number in range(0, 48)]
    
    
    return html.Div(children = [html.H5("Minimum Minutes Per Game"), 
                                dcc.Dropdown(
                                            id = ids.MINUTE_DROPDOWN,
                                            options = [{"label": minutes, "value": minutes} for minutes in minute_options],
                                            multi = False,
                                            value = 0
                                            ),
                                
                                ]
                    )
# %%
