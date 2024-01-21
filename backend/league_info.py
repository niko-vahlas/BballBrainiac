from espn_api.basketball import League
import helper

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
        



# s2 = "AEBAJxdxP5I6JqBI8BkCNUC37xDPMxVuJz7wRG7CKm%2FoPSQVaMctW6r%2FQUGJHrSNM7I4CpyMUFW6BUQ%2FJjcmtBqmlkJLWBhfWHKYVRK59T2ZeWfXPjYB6sL31lsVBHHoGX00fpAdmqjBCtfIKFcjgIjNSxqrQLIJYJrxTZX46oxXk%2BVntCasJHvYetVfopOGuHfOPBoMF4jkHFle9KXwHsOOo8Mfa0%2F6%2FajTUKnUG2iZZCSHgieAvDVkJoX%2B2tqR9%2BxqANWpzDIlWOhGR7JIrXhIR%2BC5WH6zKEz06TobWR7bUg%3D%3D"
# id = "{4884AC59-8D81-48FA-A56F-323FCBF78DE4}"

# league = FBL(league_id=1944084794, year=2024, espn_s2=s2, swid=id)
# t = league.teams[5]

# print("Hello world")
# print(t.roster)


