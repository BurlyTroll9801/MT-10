from Slab import Slab
from RelDef import RelDef
from TempDrDM import TempDrDM

Slab.RelDef = RelDef
Slab.TempDrDM = TempDrDM

if __name__ == "__main__":
    slab = Slab(Size=10, StartTemp="25C")
    print(slab.RelDef())
    print(slab.TempDrDM())
    