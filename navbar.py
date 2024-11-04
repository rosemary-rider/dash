import dash_bootstrap_components as dbc


def navbar():
    return dbc.NavbarSimple(
        brand="Risk-Dashboard",
        brand_href="/",
        color="dark",
        dark=True,
        fluid=True,
        links_left=True,
        children=[
            dbc.NavItem(dbc.NavLink("Config", href="/", active="exact")),
            dbc.NavItem(dbc.NavLink("Pnl", href="/pnl", active="partial")),
        ],
    )
