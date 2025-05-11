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
    elif func == 0:
        """ends the program"""
        return 0
    main()

def main():
    func = int(input("Please type a number to select what you want to do.\n1:Create new team\n2:Display team stats\n3:Display Player Stats\n0:Exit the program\n"))
    functions(func)

if __name__=="__main__":
    main()
    
