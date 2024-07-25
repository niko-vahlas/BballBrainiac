import json
import requests

# URL for NBA schedule
url = "https://cdn.nba.com/static/json/staticData/scheduleLeagueV2.json"

response = requests.get(url)

if response.status_code == 200:
    nba_schedule = response.json()
    schedule_map = {}
    
    for game_date in nba_schedule['leagueSchedule']['gameDates']:
        date = game_date['gameDate']
        games = game_date['games']
        
        teams_playing = []
        for game in games:
            home_team = game['homeTeam']['teamName']
            away_team = game['awayTeam']['teamName']
            teams_playing.append(f"{away_team} vs {home_team}")
        
        schedule_map[date] = teams_playing
    with open('nba_schedule_2024.json', 'w') as json_file:
        json.dump(schedule_map, json_file, indent=4)
    
    print("NBA schedule has been saved to nba_schedule_2024.json")
else:
    print(f"Failed to retrieve NBA schedule. Status code: {response.status_code}")
