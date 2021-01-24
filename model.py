from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import cumestatsteam
import json

# Basic Request
# player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
# print(player_info.available_seasons.get_json())
# leBron = player_info.available_seasons.get_json()
# json_object = json.loads(teams.get_teams())
# json_format = json.dumps(json_object, indent=2)
# print(json_format)

cumestatsteam.total_team_stats()
