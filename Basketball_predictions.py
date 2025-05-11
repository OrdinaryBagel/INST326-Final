import pandas as pd
import csv

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
        Driver:Thomas
        Navigator:Peter
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
    """Calculates Plater Efficiency with different measures"""

    def calculate_per(player, team_pace=100):
        """Calculates the PER Player Efficiency Rating for a player."""

        if player.gp == 0:
            return 0.0
        
        pts = player.pts
        reb = player.rb
        ast = player.ast
        stl = player.stl
        blk = player.blk
        to = player.to
        pf = player.pf

        # Calculate the individual PER Adds positive stats and subtracts negative states 
        # Multiplies by a number that indicates weight of the stat
        positive = (pts * 0.85 + reb * 0.7 + ast * 0.7 + stl * 1.2 + blk * 0.9)
        negative = (to * 0.9 + pf * 0.45)                       
        
        raw_per = positive - negative
        if team_pace != 100:
            per = raw_per * (100 / team_pace)            
                   
        return round(per, 1)

    def get_team_pers(team, team_pace=100):
        """ Calculate PER for all players on a team
        
        Returns:
        dict: Dictionary with player names as keys and PER values as values
        """
        pers = {}
        for player_name, player in team.playersDict.items():
            pers[player_name] = PlayerEfficiency.calculate_per(player, team_pace)
        
        return dict(sorted(pers.items(), key=lambda x: x[1], reverse=True))
    
def trade_player(team_from, team_to, player_name):
    """
    Driver: Zayan
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
                PlayerEfficiency.print_player_per(player)
            else:
                print(f"{player_name} is not on this team.")
        else:
            print(f"{team_name} does not exist")

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
                     "9: Calculate the Player Efficiency Rating of a Players and Teams\n"
                     "0:Exit the program\n"))
    functions(func)

if __name__=="__main__":
    main()
    
