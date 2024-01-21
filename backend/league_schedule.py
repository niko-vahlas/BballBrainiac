import pandas as pd
import datetime

class Schedule:
    """
    Class that represents a fantasy league shedule.
    """

    def __init__(self) -> None:
        """
        Read schedule and replaces date with date index (starts at 0).
        """
        self.df = pd.read_csv("2023_schedule.csv")
        self.df = self.df.sort_values(by='GameDate')

        l = sorted(list(set(self.df["GameDate"])))
        self.d = {date: index for index, date in enumerate(l)}
        
        indices = []
        for index, row in self.df.iterrows():
            # row.GameDate = self.d[row.GameDate]
            indices += [self.d[row.GameDate]]

        self.df.insert(0, "DateIndex", indices, True)
        # print(self.df)

    def get_days_played(self, team: str, n: int) -> list:
        """

        """
        date = str(datetime.datetime.now())[:10]
        # print(date)
        # date = "2024-01-02"
        team_games = self.df[self.df["Home"] == team]
        # print(list(team_games["GameDate"]))
        if date not in list(team_games["GameDate"]):
            date = str(datetime.datetime.now() + datetime.timedelta(days=1))[:10]
            counter = 2
            while date not in list(team_games["GameDate"]):
                date = str(datetime.datetime.now() + counter*datetime.timedelta(days=1))[:10]
                counter += 1

            team_games = team_games[team_games["DateIndex"] >= self.d[date]]
        else:
            team_games = team_games[team_games["DateIndex"] >= self.d[date]]

        return list(team_games["DateIndex"])[:n]



# df = pd.read_csv("2023_schedule.csv")

# df_date = df.sort_values(by='GameDate')

# l = sorted(list(set(df_date["GameDate"])))
# d = {date: index for index, date in enumerate(l)}

# for index, row in df_date.iterrows():
#     row.GameDate = d[row.GameDate]

# print(df_date)
            
s = Schedule()
print(s.get_days_played("TOR", 5))
