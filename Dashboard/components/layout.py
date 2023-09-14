# %%
import pandas as pd

from dash import Dash, html, dcc, dash_table
from dash_bootstrap_components.themes import SUPERHERO
import dash_bootstrap_components as dbc

from . import position_dropdown 
from . import minutes_dropdown
from . import games_played_dropdown 
from . import stat_table
from . import percentage_table 


def create_layout(app:Dash, data: pd.DataFrame) -> html.Div:
    return dbc.Container(
                        [
                        # Title head
                        dbc.Row(
                                [
                                html.H1(app.title), 
                                html.Hr()
                                ],
                                className = "text-center border-0",
                                justify="center"
                                ),
                        # Critera Section
                        dbc.Row(
                                
                                [
                                dbc.Col(
                                        dbc.Card(
                                                [
                                                minutes_dropdown.render(app, data)
                                                ],
                                                body = True,
                                                className = "shadow-lg rounded p-auto"
                                                ),
                                        width = 3,
                                        align="center",
                                        ), 
                                dbc.Col(
                                        dbc.Card(
                                                [
                                                games_played_dropdown.render(app, data)
                                                ],
                                                body = True,
                                                className = "shadow-lg rounded p-auto"
                                                ),
                                        width = 3,
                                        align="center",
                                        ),
                                dbc.Col(
                                        dbc.Card(
                                                [
                                                position_dropdown.render(app, data)
                                                ],
                                                body = True,
                                                className = "shadow-lg rounded p-auto"
                                                ),
                                        width = 3,
                                        align="center",
                                        )
                                ], 
                                justify="center"              
                                ),
                                
                        html.Br(),
                        html.Br(),

                        html.Br(),
                        html.Br(),
                        
                        # Stats Table
                        dbc.Row(
                                dbc.Col(
                                        dbc.Card(
                                                [
                                                stat_table.render(app, data)
                                                ],
                                                body = True,
                                                className = "shadow-lg rounded p-auto"
                                                ),
                                       # width = 5,
                                        align="center",
                                        ), 
                                justify="center"                
                                ),
                        html.Br(),
                        html.Br(),

                        # Percentage Table
                        dbc.Row(
                                dbc.Col(
                                        dbc.Card(
                                                [
                                                percentage_table.render(app, data)
                                                ],
                                                body = True,
                                                className = "shadow-lg rounded p-auto"
                                                ),
                                       # width = 5,
                                        align="center",
                                        ), 
                                justify="center"                
                                ),
                        html.Br(),
                        html.Br(),

                        ],

                        className = "bg-light bg-gradient w-100",
                        fluid = True
                        )