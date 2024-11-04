import uuid
import json
import dash
from dash import Dash, dcc
import dash_bootstrap_components as dbc
from navbar import navbar
from common import ClientState, client_state_id

# @TODO
# - attention les exceptions comme PreventUpdate vont empecher l'appel d'autre callback (comme celle qui affichent le dcc.Store)
# - utiliser ag-grid
# - export CSV de ag-grid
# - export CSV des data d'un graphe
# - component pour faire filter et groupby (utiliser une modale)
# - utiliser des <input type="file"> de dbc
# - mettre en place un client session-id
# - mettre en place un server-state pour chaque session-id
# - discuter avec olivier comment associer un label a une source alors qu'on a des paths avengers et des paths esa
# est ce que le driver c'est le path avengers ?
# est ce que dans tous les calculs on aura tjrs besoin de data avengers ? (e.g. pour les calculs ou on n'a que des perfs)

def layout(client_state: ClientState):
    return [
        dcc.Location(
            id="url", refresh="callback-nav"
        ),  # callback-nav to allow the update of Location.href from a callback Output
        dcc.Store(id=client_state_id, data=json.dumps(client_state)),
        navbar(),
        dbc.Container(fluid=True, children=[dash.page_container]),
    ]


if __name__ == "__main__":
    client_state: ClientState = {
        "session_id": str(uuid.uuid4()),
        "config_path": None,
        "config": None,
    }
    app = Dash(__name__, use_pages=True, pages_folder=".", external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = layout(client_state)
    app.run(debug=True)
