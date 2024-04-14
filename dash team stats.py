import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests
#PLEASE LIMIT TESTING OF API REQUESTS ONLY 100 FREE REQUESTS A DAY!!!!
# Initialize the Dash app with suppress_callback_exceptions=True to avoid error messages when testing
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define API endpoint and headers
url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics?league=39&season=2020&team=33"
headers = {
    'X-RapidAPI-Key': "aa6dc5a2afmsh8be7dcdb4914cddp161bf3jsne2d975cd39bb",
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
}

# Retrieve data from the API
response = requests.get(url, headers=headers)

# Parse JSON data
try:
    if response.status_code == 200:
        data = response.json()
    else:
        data = None
except ValueError as e:
    print("Error parsing JSON:", e)
    data = None

# Define the layout of the dashboard
if data:
    app.layout = html.Div([
        html.H1("Team Statistics Dashboard"),
        html.Div([
            html.Div([
                html.H3("Statistic"),
                dcc.Dropdown(
                    id='statistic-dropdown',
                    options=[{'label': key, 'value': key} for key in data.get('response', {}).keys()],
                    value=None
                )
            ], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                html.H3("Value"),
                html.Div(id='statistic-value')
            ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
        ]),
    ])
else:
    app.layout = html.Div([
        html.H1("Team Statistics Dashboard"),
        html.Div("Failed to retrieve data from the API", style={'color': 'red', 'font-weight': 'bold'})
    ])

# Define callback to update the value based on selected statistic
@app.callback(
    Output('statistic-value', 'children'),
    [Input('statistic-dropdown', 'value')]
)
def update_statistic_value(selected_statistic):
    if data and selected_statistic:
        value = data.get('response', {}).get(selected_statistic)
        return f"{value}"
    else:
        return ""

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
