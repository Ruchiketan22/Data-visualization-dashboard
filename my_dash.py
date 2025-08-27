import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Initialize the app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Create the layout
app.layout = dbc.Container(
    [
        # Header
        html.H1("Data Visualization Dashboard", style={"textAlign": "center", "marginBottom": "20px"}),
        html.P("Interactive dashboard for exploring dataset insights", style={"textAlign": "center", "marginBottom": "30px"}),
        
        # Sidebar
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader("Controls"),
                                dbc.CardBody(
                                    [
                                        dcc.Dropdown(
                                            id="metric-dropdown",
                                            options=[
                                                {"label": "Metric 1", "value": "metric1"},
                                                {"label": "Metric 2", "value": "metric2"},
                                            ],
                                            value="metric1",
                                            placeholder="Select a metric"
                                        )
                                    ]
                                )
                            ]
                        )
                    ],
                    width=3,
                    style={"marginRight": "20px"}
                ),
                
                # Main Content
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(id="chart1"), width=6),
                                dbc.Col(dcc.Graph(id="chart2"), width=6)
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dcc.Graph(id="chart3"), width=12)
                            ]
                        )
                    ],
                    width=9
                )
            ]
        )
    ],
    fluid=True,
    className="dashboard-container"
)

# Run the app
if __name__ == "__main__":

    app.run(debug=True)
