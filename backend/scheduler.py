from typing import Dict, List
from espn_api.basketball import Team
from espn_api.basketball import Player
from datetime import datetime
import json
from utils import generate_dates, get_players_playing

class Scheduler:
    """
    Class representing a scheduler
    Takes in a team, a number of days, a list of free agents, and return the best swaps to make
    """

    def __init__(self, team: Team, days: int, free_agents: List[Player]) -> None:
        self.team = team
        self.days = days
        self.free_agents = free_agents
        self.days = days
    
    def calculate_total_points_list(self, players: List[Player]) -> int:
        """
        Calculate how many points a list of players will have on average
        """
        with open('nba_schedule_2024.json', 'r') as json_file:
            schedule_map = json.load(json_file)
        dates = generate_dates(self.days)
        points = 0
        for date in dates:
            teams_playing = schedule_map[date]
            players_playing = get_players_playing(date, players, teams_playing)
            for player in players_playing:
                points+=player.avg_points

        return points

    def all_possible_teams(self) -> List[Dict[str, any]]:
        """
        Calculates all the different combinations of teams and single free agent swaps
        """
        possible_teams = [[]]
        current_team: List[Player] = self.team.roster
        current_free_agents: List[Player] = self.free_agents

        for i in range(len(current_team)):
            for j in range(len(current_free_agents)):
                new_team = current_team[:]
                new_team[i] = current_free_agents[j]
                possible_teams.append({
                    'new_team_points': self.calculate_total_points_list(new_team),
                    'swapped_in': current_free_agents[j],
                    'swapped_out': current_team[i]
                })

        return possible_teams
    
    
        

