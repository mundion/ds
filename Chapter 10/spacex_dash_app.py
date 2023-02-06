# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

unique_launch_sites = spacex_df['Launch Site'].unique().tolist()
launch_sites = []
launch_sites.append({'label': 'All Sites', 'value': 'All Sites'})
for launch_site in unique_launch_sites:
    launch_sites.append({'label': launch_site, 'value': launch_site})

# Create a dash application
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(   id='site-dropdown',
                                                options=launch_sites,
                                                value='All Sites',
                                                placeholder="Select a Launch Site here",
                                                searchable=True
                                ),
                                # options attribute is a list of dict-like option objects (with label and value attributes). You can set the label and value all to be the launch site names in the spacex_df and you need to include the default All option. e.g., options=[{'label': 'All Sites', 'value': 'ALL'},{'label': 'site1', 'value': 'site1'}, ...]
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, 
                                                max=10000, 
                                                step=1000,
                                                marks = {
                                                0: {'label': '0 Kg', 'style': {'color': '#77b0b1'}},
                                                1000: {'label': '1000 Kg'},
                                                2000: {'label': '2000 Kg'},
                                                3000: {'label': '3000 Kg'},
                                                4000: {'label': '4000 Kg'},
                                                5000: {'label': '5000 Kg'},
                                                6000: {'label': '6000 Kg'},
                                                7000: {'label': '7000 Kg'},
                                                8000: {'label': '8000 Kg'},
                                                9000: {'label': '9000 Kg'},
                                                10000: {'label': '10000 Kg', 'style': {'color': '#f50'}},
                                                },
                                                value=[min_payload, max_payload]),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                    html.Div(dcc.Graph(id = 'success-payload-scatter-chart')),
                                        ])


# TASK 2: success-pie-chart callback based on selected site dropdown
@app.callback(
     Output(component_id = 'success-pie-chart', component_property = 'figure'),
     [Input(component_id = 'site-dropdown', component_property = 'value')]
)
def get_pie_chart(site_dropdown):
    if (site_dropdown == 'All Sites' or site_dropdown == 'None'):
        filter_df  = spacex_df[spacex_df['class'] == 1] # All Success only for all sites.
        fig = px.pie(
                filter_df,
                names = 'Launch Site',
                title = 'Total Success Launches by All Sites'
            )
    else:
        filter_df  = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]
        fig = px.pie(
                filter_df,
                names = 'class',
                title = 'Total Success Launches for Site &#8608; '+site_dropdown,
            )
    return fig

# TASK 3, 4: Range Slider or Scatter Chart Callback
@app.callback(
     Output(component_id = 'success-payload-scatter-chart', component_property = 'figure'),
     [Input(component_id = 'site-dropdown', component_property = 'value'), 
     Input(component_id = "payload-slider", component_property = "value")]
)
def get_scattergraph(site_dropdown,payload_slider):
    if (site_dropdown == 'All Sites' or site_dropdown == 'None'):
        low, high = payload_slider
        filter_df  = spacex_df
        inrange = (filter_df['Payload Mass (kg)'] > low) & (filter_df['Payload Mass (kg)'] < high)
        fig = px.scatter(
                filter_df[inrange], 
                x = "Payload Mass (kg)", 
                y = "class",
                labels={
                     "Payload Mass (kg)": "Payload Mass in kg",
                     "class": "Success",
                     "Booster Version Category": "Booster Version Category"
                 },
                title = 'Payload Mass vs Success for All Sites',
                color="Booster Version Category",
                size='Payload Mass (kg)',
                hover_data=['Payload Mass (kg)']
            )
    else:
        low, high = payload_slider
        filter_df  = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]
        inrange = (filter_df['Payload Mass (kg)'] > low) & (filter_df['Payload Mass (kg)'] < high)
        fig = px.scatter(
                filter_df[inrange],
                x = "Payload Mass (kg)",
                y = "class",
                labels={
                     "Payload Mass (kg)": "Payload Mass in kg",
                     "class": "Success",
                     "Booster Version Category": "Booster Version Category"
                 },
                title = 'Payload Mass vs Success for '+site_dropdown,
                color="Booster Version Category",
                size='Payload Mass (kg)',
                hover_data=['Payload Mass (kg)']
            )
    return fig

if __name__ == '__main__':
    app.run_server()