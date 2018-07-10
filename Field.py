from enum import Enum

class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.terrain = TerrainType.NONE
        self.feature = TerrainFeature.NONE
        self.naturalWonder = NaturalWonder.NONE

    def isNeighbour(self, field):
        if self.x == field.x and abs(self.y-field.y)==1:
            return True
        elif self.y == field.y and abs(self.x-field.x)==1:
            return True
        elif self.x == field.x+1 and self.y == field.y+1:
            return True
        else:
            return (self.x == field.x-1 and self.y == field.y-1)

    def SetTerrain(self, terrain):
        self.terrain = terrain

    def SetFeature(self, feature):
        self.feature = feature

    def SetNaturalWonder(self, wonder):
        self.naturalWonder = wonder

class TerrainType(Enum):
    COAST_AND_LAKE = 1
    DESERT = 2
    DESERT_HILLS = 3
    GRASSLAND = 4
    GRASSLAND_HILLS = 5
    MOUNTAINS = 6
    OCEAN = 7
    PLAINS = 8
    PLAINS_HILLS = 9
    SNOW = 10
    SNOW_HILLS = 11
    TUNDRA = 12
    TUNDRA_HILLS = 13
    NATURAL_WONDER = 14
    NONE = 15

class TerrainFeature(Enum):
    FLOODPLAINS = 1
    ICE = 2
    MARSH = 3
    OASIS = 4
    RAINFOREST = 5
    WOODS = 6
    NONE = 7

class NaturalWonder(Enum):
    CLIFFS_OF_DOVER = 1
    CRATER_LAKE = 2
    DEAD_SEA = 3
    EYJAFJALLAJOKULL = 4
    GLAPAGOS_ISLANDS = 5
    GIANTS_CAUSEWAY = 6
    GREAT_BARRIER_REEF = 7
    LYSEFJORD = 8
    MOUNT_EVEREST = 9
    MOUNT_KILIMANJARO = 10
    PANTANAL = 11
    PIOPIOTAHI = 12
    TORRES_DEL_PAINE = 13
    TSINGY_DE_BEMARAHA = 14
    ULURU = 15
    YOSEMITE = 16
    NONE = 17
