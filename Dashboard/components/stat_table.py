# %%
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output
import pandas as pd


from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    
    @app.callback(
                 Output(ids.STATS_TABLE, "data"),
                 [Input(ids.MINUTE_DROPDOWN, "value"),
                 Input(ids.GAMES_PLAYED_DROPDOWN, "value"),
                 Input(ids.POSITION_DROPDOWN, "value")]
                )
    def update_table(minutes: list[int], games: list[str], position: list[str]):
        
        data_copy = data.copy()
    
        filtered_data = data_copy.query("MP > @minutes and G > @games and Pos == @position")

        return filtered_data.to_dict('records')


    return dash_table.DataTable(
                                id = ids.STATS_TABLE,
                                data = data.to_dict('records'), 
                                columns = [{"name": i, "id": i, "type": "float"} for i in data.columns],
                                page_size = 20,
                                sort_action='native'
                                
                                )



                                
                                
                    
# %%
