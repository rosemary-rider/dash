import pandas as pd
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc


def graph_layout(graph_id, graph_button_id, graph_download_id):
    return [
        dcc.Download(id=graph_download_id),
        html.Div(dbc.Button("Download csv", id=graph_button_id, color="secondary", outline=True), className="d-flex justify-content-end"),
        dcc.Graph(id=graph_id, config={"displayModeBar": True, "displaylogo": False}),
    ]


def graph_cbs(graph_button_id, graph_download_id):
    @callback(
        Output(graph_download_id, "data"),
        Input(graph_button_id, "n_clicks"),
        prevent_initial_call=True,
    )
    def on_export_button_click(n_clicks):
        df = pd.DataFrame()
        return dcc.send_data_frame(df.to_csv, "export.csv")