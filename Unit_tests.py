import io
import sys
import Basketball_predictions

def celtics_test():
    celtics = Basketball_predictions.Team("Celtics","CelticsData.csv")
    assert celtics.__repr__() == (f"Team: Celtics, PTS=116.50000000000001\n"
            f"REB=50.4\n"
            f"AST=23.8, STL=8.3, BLK=5.5\n"
            f"TO=96.0, PF=152.0\n")
    assert celtics.playersDict["J. Brown"].__repr__() == (
            f"Player: J. Brown, GP=8, PTS=22.1\n"
            f"REB=7.1\n"
            f"AST=2.9, STL=1.1, BLK=0.3\n"
            f"TO=26.0, PF=22.0\n"
        )
    assert celtics.playersDict["J. Tatum"].__repr__() == (
            f"Player: J. Tatum, GP=7, PTS=26.1\n"
            f"REB=12.0\n"
            f"AST=5.6, STL=1.9, BLK=0.6\n"
            f"TO=22.0, PF=18.0\n"
        )
    assert celtics.playersDict["N. Queta"].__repr__() == (
            f"Player: N. Queta, GP=2, PTS=2.0\n"
            f"REB=0.0\n"
            f"AST=0.5, STL=0.0, BLK=0.0\n"
            f"TO=0.0, PF=0.0\n"
        )
def trade_calc_test_1():
    """Trade Calc tests"""
    Celtics = Basketball_predictions.Team("Celtics","CelticsData.csv")
    Warriors = Basketball_predictions.Team("Warriors","WarriorsData.csv")
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    Basketball_predictions.trade_calc(Celtics, ["J. Brown"], Warriors, ["D. Green","G. Payton II"])
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == ("Celtics's pts would decrease by 7.12% from this trade\n"
    "Celtics's rb would increase by 0.99% from this trade\n"
    "Celtics's ast would increase by 10.5% from this trade\n"
    "Celtics's blk would increase by 14.55% from this trade\n"
    "Celtics's to would increase by 9.38% from this trade\n"
    "Celtics's pf would increase by 21.05% from this trade\n"
    "Warriors's pts would increase by 6.88% from this trade\n"
    "Warriors's rb would decrease by 1.05% from this trade\n"
    "Warriors's ast would decrease by 9.09% from this trade\n"
    "Warriors's blk would decrease by 14.29% from this trade\n"
    "Warriors's to would decrease by 7.26% from this trade\n"
    "Warriors's pf would decrease by 15.38% from this trade\n"
    "Overall the Celtics would become worse from this trade while the Warriors would become better from this trade\n"
    )
def trade_calc_test_2():
    """Reverse of previous"""
    Celtics = Basketball_predictions.Team("Celtics","CelticsData.csv")
    Warriors = Basketball_predictions.Team("Warriors","WarriorsData.csv")
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    Basketball_predictions.trade_calc(Warriors, ["D. Green","G. Payton II"], Celtics, ["J. Brown"])
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == ("Warriors's pts would increase by 6.88% from this trade\n"
    "Warriors's rb would decrease by 1.05% from this trade\n"
    "Warriors's ast would decrease by 9.09% from this trade\n"
    "Warriors's blk would decrease by 14.29% from this trade\n"
    "Warriors's to would decrease by 7.26% from this trade\n"
    "Warriors's pf would decrease by 15.38% from this trade\n"
    "Celtics's pts would decrease by 7.12% from this trade\n"
    "Celtics's rb would increase by 0.99% from this trade\n"
    "Celtics's ast would increase by 10.5% from this trade\n"
    "Celtics's blk would increase by 14.55% from this trade\n"
    "Celtics's to would increase by 9.38% from this trade\n"
    "Celtics's pf would increase by 21.05% from this trade\n"
    "Overall the Warriors would become better from this trade while the Celtics would become worse from this trade\n"
    )
def trade_calc_test_3():
    """Reverse of previous"""
    Knicks = Basketball_predictions.Team("Knicks","NewYorkKnicksData.csv")
    Warriors = Basketball_predictions.Team("Warriors","WarriorsData.csv")
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    Basketball_predictions.trade_calc(Warriors, ["K. Looney"], Knicks, ["J. Brunson"])
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == ("Warriors's pts would increase by 22.89% from this trade\n"
    "Warriors's rb would increase by 1.46% from this trade\n"
    "Warriors's ast would increase by 26.55% from this trade\n"
    "Warriors's blk would increase by 0.0% from this trade\n"
    "Warriors's to would increase by 16.13% from this trade\n"
    "Warriors's pf would increase by 0.48% from this trade\n"
    "Knicks's pts would decrease by 25.96% from this trade\n"
    "Knicks's rb would decrease by 1.6% from this trade\n"
    "Knicks's ast would decrease by 37.24% from this trade\n"
    "Knicks's blk would increase by 0.0% from this trade\n"
    "Knicks's to would decrease by 20.41% from this trade\n"
    "Knicks's pf would decrease by 0.6% from this trade\n"
    "Overall the Warriors would become better from this trade while the Knicks would become worse from this trade\n"
    )


def test_add_player():
    team = Basketball_predictions.Team("TestTeam", "TestTeam.csv")
    team.playersDict.clear()
    result = team.add_player("Test Player", 10, 20.0, 5.0, 4.0, 1.0, 0.5, 2.0, 1.0)
    assert "Test Player" in team.playersDict
    assert result == "Test Player added to TestTeam."

def test_remove_player():
    team = Basketball_predictions.Team("TestTeam", "TestTeam.csv")
    team.playersDict.clear()
    team.add_player("Remove Me", 5, 10.0, 4.0, 2.0, 0.5, 0.2, 1.0, 1.0)
    result = team.remove_player("Remove Me")
    assert "Remove Me" not in team.playersDict
    assert result == "Remove Me removed from TestTeam."

def test_update_player_stats():
    team = Basketball_predictions.Team("TestTeam", "TestTeam.csv")
    team.playersDict.clear()
    team.add_player("Update Guy", 5, 10.0, 4.0, 2.0, 1.0, 0.5, 1.0, 1.0)
    result = team.update_player_stats("Update Guy", pts=30.5, ast=6.5)
    player = team.playersDict["Update Guy"]
    assert player.pts == 30.5
    assert player.ast == 6.5
    assert result == "Update Guy's stats have been updated on TestTeam."

def test_trade_player():
    team_from = Basketball_predictions.Team("TeamA", "TestTeam.csv")
    team_to = Basketball_predictions.Team("TeamB", "TestTeam.csv")
    team_from.playersDict.clear()
    team_to.playersDict.clear()
    team_from.add_player("One Way", 5, 10.0, 3.0, 2.0, 1.0, 0.5, 1.0, 1.0)
    result = Basketball_predictions.trade_player(team_from, team_to, "One Way")
    assert "One Way" in team_to.playersDict
    assert "One Way" not in team_from.playersDict
    assert result == "One Way has been traded from TeamA to TeamB."

def test_trade_players():
    team_a = Basketball_predictions.Team("TeamA", "TestTeam.csv")
    team_b = Basketball_predictions.Team("TeamB", "TestTeam.csv")
    team_a.playersDict.clear()
    team_b.playersDict.clear()
    team_a.add_player("Alpha", 5, 15.0, 6.0, 4.0, 1.2, 0.8, 1.0, 2.0)
    team_b.add_player("Beta", 5, 12.0, 5.0, 3.0, 1.0, 0.6, 2.0, 1.0)
    result = Basketball_predictions.trade_players(team_a, "Alpha", team_b, "Beta")
    assert "Alpha" in team_b.playersDict
    assert "Beta" in team_a.playersDict
    assert result == "Alpha has been traded from TeamA to TeamB, and Beta has been traded from TeamB to TeamA."

def test_calculate_per():
    player = Basketball_predictions.Player("Test Player", 10, 200, 70, 50, 20, 10, 30, 25)
    per = Basketball_predictions.PlayerEfficiency.calculate_per(player)
    positive = (200 * 0.85 + 70 * 0.7 + 50 * 0.7 + 20 * 1.2 + 10 * 0.9)
    negative = (30/10 * 0.9 + 25/10 * 0.45)
    expected_per = round(positive - negative, 1)
    assert per == expected_per

def test_get_team_pers():
    team = Basketball_predictions.Team("TestTeam", "TestTeam.csv")
    team.playersDict.clear()
    team.add_player("Player1", 10, 200, 70, 50, 20, 10, 30, 25)
    team.add_player("Player2", 10, 180, 50, 40, 15, 8, 20, 18)
    pers = Basketball_predictions.PlayerEfficiency.get_team_pers(team)
    per_values = list(pers.values())
    assert per_values == sorted(per_values, reverse=True)

def test_show_team_rankings():
    Basketball_predictions.teamsDict = {}
    team1 = Basketball_predictions.Team("Team1", "TestTeam.csv")
    team1.playersDict.clear()
    team1.add_player("Player1", 10, 200, 70, 50, 20, 10, 30, 25)
    team2 = Basketball_predictions.Team("Team2", "TestTeam.csv")
    team2.playersDict.clear()
    team2.add_player("Player3", 10, 160, 60, 30, 10, 6, 25, 20)
    Basketball_predictions.teamsDict["Team1"] = team1
    Basketball_predictions.teamsDict["Team2"] = team2
    Basketball_predictions.show_team_rankings_and_prediction()
    assert "Team1" in Basketball_predictions.teamsDict
    assert "Team2" in Basketball_predictions.teamsDict
    
if __name__ =="__main__":
    celtics_test()
    trade_calc_test_1()
    trade_calc_test_2()
    trade_calc_test_3()
    test_add_player()
    test_remove_player()
    test_update_player_stats()
    test_trade_player()
    test_trade_players()
    test_calculate_per()
    test_get_team_pers()
    test_show_team_rankings()