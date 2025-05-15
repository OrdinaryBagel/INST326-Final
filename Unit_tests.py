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
    
if __name__ =="__main__":
    celtics_test()
    trade_calc_test_1()
    trade_calc_test_2()
    trade_calc_test_3()