import json
from datetime import datetime

import requests

# Data is from http://data.nba.net/10s/prod/v1/today.json
# links -> "leagueSchedule": "/prod/v1/2020/schedule.json",


def _parse_data_to_get_todays_games(games) -> str:
    game_time = "Today's NBA schedule:\n\n"
    today_date = datetime.now().strftime("%Y%m%d")
    for game_info in games:
        if game_info["startDateEastern"] == today_date:
            start_time = game_info["startTimeEastern"].replace("ET", "").strip()
            teams = game_info["gameUrlCode"].split("/")[1]
            first_team = teams[0:3]
            second_team = teams[3:]
            game_time += f'{first_team}vs{second_team}@{start_time}\n'
    return game_time


def get_todays_games() -> str:
    response = requests.get(url="http://data.nba.net/10s//prod/v1/2020/schedule.json")
    json_decoded_content = json.loads(response.content.decode())
    games = json_decoded_content["league"]["standard"]
    return _parse_data_to_get_todays_games(games)
