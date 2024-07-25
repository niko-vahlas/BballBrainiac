from typing import Dict, List
from flask import Flask, request, jsonify
from espn_api.basketball import League
from scheduler import Scheduler

app = Flask(__name__)

@app.route('/process_data', methods=['GET'])
def process_data():
    data = request.json
    # Process your data here. For example:
    # get the data from the request
    # call the espn api
    #iterate over every free agent, make a new team object and keep track of the top teams with a max heap
    #return the top 5 players with who to swap and how much of an inecrease that is
    null_fields = [key for key, value in data.items() if value is None]
    n = 5
    team_name = 'Niko Team'
    days=10

    if null_fields:
        return jsonify({
            "error": "Null values found",
            "fields": null_fields
        }), 400
    
    cur_league = League(
        league_id=data.get('LID'),
        year=data.get('YER'),
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
