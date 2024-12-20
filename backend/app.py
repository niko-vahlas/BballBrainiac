from typing import Dict, List
from flask import Flask, request, jsonify
from espn_api.basketball import League
from scheduler import Scheduler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    # fetch the current team using the league API,
    # get the list of free agents,
    # create a Scheduler instance to calculate possible swaps,
    # and sort the teams based on the total points to find the best swaps.
    null_fields = [key for key, value in data.items() if value is None]

    if null_fields:
        return jsonify({
            "error": "Null values found",
            "fields": null_fields
        }), 400

    n = 5
    team_name = data.get('teamName')
    days = int(data.get("days"))
    cur_league = League(
        league_id=data.get('LID'),
        year=int(data.get('YER')),
        espn_s2=data.get('ES2'),
        swid=data.get('SWD')
    )
    condition = lambda x: x.team_name == team_name
    current_team = next((team for team in cur_league.teams if condition(team)), None)
    if not current_team:
        return jsonify({
            "error": "Team name doesn't exist",
        }), 400
    current_free_agents = cur_league.free_agents()
    #pass in free agents to a class along with all neccessary info
    schedule = Scheduler(current_team, days, current_free_agents)
    best_teams: List[Dict[str, any]] = sorted(schedule.all_possible_teams(), key=lambda x: x['new_team_points'], reverse=True)


    top_n_teams = best_teams[:n]

    result = {"message": "Data received", "data": top_n_teams}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
