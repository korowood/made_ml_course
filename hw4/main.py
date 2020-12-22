import dash
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd

pd.set_option('display.max_columns', 100)
import numpy as np

df = pd.read_csv("players_stats_by_season_full_details.csv")
cols_dict = {
    'GP': 'Games_Played',
    'MIN': 'Minutes_Played',
    'FGM': 'Field_Goals_Made',
    'FGA': 'Field_Goals_Attempts',
    '3PM': 'Three_Points_Made',
    '3PA': 'Three_Points_Attempts',
    'FTM': 'Free_Throws_Made',
    'FTA': 'Free_Throws_Attempts',
    'TOV': 'Turnovers',
    'PF': 'Personal_Fouls',
    'ORB': 'Offensive_Rebounds',
    'DRB': 'Defensive_Rebounds',
    'REB': 'Rebounds',
    'AST': 'Assists',
    'STL': 'Steals',
    'BLK': 'Blocks',
    'PTS': 'Points'
}
df = df.rename(columns=cols_dict)
nba = df.query('League == "NBA"')

content = 'Данный датасет включает в себя: \
Информацию о 49 лигах с сезона 1999 года по 2020 год. \
Данные о 11к игроках, такие как: дата рождения, рост, вес, национальность, место учебы. \
А так же статистику за сезон: бросковые данные (двух-, трехочковые, штрафные), подборы, блоки, ассисты(пасы), минуты на площадке и тд.'

point_leaders = nba.groupby('Player').sum().sort_values(by='Points', ascending=False).head(10).reset_index()
point_leaders = point_leaders.drop(['weight_kg', 'weight', 'height_cm', 'birth_year'], axis=1)

app = dash.Dash(__main__)
server = app.server

app.layout = html.Div([
    html.H1(children="TEST1",
            style={
                'textAlign': 'center',
                'color': '#456FBV'
            }),
    html.Div(content),

    dcc.Graph(
        id="samplechart",
        figure={
            'data': [
                {'x': point_leaders['Player'], 'y': point_leaders['Points'], 'type': 'bar', 'name': 'First char'}
            ],
            'layout': {
                'title': 'simple'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server()
