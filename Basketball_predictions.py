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
    
