import json
import dash
import pathlib
from dash import html, callback, Output, Input, State, dcc
import dash_bootstrap_components as dbc
from common import client_state_id, ClientState, Config, server_state

dash.register_page(__name__, path="/")

button_id = "config-button"
input_id = "config-input"
alert_div_id = "config-alert"
content_div_id = "config-content"
avg_timeseries_id = "config-avengers-timeseries"


def layout(**kwargs):
    return html.Div(
        [
            dbc.Input(
                id=input_id,
                className="mt-3",
                type="text",  # cannot be type="file" because the config file must be loaded on server-side
                placeholder="File path",
            ),
            dbc.Button("Load config", id=button_id, color="primary", className="mt-3"),
            html.Div(id=alert_div_id, className="mt-3"),
        ]
    )


@callback(
    Output(client_state_id, "data"),
    Output(alert_div_id, "children"),
    Input(button_id, "n_clicks"),
    State(input_id, "value"),
    State(client_state_id, "data"),
    running=[
        (Output(button_id, "disabled"), True, False),
    ],
)
def on_load_button_click(n_clicks, value, data):
    if n_clicks is None or value is None:
        return data, None
    client_state: ClientState = json.loads(data)
    client_state["config_path"] = value
    server_state.pop(client_state["session_id"], None)
    client_state["config"] = None
    alert = None
    try:
        config: Config = json.loads(pathlib.Path(value).read_text(encoding="UTF-8"))
        client_state["config"] = config
        alert = dbc.Alert("Config loaded", dismissable=True, color="success")
    except:
        alert = dbc.Alert("Config load failed", dismissable=True, color="danger")
    return json.dumps(client_state), alert


@callback(
    Output(input_id, "value"),
    Input(client_state_id, "data"),
)
def on_state_change(data):
    client_state: ClientState = json.loads(data)
    return client_state["config_path"]
