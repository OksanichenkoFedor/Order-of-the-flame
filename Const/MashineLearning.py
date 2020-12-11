from Const.Units import LightInfantryType, HeavyInfantryType, CavalryType, LongDistanceSoldierType, HealerType, \
    AlchemistType

DamageCost = [50.0, 5.0, 5.0, 5.0]
TrainUnitCost = {LightInfantryType: 1, HeavyInfantryType: 1, CavalryType: 1, LongDistanceSoldierType: 1, HealerType: 1,
                 AlchemistType: 1}
UnitNumber = {LightInfantryType: 0, HeavyInfantryType: 1, CavalryType: 2, LongDistanceSoldierType: 3, HealerType: 4,
                 AlchemistType: 4}
UnitTypeOrder = {0: LightInfantryType, 1: HeavyInfantryType, 2: CavalryType, 3: LongDistanceSoldierType, 4: HealerType}
UnitTypeUnion = {0: LightInfantryType, 1: HeavyInfantryType, 2: CavalryType, 3: LongDistanceSoldierType,
                 4: AlchemistType}


ThrowUnitCost = 20

WinCost = 1000

TimeCost = 0.05

MaxGameTime = 20000

NNLayers = [81, 100, 11]

ParentsNumber = 5

ChildsNumber = 20

StartRate = 1

LearningRate = 0.1

ReluF = "relu"

Tanh = "tanh"

NNFunctions = [ReluF, ReluF]

