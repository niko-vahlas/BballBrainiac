from collections import defaultdict
from datetime import datetime, timedelta
from typing import List
from espn_api.basketball import Player

def generate_dates(n):
    """Generate a list of dates from now to n days into the future."""
    now = datetime.now()
    dates = [now + timedelta(days=i) for i in range(n + 1)]
    return dates

def get_players_playing(players: List[Player], teams_playing):
    """Schedule the players optimally and return those who are playing"""
    condition = lambda player: player.proTeam in teams_playing
    cur_players: List[Player] = filter(players, condition)
    selected_players = []
    player_used = set()

    # Define the team slots and their corresponding eligible positions
    team_slots = ["C", "PG", "SG", "SF", "PF", "F", "G"]

    # Eligible slot mapping considering G and F slots
    slot_mapping = {
        'C': ['C'],
        'PG': ['PG'],
        'SG': ['SG'],
        'SF': ['SF'],
        'PF': ['PF'],
        'G': ['PG', 'SG'],
        'F': ['SF', 'PF']
    }

    # Create a dictionary of slot to eligible players sorted by avg_points in descending order
    slot_candidates = defaultdict(list)
    for player in cur_players:
        for slot in player.eligibleSlots:
            slot_candidates[slot].append(player)

    for slot in slot_candidates:
        slot_candidates[slot].sort(key=lambda p: p.avg_points, reverse=True)

    # Assign players to slots
    for team_slot in team_slots:
        eligibleSlots = slot_mapping[team_slot]
        for eligible_slot in eligibleSlots:
            candidates = slot_candidates.get(eligible_slot, [])
            for candidate in candidates:
                if candidate.name not in player_used:
                    selected_players.append(candidate)
                    player_used.add(candidate.name)
                    break
            if any(player.name in player_used for player in selected_players):
                break

    return selected_players