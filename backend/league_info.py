from espn_api.basketball import League

class FBL:
    """
    Class representing a fantasy basketball league.
    """

    def __init__(self, league_id: int, year: int, s2: str, id: str) -> None:
        self.league = League(league_id, year, s2, id)

    def get_free_players(self, n: int) -> list:
        """
        Returns the top n 
        """
        return self.league.free_agents(n)
    
    def get_player_points(player: object) -> int:
        """
        Takes a player object as an argument and returns their fantasy points.
        """
        return player.total_points()
    
    def get_schedule(team: object) -> list:
        """
        Takes a team object as an argument and returns their schedule.
        """
        



