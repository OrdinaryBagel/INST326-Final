import pandas as pd
import csv
import random

teamsDict = {}

class Team:
    def __init__(self,name, csv):
        """
        Driver: Thomas, Peter
        Navigator: Khalid
        initalizes team objects using pandas and a csv containg team stats
        (the csv must be formatted like the one in our github)
        the variables represent:
        name = name
        gp = games played
        pts = points
        rb = rebounds
        ast = assists
        stl = steals
        blk = blocks
        to = turn overs
        pf = fouls"""
        self.name = name
        self.pts = 0
        self.rb = 0
        self.ast = 0
        self.stl = 0
        self.blk = 0
        self.to = 0
        self.pf = 0
        self.playersDict = {}
        teamData = pd.read_csv(csv)
        for i in range(0,len(teamData.index)):
            p_name = teamData["Player"][i]
            p_gp = teamData["GP"][i]
            p_rb = teamData["Reb/G"][i]
            p_ast = teamData["APG"][i]
            p_stl = teamData["SPG"][i]
            p_blk = teamData["BPG"][i]
            p_to = teamData["TO"][i]
            p_pf = teamData["PF"][i]
            p_pts = teamData["PPG"][i]
            self.playersDict[p_name] = Player(p_name, p_gp, p_pts, p_rb, p_ast, p_stl, p_blk, p_to, p_pf)
        self.calc_team_total()
    def add_player(self, name, gp, pts, rb, ast, stl, blk, to, pf):
        """
        Driver: Zayan
        Navigator: Thomas
        Adds a new player to the team.
        """
        if name in self.playersDict:
            return f"{name} is already on the team."
        self.playersDict[name] = Player(name, float(gp), float(pts), float(rb), float(ast), float(stl), float(blk), float(to), float(pf))
        self.calc_team_total()
        return f"{name} added to {self.name}."


    def remove_player(self,name):
        """
        Driver: Zayan
        Navigator: Khalid
        Removes a player from the team.
        """
        if name in self.playersDict:
            del self.playersDict[name]
            self.calc_team_total()
            return f"{name} removed from {self.name}."
        else: 
            return f"{name} is not on the team."   
        
    def update_player_stats(self, name, gp=None, pts=None, rb=None, ast=None, stl=None, blk=None, to=None, pf=None):
        """
        Driver: Zayan
        Navigator: Thomas
        Updates the stats of an existing player on the team.
        Only updates stats that are provided.
        """
        if name not in self.playersDict:
            return f"{name} is not on the team."

        player = self.playersDict[name]

        if gp is not None: 
            player.gp = float(gp)
        if pts is not None: 
            player.pts = float(pts)
        if rb is not None: 
            player.rb = float(rb)
        if ast is not None: 
            player.ast = float(ast)
        if stl is not None: 
            player.stl = float(stl)
        if blk is not None: 
            player.blk = float(blk)
        if to is not None: 
            player.to = float(to)
        if pf is not None: 
            player.pf = float(pf)

        self.calc_team_total()
        return f"{name}'s stats have been updated on {self.name}."

    def calc_team_total(self):
        """
        Driver: Thomas
        Navigator: Peter
        Calculates the total of the players stats to get the team stats
        """
        for key in self.playersDict:
            self.pts += self.playersDict[key].pts
            self.rb += self.playersDict[key].rb
            self.ast += self.playersDict[key].ast
            self.stl += self.playersDict[key].stl
            self.blk += self.playersDict[key].blk
            self.to += self.playersDict[key].to
            self.pf += self.playersDict[key].pf
    def print_player(self,name):
        if name in self.playersDict:
            print(self.playersDict[name])
        else:
            print(f"Player named {name} is not on this team.")
    def update(self):
        """
        Should be able to call other methods that add players, remove players, update a players stats, and trade players.
        After any of these are done the total stats should be updated to reflect it.
        """
    def save_to_csv(self, filename):
        """
        driver: Khalid Goshu
        Navigator: Zayan
        saves this team's player data to a CSV file
        """
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Player', 'GP', 'PPG', 'Reb/G', 'APG', 'SPG', 'BPG', 'TO', 'PF'])
            for player in self.playersDict.values():
                writer.writerow([
                    player.name,
                    player.gp,
                    player.pts,
                    player.rb,
                    player.ast,
                    player.stl,
                    player.blk,
                    player.to,
                    player.pf
                ])
    def __repr__(self):
        return (
            f"Team: {self.name}, PTS={self.pts}\n"
            f"REB={self.rb}\n"
            f"AST={self.ast}, STL={self.stl}, BLK={self.blk}\n"
            f"TO={self.to}, PF={self.pf}\n"
        )

class Player:
    def __init__(self, name, gp, pts, rb, ast, stl, blk, to, pf):
        """
        initializes the player object
        """
        self.name = name
        self.gp = gp
        self.pts = pts
        self.rb = rb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.to = to
        self.pf = pf
    def __repr__(self):
        return (
            f"Player: {self.name}, GP={self.gp}, PTS={self.pts}\n"
            f"REB={self.rb}\n"
            f"AST={self.ast}, STL={self.stl}, BLK={self.blk}\n"
            f"TO={self.to}, PF={self.pf}\n"
        )
    
class PlayerEfficiency:
    """
    Driver: Peter
    Navigator: Zayan
    Calculates Player Efficiency with different measures
    """

    def calculate_per(player, team_pace=100):
        """Calculates the PER Player Efficiency Rating for a player."""

        if player.gp == 0:
            return 0.0
        
        gp = player.gp
        pts = player.pts
        reb = player.rb
        ast = player.ast
        stl = player.stl
        blk = player.blk
        to = player.to
        pf = player.pf

        # Calculate the individual PER Adds positive stats and subtracts negative states 
        # Multiplies by a number that indicates weight of the stat - team pace set to 100 and a conditional is setup incase we decide to be more accurate
        positive = (pts * 0.85 + reb * 0.7 + ast * 0.7 + stl * 1.2 + blk * 0.9)
        negative = (to/gp * 0.9 + pf/gp * 0.45)                       
        
        raw_per = positive - negative
        if team_pace != 100:
            per = raw_per * (100 / team_pace)
        else:
            per = raw_per         
                   
        return round(per, 1)

    def get_team_pers(team, team_pace=100):
        """ 
        Driver: Peter
        Navigator: Zayan
        Calculate PER for all players on a team
        Returns:
            dict: Dictionary with player names as keys and PER values as values
        """
        pers = {}
        for player_name, player in team.playersDict.items():
            pers[player_name] = PlayerEfficiency.calculate_per(player, team_pace)
        
        return dict(sorted(pers.items(), key=lambda x: x[1], reverse=True))

def show_team_rankings_and_prediction():
    """
    Driver: Peter
    Navigator: Khalid
    Displays team PER rankings and predicts a winner between teams.
    """
    if not teamsDict:
        print("No teams have been entered.")
        return

    team_averages = {}
    for team_name, team in teamsDict.items():
        pers = PlayerEfficiency.get_team_pers(team)
        if pers:
            avg_per = sum(pers.values()) / len(pers)
        else:
            avg_per = 0.0
        team_averages[team_name] = round(avg_per, 2)

    sorted_teams = sorted(team_averages.items(), key=lambda x: x[1], reverse=True)

    print("\nTeam PER Rankings: ")
    for rank, (team, avg_per) in enumerate(sorted_teams, start=1):
        print(f"{rank}. {team} - Avg PER: {avg_per}")

    if len(sorted_teams) >= 2:
        top_team = sorted_teams[0][0]
        runner_up = sorted_teams[1][0]
        print(f"\nPrediction: {top_team} is more likely to win based on a higher average PER compared to {runner_up}.")
    elif len(sorted_teams) == 1:
        print(f"\nOnly one team entered. {sorted_teams[0][0]} is currently unopposed.")

def trade_player(team_from, team_to, player_name):
    """
    Driver: Zayan
    Navigator: Thomas
    Trades a player from one team to another.
    This is a 1 way trade if the user wishes to move one player from a team to another.

    Args:
        team_from (Team): The team the player is currently on.
        team_to (Team): The team the player is going to.
        player_name (str): Name of the player being traded.
    
    Returns:
        str: Message indicating the result of the trade.
    """
    if player_name not in team_from.playersDict:
        return f"{player_name} is not on {team_from.name}."

    if player_name in team_to.playersDict:
        return f"{player_name} is already on {team_to.name}."

    player = team_from.playersDict[player_name]
    team_to.playersDict[player_name] = player
    del team_from.playersDict[player_name]

    team_from.calc_team_total()
    team_to.calc_team_total()

    return f"{player_name} has been traded from {team_from.name} to {team_to.name}."

def trade_players(team_a, player_a_name, team_b, player_b_name):
    """
    Driver: Zayan
    Navigator: Peter
    Trades player_a from team_a with player_b from team_b.
    This is a 2 way trade if the user wishes to trade 2 players between 2 teams.

    Args:
        team_a(Team): The first team involved in the trade.
        player_a_name(str): The name of the player from team A.
        team_b (Team): The second team involved in the trade.
        player_b_name (str): Name of the player from team B.
    
    Returns:
        str: Message indicating the result of the trade.
    """
    
    if player_a_name not in team_a.playersDict:
        return f"{player_a_name} is not on {team_a.name}."
    if player_b_name not in team_b.playersDict:
        return f"{player_b_name} is not on {team_b.name}."
    
    player_a = team_a.playersDict[player_a_name]
    player_b = team_b.playersDict[player_b_name]
    
    team_a.playersDict[player_b_name] = player_b
    team_b.playersDict[player_a_name] = player_a
    
    del team_a.playersDict[player_a_name]
    del team_b.playersDict[player_b_name]
    
    team_a.calc_team_total()
    team_b.calc_team_total()
    
    return (f"{player_a_name} has been traded from {team_a.name} to {team_b.name}, "
            f"and {player_b_name} has been traded from {team_b.name} to {team_a.name}.")

def convert_input(x):
    """
    Converts input to float if not blank.
    Returns None if the input is empty or only whitespace.
    """
    return float(x) if x.strip() else None

def trade_calc(team_a,players_a,team_b,players_b):
    """
    Driver: Thomas
    Navigator: Peter
    Calculates what team would lose and/or gain from a trade
    supports multiple player trades
    Returns nothing and prints the results of the tests
    """
    a_stats= {"pts": team_a.pts, "rb": team_a.rb, "ast": team_a.ast, "blk": team_a.blk, "to": team_a.to, "pf": team_a.pf}
    b_stats= {"pts": team_b.pts, "rb": team_b.rb, "ast": team_b.ast, "blk": team_b.blk, "to": team_b.to, "pf": team_b.pf}

    a_stats_d= {"pts": team_a.pts, "rb": team_a.rb, "ast": team_a.ast, "blk": team_a.blk, "to": team_a.to, "pf": team_a.pf}
    b_stats_d= {"pts": team_b.pts, "rb": team_b.rb, "ast": team_b.ast, "blk": team_b.blk, "to": team_b.to, "pf": team_b.pf}
    """calculates the stats changes that would come from the trade"""
    for i in players_a:
        a_stats["pts"]=a_stats["pts"] - team_a.playersDict[i].pts
        a_stats["rb"]=a_stats["rb"] - team_a.playersDict[i].rb
        a_stats["ast"]=a_stats["ast"] - team_a.playersDict[i].ast
        a_stats["blk"]=a_stats["blk"] - team_a.playersDict[i].blk
        a_stats["to"]=a_stats["to"] - team_a.playersDict[i].to
        a_stats["pf"]=a_stats["pf"] - team_a.playersDict[i].pf
        b_stats["pts"]=b_stats["pts"] + team_a.playersDict[i].pts
        b_stats["rb"]=b_stats["rb"] + team_a.playersDict[i].rb
        b_stats["ast"]=b_stats["ast"] + team_a.playersDict[i].ast
        b_stats["blk"]=b_stats["blk"] + team_a.playersDict[i].blk
        b_stats["to"]=b_stats["to"] + team_a.playersDict[i].to
        b_stats["pf"]=b_stats["pf"] + team_a.playersDict[i].pf
    for i in players_b:
        a_stats["pts"]=a_stats["pts"] + team_b.playersDict[i].pts
        a_stats["rb"]=a_stats["rb"] + team_b.playersDict[i].rb
        a_stats["ast"]=a_stats["ast"] + team_b.playersDict[i].ast
        a_stats["blk"]=a_stats["blk"] + team_b.playersDict[i].blk
        a_stats["to"]=a_stats["to"] + team_b.playersDict[i].to
        a_stats["pf"]=a_stats["pf"] + team_b.playersDict[i].pf
        b_stats["pts"]=b_stats["pts"] - team_b.playersDict[i].pts
        b_stats["rb"]=b_stats["rb"] - team_b.playersDict[i].rb
        b_stats["ast"]=b_stats["ast"] - team_b.playersDict[i].ast
        b_stats["blk"]=b_stats["blk"] - team_b.playersDict[i].blk
        b_stats["to"]=b_stats["to"] - team_b.playersDict[i].to
        b_stats["pf"]=b_stats["pf"] - team_b.playersDict[i].pf
    """Calculates how much each stat changed percentage-wise to determine how much the team gained/loss
    percentages will be added/subtracted to/from a total to determine if a team gained/lost overall
    will also display the percent chnages in stats
    """
    temp = 0.0
    a_change = 0.0
    b_change = 0.0
    for key in a_stats:
        temp = (a_stats[key]-a_stats_d[key])/a_stats_d[key]
        if key == "pf" or key =="to":
            a_change = a_change - temp
        else:
            a_change +=temp
        if temp<0:
            print(f"{team_a.name}'s {key} would decrease by {round(temp*100*(-1),2)}% from this trade")
        else:
            print(f"{team_a.name}'s {key} would increase by {round(temp*100,2)}% from this trade")
    for key in b_stats:
        temp = (b_stats[key]-b_stats_d[key])/b_stats_d[key]
        if key == "pf" or key =="to":
            b_change = b_change - temp
        else:
            b_change +=temp
        if temp<0:
            print(f"{team_b.name}'s {key} would decrease by {round(temp*100*(-1),2)}% from this trade")
        else:
            print(f"{team_b.name}'s {key} would increase by {round(temp*100,2)}% from this trade")
    if(a_change<0):
        s1 = f"Overall the {team_a.name} would become worse from this trade"
    elif(a_change>0):
        s1 = f"Overall the {team_a.name} would become better from this trade"
    else:
        s1 = f"Overall the {team_a.name} wouldn't become better or worse from this trade"
    if(b_change<0):
        s2 = f"while the {team_b.name} would become worse from this trade"
    elif(b_change>0):
        s2 = f"while the {team_b.name} would become better from this trade"
    else:
        s2 = f"while the {team_a.name} wouldn't become better or worse from this trade"
    print(f"{s1} {s2}")

def get_stat_leaders(stat, top_n=5):
    """
    driver: khalid goshu
    navigator: zayan
    Shows top N players across all teams for a given stat (such as points rebounds etc).
    """
    leaders = []
    for team in teamsDict.values():
        for player in team.playersDict.values():
            value = getattr(player, stat, None)
            if value is not None:
                leaders.append((player.name, team.name, value))

    leaders.sort(key=lambda x: x[2], reverse=True)
    return leaders[:top_n]

def get_top_players(team, n=3, by="PPG"):
    """
    driver: khalid goshu
    Returns the top N players on a team by PPG or PER
    """
    if by.lower() == "per":
        stats = {
            name: PlayerEfficiency.calculate_per(player)
            for name, player in team.playersDict.items()
        }
    else:
        stats = {
            name: player.pts for name, player in team.playersDict.items()
        }

    sorted_players = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    return sorted_players[:n]


def simulate_game(team_a, team_b):
    """
    driver: khalid goshu
    navigator: thomas minnihan
    Simulates a game between two teams using their average PER and adds randomness to make the games more realistic because of the nature of sports
    """
    total_per_a = 0
    total_per_b = 0

    for player_name in team_a.playersDict:
        player = team_a.playersDict[player_name]
        total_per_a += PlayerEfficiency.calculate_per(player)
    avg_per_a = total_per_a / len(team_a.playersDict) if team_a.playersDict else 0

    for player_name in team_b.playersDict:
        player = team_b.playersDict[player_name]
        total_per_b += PlayerEfficiency.calculate_per(player)
    avg_per_b = total_per_b / len(team_b.playersDict) if team_b.playersDict else 0

    noise_a = random.uniform(-3, 3)
    noise_b = random.uniform(-3, 3)

    score_a = avg_per_a + noise_a
    score_b = avg_per_b + noise_b

    if avg_per_a > avg_per_b:
        score_b += random.uniform(0, 2)
    elif avg_per_b > avg_per_a:
        score_a += random.uniform(0, 2)

    print(f"\nSimulating Game: {team_a.name} vs {team_b.name}")
    print(f"{team_a.name} Score: {round(score_a, 2)}")
    print(f"{team_b.name} Score: {round(score_b, 2)}")

    if score_a > score_b:
        print(f"{team_a.name} wins!")
    elif score_b > score_a:
        print(f"{team_b.name} wins!")
    else:
        print("It's a tie!")
        
def load_team_from_csv(name, filename):
    """
    Loads a team from a csv file and returns a team object
    """
    try:
        return Team(name, filename)
    except Exception as e:
        print(f"Error loading team from {filename}: {e}")
        return None


def functions(func):
    """determines what the program will do, will be update by multiple people as the project moves forward."""
    if func == 1:
        """creates new teams"""
        name = input("Please enter the name of the team: ")
        csv = input("Please enter the CSV file containg the teams information: ")
        teamsDict[name] = Team(name,csv)
    elif func == 2:
        name = input("Please enter the name of the team: ")
        if name in teamsDict:
            print(teamsDict[name])
        else:
            print(f"{name} does not exist")
    elif func == 3:
        name = input("Please enter the name of the team: ")
        if name in teamsDict:
            p_name = input("Please enter the name of the player: ")
            teamsDict[name].print_player(p_name)
        else:
            print(f"{name} does not exist")

    elif func == 4:
        team_name = input("Enter the name of the team: ")
        if team_name in teamsDict:
            name = input("Player name: ")
            gp = input("Games played: ")
            pts = input("PPG: ")
            rb = input("Rebounds per game: ")
            ast = input("Assists per game: ")
            stl = input("Steals per game: ")
            blk = input("Blocks per game: ")
            to = input("Turnovers: ")
            pf = input("Personal fouls: ")
            msg = teamsDict[team_name].add_player(name, gp, pts, rb, ast, stl, blk, to, pf)
            print(msg)
        else:
            print(f"{team_name} does not exist.")

    elif func == 5:
        team_name = input("Enter the name of the team: ")
        if team_name in teamsDict:
            name = input("Enter the name of the player to remove: ")
            msg = teamsDict[team_name].remove_player(name)
            print(msg)
        else:
            print(f"{team_name} does not exist.")

    elif func == 6:
        team_name = input("Enter the name of the team: ")
        if team_name in teamsDict:
            name = input("Enter the name of the player to update: ")
            print("Press Enter to skip any stat you don't want to update.")
        
            gp = input("New games played (or leave blank): ")
            pts = input("New PPG (or leave blank): ")
            rb = input("New RPG (or leave blank): ")
            ast = input("New APG (or leave blank): ")
            stl = input("New SPG (or leave blank): ")
            blk = input("New BPG (or leave blank): ")
            to = input("New TO (or leave blank): ")
            pf = input("New PF (or leave blank): ")

            msg = teamsDict[team_name].update_player_stats(
                name,
                gp=convert_input(gp),
                pts=convert_input(pts),
                rb=convert_input(rb),
                ast=convert_input(ast),
                stl=convert_input(stl),
                blk=convert_input(blk),
                to=convert_input(to),
                pf=convert_input(pf)
            )
            print(msg)
        else:
            print(f"{team_name} does not exist.")
    elif func == 7:
        from_team = input("Enter the name of the team trading the player: ")
        to_team = input("Enter the name of the team receiving the player: ")
        player_name = input("Enter the name of the player to trade: ")

        if from_team in teamsDict and to_team in teamsDict:
            msg = trade_player(teamsDict[from_team], teamsDict[to_team], player_name)
            print(msg)
        else:
            print("One or both teams not found.")

    elif func == 8:
        team_a = input("Enter the first team name: ")
        player_a = input("Enter the player from the first team: ")
        team_b = input("Enter the second team name: ")
        player_b = input("Enter the player from the second team: ")

        if team_a in teamsDict and team_b in teamsDict:
            msg = trade_players(teamsDict[team_a], player_a, teamsDict[team_b], player_b)
            print(msg)
        else:
            print("One or both teams not found.")

    elif func == 9:
        team_name = input("Please enter the name of the team: ")
        if team_name in teamsDict:
            player_name = input("Enter player name (or 'all' for team rankings): ")
            team = teamsDict[team_name]
            if player_name.lower() == "all":
                # Show PER for entire team
                team_pers = PlayerEfficiency.get_team_pers(team)
                print(f"\n{team_name} PER Rankings:")
                for name, per in team_pers.items():
                    print(f"{name}: {per}")
            elif player_name in team.playersDict:
                # Show individual player PER
                player = team.playersDict[player_name]
                print(f"{player_name}'s PER: {PlayerEfficiency.calculate_per(player)}")
            else:
                print(f"{player_name} is not on this team.")
        else:
            print(f"{team_name} does not exist")
    elif func == 10:
        show_team_rankings_and_prediction()
    elif func == 11:
        temp = 1
        players_a = []
        players_b = []
        team_a = input("Please enter the first team's name: ")
        team_b = input("Please enter the second team's name: ")
        while temp !="exit":
            temp = input(f"Please enter the name of a player from {team_a}(\"exit\" to stop): ")
            if(temp!=0 and temp in teamsDict[team_a].playersDict):
                players_a.append(temp)
        temp = 1
        while temp !="exit":
            temp = input(f"Please enter the name of a player from {team_b}(\"exit\" to stop): ")
            if(temp!=0 and temp in teamsDict[team_b].playersDict):
                players_b.append(temp)
        trade_calc(teamsDict[team_a],players_a,teamsDict[team_b],players_b)
        
    elif func == 12:
        team_a = input("Enter the first team name: ")
        team_b = input("Enter the second team name: ")
        if team_a in teamsDict and team_b in teamsDict:
            simulate_game(teamsDict[team_a], teamsDict[team_b])
        else:
            print("One or both teams not found.")
    elif func == 13:
        team_name = input("Enter the name of the team to save: ")
        if team_name in teamsDict:
            filename = input("Enter the filename to save to (e.g., team_data.csv): ")
            try:
                teamsDict[team_name].save_to_csv(filename)
                print(f"{team_name} has been saved to {filename}")
            except Exception as e:
                print(f"Failed to save team: {e}")
        else:
            print(f"{team_name} does not exist.")
            
    elif func == 14:
        name = input("Enter a name for the team: ")
        filename = input("Enter the CSV filename to load from (e.g., team_data.csv): ")
        team = load_team_from_csv(name, filename)
        if team:
            teamsDict[name] = team
            print(f"{name} has been loaded from {filename}")
        else:
            print(f"Failed to load team from {filename}")

    elif func == 15:
        team_name = input("Enter the team name: ")
        if team_name in teamsDict:
            metric = input("Sort by 'PPG' or 'PER': ").strip().lower()
            top_n = int(input("How many top players would you like to see? "))
            top_players = get_top_players(teamsDict[team_name], n=top_n, by=metric)
            print(f"\nTop {top_n} players on {team_name} by {metric.upper()}:")
            for name, value in top_players:
                print(f"{name}: {value}")
        else:
            print(f"{team_name} not found.")

    elif func == 16:
        stat = input("Enter the stat to rank players by (pts, rb, ast, stl, blk, to, pf): ").strip().lower()
        top_n = int(input("How many top players would you like to see? "))
        leaders = get_stat_leaders(stat, top_n)
        print(f"\nTop {top_n} players across all teams by {stat.upper()}:")
        for name, team, value in leaders:
            print(f"{name} ({team}): {value}")
    elif func == 0:
        """ends the program"""
        return 0  
    main()

def main():
    func = int(input("Please type a number to select what you want to do.\n"
                     "1:Create new team\n"
                     "2:Display team stats\n"
                     "3:Display Player Stats\n"
                     "4: Add player to team\n"
                     "5: Remove player from team\n"
                     "6: Update player stats\n"
                     "7: Trade player (one-way)\n"
                     "8: Trade players (two-way)\n"
                     "9: Calculate the Player Efficiency Rating of Players\n"
                     "10: Show overall team rankings and predictions\n"
                     "11: Tests the theoretical gains/losses of a trade\n"
                     "12: Simulate a game between two teams\n"
                     "13: Save a team to CSV\n"
                     "14: Load a team from CSV\n"
                     "15: Show top players on a team\n"
                     "16: Show stat leaders across all teams\n"
                     "0:Exit the program\n"))
    functions(func)

if __name__=="__main__":
    main()
    
