import dash
import json
import time
import pandas as pd
from dash import html, callback, Output, Input, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from common import server_state, client_state_id, ClientState
from grid import grid_layout, grid_cbs
from graph import graph_layout, graph_cbs

dash.register_page(__name__, path="/pnl")
content_div_id = "pnl-content"
grid_id = "pnl-grid"
grid_button_id = "pnl-grid-export"
graph_id = "pnl-graph"
graph_download_id = "pnl-graph-download"
graph_button_id = "pnl-graph-export"
grid_cbs(grid_id, grid_button_id)
graph_cbs(graph_button_id, graph_download_id)

def layout(**kwargs):
    return [
        html.H1("Metrics", className="mt-3"),
        dbc.Spinner(grid_layout(grid_id, grid_button_id), color="primary"),
        html.H1("Pnl", className="mt-3"),
        dbc.Spinner(graph_layout(graph_id, graph_button_id, graph_download_id), color="primary"),
    ]


@callback(
    Output(grid_id, "rowData"),
    Output(grid_id, "columnDefs"),
    Input(client_state_id, "data"),
)
def render_grid(data):
    client_state: ClientState = json.loads(data)
    session_state = server_state[client_state["session_id"]]
    time.sleep(2)
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")
    grid_row_data = df.head(3).to_dict("records")
    grid_column_defs = [{"field": i, "filter": True} for i in df.columns]
    return grid_row_data, grid_column_defs


@callback(
    Output(graph_id, "figure"),
    Input(client_state_id, "data"),
)
def render_graph(data):
    client_state: ClientState = json.loads(data)
    session_state = server_state[client_state["session_id"]]
    time.sleep(1)
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")
    graph_figure = px.line(df, x="direction", y="frequency")
    return graph_figure
