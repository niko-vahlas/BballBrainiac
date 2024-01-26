from espn_api.basketball import League

class Team:
    """
    Class representing a possible fantasy team
    Pass in a player, list of current players, 
    """

    def __init__(self, players_on_team: list, free_agent: object) -> None:
        """
        players_on_team is a list of player objects.
        """
        self.team = players_on_team
        self.free_agent = free_agent
        self.max_points = None
        self.player_to_swap = None


    def calculate_max_points(self) -> None:
        """
        Sets the best team swap to maximize the number of points and sets the max_points parameter and who we should swap for the free agent
        """
        player_points_map = {p: p.total_points for p in self.team}

        # get the player with the minimum points on the initial team
        min_points_player = min(player_points_map, key=player_points_map.get)

        if (self.free_agent.total_points > player_points_map[min_points_player]): # if free agent has more points than lowest player on team
            self.max_points = self.__sum_team_points() - min_points_player + self.free_agent.total_points
            self.player_to_swap = min_points_player
        else:
            self.max_points = self.__sum_team_points()

    
    def calculate_max_points_for_variation(self) -> list:
        """
        Returns the number of points that team varitation will get if they get their average points
        Calculate ideal schedule
        """
        if (self.player_to_swap == None):
            print("Error: player_to_swap is None\nProgram Stopped")
            return
        
        s = Schedule()
        # for each player calculates avg_points times number of games for their time
        average_points = map(lambda x: len(s.get_days_played(x.proTeam, days)*x.avg_points, self.team))

        return sum(average_points)
    
    def calculate_ideal_schedule_total_days(self) -> int:
        """
        Return the number of points that team should get over the given period
        """
        # for players in self.players_on_team:

        return 0

    def calculate_ideal_schedule_day(self) -> int:
        """
        Given the players who are playing that day and their average points and the positions they can play
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

    def __sum_team_points(self) -> int:
        """
        Returns total points from each player on team.
        """
        points = map(lambda x: x.total_points, self.team)
        return sum(points)
