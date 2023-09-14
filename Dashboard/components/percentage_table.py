# %%
from dash import Dash, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd

from . import ids
from . import dash_functions as dash_func

def render(app: Dash, data: pd.DataFrame) -> html.Div:

    initial_data_copy = data.copy()
    # Get position averages
    basic_info = ["Player", "G", "MP", "Pos", "Tm"]
    fantasty_category = ["FG%", "FT%", "3P", "PTS", "TRB", "AST", "BLK", "STL", "TOV"]
    drop_list = [x for x in initial_data_copy.columns if x not in fantasty_category and x not in basic_info]
    initial_data_copy.drop(labels = drop_list, axis = 1, inplace = True)

    dash_func_ = dash_func.dash_functions()

    (style, legend) = dash_func_.discrete_background_color_bins(initial_data_copy, n_bins=5, columns='all')
    
    @app.callback(
                 Output(ids.PERCENTAGE_TABLE, "data"),
                 [Input(ids.MINUTE_DROPDOWN, "value"),
                 Input(ids.GAMES_PLAYED_DROPDOWN, "value"),
                 Input(ids.POSITION_DROPDOWN, "value")]
                )
    def update_table(minutes: list[int], games: list[str], position: list[str]):

        data_copy = initial_data_copy.copy()

        filtered_data = data_copy.query("MP > @minutes and G > @games and Pos == @position")

        category_average = {}

        for j in fantasty_category:
            category_average[j] = filtered_data[j].mean()

        filtered_data.reset_index(drop = True, inplace = True)
        
        percentage_stats = filtered_data.copy()


        for i in range(0, percentage_stats.shape[0]):
            for j in fantasty_category:

                    difference = percentage_stats.loc[i, [j]] - category_average[j]
                    percentage_stats.loc[i, [j]] = ((difference / category_average[j]) * 100)
                    percentage_stats.loc[i, [j]] = round(percentage_stats.loc[i][j], 1)

        return percentage_stats.to_dict('records')


    return dash_table.DataTable(
                                id = ids.PERCENTAGE_TABLE,
                                data = initial_data_copy.to_dict('records'), 
                                columns = [{"name": i, "id": i, "type": "float"} for i in initial_data_copy.columns],
                                page_size = 20,
                                sort_action='native',
                                style_data_conditional = style
                                )



                                
                                
                    
# %%
