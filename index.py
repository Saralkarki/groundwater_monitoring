import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import dash_auth

from app import app
from layouts import main_layout, pilot_layout, banke_stw_layout, banke_dtw_layout, bardiya_stw_layout,bardiya_dtw_layout,history_layout, meta_layout, upload_layout
import callbacks
import os
VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin@123',
    'administrator': 'admin@123'
}




server = app.server

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)



def drawLogos(): return html.Div([
                html.Img(src = 'assets/images/partners.png',style={"width":"100%"},className="float-left"),
                html.Img(src = 'assets/images/gon.png'),
                html.Img(src = 'assets/images/gwrdb-new.gif'),
                html.Img(src = 'assets/images/csisa-logo.png',style={"width":"12%"}),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),

                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ])

def drawHeader(): return dbc.Container([
    dbc.Row([
        
        dbc.Col(
        html.H1("Groundwater Monitoring Dashboard"),
        width={"size": 5, "offset": 3},
        ),
        
        dbc.Col([
                html.Div(
                html.Img(src = 'assets/images/partners.png',className="float-right"),
                className="col-1 offset-7"
                ),
                html.Img(src = 'assets/images/gon.png'),
                html.Img(src = 'assets/images/gwrdb-new.gif'),
                html.Img(src = 'assets/images/csisa-logo.png',style={"width":"12%"}),
                ],
        width={"size": 5, "offset": 7},
        ),
    ]),

    dbc.Row([
        
        dbc.Col(
        html.P("Real-time groundwater level database for data sharing and monitoring."),
        width={"size": 6, "offset": 3},
        )
        ]),
    
    dbc.Row([html.Br(),html.Br()]),
    ],fluid=True, style={'color': 'primary'}
)

partner_card = dbc.Card([
    dbc.CardBody([
        dbc.CardImg(src='assets/images/partners.png')
        ])
    ])
gon_card = dbc.Card([
    dbc.CardBody([
        dbc.CardImg(src='assets/images/gon.png')
        ])
    ])
csisa_card = dbc.Card([
    dbc.CardBody([
        dbc.CardImg(src='assets/images/csisa-logo.png')
        ])
    ])
gwrdb_card = dbc.Card([
    dbc.CardBody([
        dbc.CardImg(src='assets/images/gwrdb-new.gif')
        ])
    ])

logos_card = dbc.Card([
    dbc.CardBody([
        dbc.CardImg(src='assets/images/ilogos.png')
        ])
    ],color="light", outline=True)


header_card = dbc.Card([
    dbc.CardBody([
        html.H1("Groundwater Monitoring Dashboard", className="card-title"),
        html.H4("    Real-time groundwater database for Nepal")
        ])
    ],style={'backgroundColor':'light'},color="light", outline=True)


logos = html.Div([
    dbc.Row(html.Br()),
    dbc.Row([
        dbc.Col([html.Div(header_card)],width={"offset":2,"size":4}),
        dbc.Col([html.Div(logos_card)],width={"offset":1, "size":3}),
        ],no_gutters=True,align="center")

        
    ],style={'backgroundColor':'light'})

row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div(gon_card),width={"offset":7,"size":1}),
                dbc.Col(html.Div(gwrdb_card)),
                dbc.Col(html.Div(csisa_card)),
            ]
        ),
    ]
)





nav =  dbc.Nav([
            dbc.NavLink("Real-Time Monitoring", href="/realtime"),
            dbc.NavLink("Database", href="/pilot"),
            dbc.NavLink("Past-Database", href="/historical_data"),
            dbc.NavLink("Meta-Data", disabled=True, href="/"),
            ])
    # add a dbc nav 

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Real-Time Monitoring", active=True, href="/realtime",style={"width":"25%"})),
        dbc.NavItem(dbc.NavLink("Database", href="/pilot")),
        dbc.NavItem(dbc.NavLink("Past-Database", href="/historical_data")),
        dbc.NavItem(dbc.NavLink("Meta-Data", href="/"))
    ],
    brand="Groundwater Resources Development Board",
    brand_href="http://www.gwrdb.gov.np/",
    color="info"
)

navbar1 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Real-Time Monitoring", href="/realtime",style={"text-align":"center","padding-right":50,"padding-left":50,"width":250})),
        dbc.DropdownMenu(
            children=[
           #     dbc.DropdownMenuItem("Datasets", header=True),
                dbc.DropdownMenuItem("All wells", href="/pilot"),
                dbc.DropdownMenuItem("Banke shallow wells", href="/pilot/bstw"),
                dbc.DropdownMenuItem("Banke deep wells", href="/pilot/bdtw"),
                dbc.DropdownMenuItem("Bardiya shallow wells", href="/pilot/bastw"),
                dbc.DropdownMenuItem("Bardiya deep wells", href="/pilot/badtw"),
            ],
            nav=True,
            in_navbar=True,
            label="Datasets",
            style={"text-align":"center","padding-right":50,"padding-left":50,"width":250}
        ),
#        dbc.NavItem(dbc.NavLink("Database", href="/pilot",style={"text-align":"center","padding-right":50,"padding-left":50,"width":250})),
        dbc.NavItem(dbc.NavLink("Past-Database", href="/historical_data",style={"text-align":"center","padding-right":50,"padding-left":50,"width":250})),
        dbc.NavItem(dbc.NavLink("Meta-Data", href="/",style={"text-align":"center","padding-right":50,"padding-left":50,"width":250})),
    ],
   # brand="GW Dashboard",
    #brand_href="/",
    color="info",
    dark=True,
    sticky="top",
#    style={"width":"100%","overflow":"auto"},
)


#ube Well', href = '/pilot/bstw', style
##', href = '/pilot/bdtw', style = {'fon
# Well', href = '/pilot/bastw', style =
#ll', href = '/pilot/badtw', style = {'



app.layout = html.Div([
    dbc.Row([dbc.Col([
    logos,
    navbar1,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
    ])])
# print(app.layout)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return meta_layout
    elif pathname == '/pilot':
        return pilot_layout
    elif pathname == '/realtime':
        return main_layout
    elif pathname == '/historical_data':
        return history_layout
    elif pathname == '/pilot/bstw':
        return banke_stw_layout
    elif pathname == '/pilot/bdtw':
        return banke_dtw_layout
    elif pathname == '/pilot/bastw':
        return bardiya_stw_layout
    elif pathname == '/pilot/badtw':
        return bardiya_dtw_layout
    elif pathname == '/pilot/upload':
        return upload_layout
    else:
        return '404 - Page Not Found'

if __name__ == '__main__':
    app.run_server(debug=True, port = 8000)