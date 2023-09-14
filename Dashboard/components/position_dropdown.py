# %%
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd


from . import ids


#data = pd.read_pickle("/Users/trey/Desktop/Python Projects/Spotify EDA/Dashboard/components/data/playlist_data.pickle")

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    
    position_options = sorted(data["Pos"].unique())
    @app.callback(
                 Output(ids.POSITION_DROPDOWN, "value"),
                 Input(ids.SELECT_ALL_POSITION_BUTTON, "n-clicks")
                )
    def restore_position_options(_:int):
        return position_options
    
    return html.Div(children = [html.H5("Select Position"), 
                                dcc.Dropdown(
                                            id = ids.POSITION_DROPDOWN,
                                            options = [{"label": position, "value": position} for position in position_options],
                                            
                                            multi = True
                                            ),
                                html.Button(
                                            className = "dropdown-button",
                                            children = ["Restore All"],
                                            id = ids.SELECT_ALL_POSITION_BUTTON
                                            )
                                ]
                    )
# %%
