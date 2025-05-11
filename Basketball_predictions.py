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
            print(f"{name} is already on the team.")
            return
        self.playersDict[name] = Player(name, float(gp), float(pts), float(rb), float(ast), float(stl), float(blk), float(to), float(pf))
        print(f"{name} added to {self.name}.")
        self.calc_team_total()

    def remove_player(self,name):
        """
        Driver: Zayan
        Removes a player from the team.
        """
        if name in self.playersDict:
            del self.playersDict[name]
            print(f"{name} removed from {self.name}.")
            self.calc_team_total()
        else: 
            print(f"{name} is not on the team.")   



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
    func = int(input("Please type a number to select what you want to do.\n1:Create new team\n2:Display team stats\n3:Display Player Stats\n0:Exit the program\n"))
    functions(func)

if __name__=="__main__":
    main()
    
