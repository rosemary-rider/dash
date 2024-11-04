from dash import html, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_ag_grid as dag


def grid_layout(grid_id, grid_button_id):
    return [
        html.Div(dbc.Button("Download csv", id=grid_button_id, color="secondary", outline=True), className="d-flex justify-content-end mb-1"),
        dag.AgGrid(id=grid_id, dashGridOptions={"domLayout": "autoHeight"}),
    ]


def grid_cbs(grid_id, grid_button_id):
    @callback(
        Output(grid_id, "exportDataAsCsv"),
        Input(grid_button_id, "n_clicks"),
        prevent_initial_call=True,
    )
    def on_export_button_click(n_clicks):
        return True

