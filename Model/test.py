from Stan import Stan
from RelDef import RelDef
from Model.TempDrDMove import TempDrDMove
from TempDrDR import TempDrDR
from DefResistance import DefResistance
from TorEffPow import TorrEffPow
from CapCondition import CapCondition
from FricCoef import FricCoef

Stan.RelDef = RelDef #1
Stan.TempDrDMove = TempDrDMove #2
Stan.TempDrDR = TempDrDR #3
Stan.DefResistance = DefResistance #4
Stan.TorrEffPow = TorrEffPow #5
Stan.CapCondition = CapCondition #6
Stan.FricCoef = FricCoef #7


if __name__ == "__main__":
    Process = Stan(Size=10, StartTemp="25C")
    