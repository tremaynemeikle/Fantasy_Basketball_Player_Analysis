# %%
from dash import Dash, html
from dash_bootstrap_components.themes import SUPERHERO, BOOTSTRAP
import dash_bootstrap_components as dbc

from components.layout import create_layout

import pandas as pd

import os

import plotly.express as px


os.chdir("/Users/trey/Desktop/Python Projects/Fantasy Basketball/Dashboard")

# %%
def main() -> None:

    data = pd.read_pickle("data/player_data.pkl")
    
    app = Dash(external_stylesheets = [BOOTSTRAP, dbc.icons.BOOTSTRAP])

    app.title = "Fantasy Player Stat Analysis"
    app.layout = create_layout(app, data)

    app.run()


if __name__ == "__main__":
    main()


# %%
