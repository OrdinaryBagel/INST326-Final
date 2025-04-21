

teamsDict = {}

class Team:
    def __init__(self,name, gp, pts, off_rebounds, def_rebounds, ast, stl, blk, to, pf):
        """
        Driver: Thomas, Peter
        Navigator: Khalid
        initalizes team objects the variables represent:
        name = name
        gp = games played
        pts = points
        off_rebounds = offensive rebounds
        def_rebounds = defensive rebounds
        total_rebounds = total rebounds
        ast = assists
        stl = steals
        blk = blocks
        to = turn overs
        pf = fouls
        ast_to = assist turnover ratio"""
        self.name = name
        self.gp = gp
        self.pts = pts
        self.off_rebounds = off_rebounds
        self.def_rebounds = def_rebounds
        self.total_rebounds = off_rebounds + def_rebounds
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.to = to
        self.pf = pf
        self.ast_to = ast/to
    def update(self, gp, pts, off_rebounds, def_rebounds, ast, stl, blk, to, pf):
        """
        updates the stats of a team, basically the same as __init__ so it will not be counted for total methods"""
        self.gp = gp
        self.pts = pts
        self.off_rebounds = off_rebounds
        self.def_rebounds = def_rebounds
        self.total_rebounds = off_rebounds + def_rebounds
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.to = to
        self.pf = pf
        self.ast_to = ast/to

    def __repr__(self):
        return (
            f"Team{self.name}, GP={self.gp}, PTS={self.pts}\n"
            f"REB={self.total_rebounds} OFF={self.off_rebounds}, DEF={self.def_rebounds}\n"
            f"AST={self.ast}, STL={self.stl}, BLK={self.blk}\n"
            f"TO={self.to}, PF={self.pf}, AST/TO={self.ast_to}\n"
        )
    
def functions(func):
    """determines what the program will do, will be update by multiple people as the project moves forward."""
    if func == 1:
        """creates new teams"""
        name = input("Please enter the name of the team: ")
        gp = float(input(f"Please enter the number of games played by the {name}: "))
        pts = float(input(f"Please enter the average number of points per game scored by the {name}: "))
        off_rebounds = float(input(f"Please enter the average number of offensive rebounds per game earned by the {name}: "))
        def_rebounds = float(input(f"Please enter the average number of defensive rebounds per game earned by the {name}: "))
        ast = float(input(f"Please enter the average number of assists per game earned by the {name}: "))
        stl = float(input(f"Please enter the average number of steals per game earned by the {name}: "))
        blk = float(input(f"Please enter the average number of blocks per game earned by the {name}: "))
        to = float(input(f"Please enter the average number of turnovers per game earned by the {name}: "))
        pf = float(input(f"Please enter the average number of fouls per game earned by the {name}: "))
        teamsDict[name] = Team(name,gp,pts,off_rebounds,def_rebounds,ast,stl,blk,to,pf)
    elif func == 2:
        """updates existing teams"""
        name = input("Please enter the name of the team: ")
        if name in teamsDict:
            gp = float(input(f"Please enter the number of games played by the {name}: "))
            pts = float(input(f"Please enter the average number of points per game scored by the {name}: "))
            off_rebounds = float(input(f"Please enter the average number of offensive rebounds per game earned by the {name}: "))
            def_rebounds = float(input(f"Please enter the average number of defensive rebounds per game earned by the {name}: "))
            ast = float(input(f"Please enter the average number of assists per game earned by the {name}: "))
            stl = float(input(f"Please enter the average number of steals per game earned by the {name}: "))
            blk = float(input(f"Please enter the average number of blocks per game earned by the {name}: "))
            to = float(input(f"Please enter the average number of turnovers per game earned by the {name}: "))
            pf = float(input(f"Please enter the average number of fouls per game earned by the {name}: "))
        else:
            print("That team does not exist")
    elif func == 0:
        """ends the program"""
        return 0
    main()

def main():
    func = int(input("Please type a number to select what you want to do.\n1:Create new team\n2:Update team\n0:Exit the program\n"))
    functions(func)

if __name__=="__main__":
    main()
    
