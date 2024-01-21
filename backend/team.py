from espn_api.basketball import League

class Team:
    """
    Class representing a possible fantasy team
    Pass in a player, list of current players, 

    """

    def __init__(self, players_on_team: list, free_agent: object, max_points: 0, player_to_swap: object) -> None:
        self.team = Team(players_on_team, free_agent, max_points, None)


    def calculate_max_points(self) -> None:
        """
        Sets the best team swap to maximize the number of points and sets the max_points parameter and who we should swap for the free agent
        """
    
    def calculate_max_points_for_variation(self) -> list:
        """
        Returns the number of points that team varitation will get if they get their average points
        Calculate ideal schedule
        """
        return self.league.free_agents(n)
    
    def calculate_ideal_schedule_total_days(self) -> int:
        """
        Return the number of points that team should get over the given period
        """
        ()
        for players in self.players_on_team:

        return 

    def calculate_ideal_schedule_day(self) -> int:
        """
        Given the players who are playing that day and their average points and the positio ns they can play
        Return the number of points that team should get in a day using the ideal schedule
        Players are in use once their positions are empty
        """
        players = [("Zion", ["PF"], 50), ("Lebron", ["PF", "C"]), 40]
        positions = [["PG"], ["SG"], ["SF"], ["PF"], ["C"], ["PG", "SG"], ["SF", "PF"]]
        points = 0

        for multiposition in positions:
            foundplayer=False
            for position in multiposition and foundplayer is False:
                for player in players:
                    if player(1) is not False:
                        for player_position in player(1):
                            if player_position == position:
                                points = player(2) + points
                                player(1).clear()

   








    
        



