from enum import Enum
import random

class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.terrain = TerrainType.NONE
        self.feature = TerrainFeature.NONE
        self.naturalWonder = NaturalWonder.NONE
        self.resource = Resource.NONE
        self.isRiver = False

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

    def isHills(self):
        return self.terrain == TerrainType.DESERT_HILLS or \
        self.terrain == TerrainType.GRASSLAND_HILLS or \
        self.terrain == TerrainType.PLAINS_HILLS or \
        self.terrain == TerrainType.SNOW_HILLS or \
        self.terrain == TerrainType.TUNDRA_HILLS

    def isAdjacentToCity(self):
        return self.isNeighbour(Field(4,4))

    def canContainEncampment(self):
        if not self.BasicWonderConditions():
            return False
        if self.isAdjacentToCity():
            return False
        return True

    def canContainCampus(self):
        return self.BasicWonderConditions()

    def canContainHolySite(self):
        return self.BasicWonderConditions()

    def canContainCommercialHub(self):
        return self.BasicWonderConditions()

    def canContainEntertainmentComplex(self):
        return self.BasicWonderConditions()

    def canContainTheaterSquare(self):
        return self.BasicWonderConditions()

    def canContainGovermentPlaza(self):
        return self.BasicWonderConditions()

    def canContainHarbor(self):
        return self.terrain == TerrainType.COAST or self.terrain == TerrainType.LAKE

    def canContainAqueduct(self, fieldList):
        if not self.BasicWonderConditions():
            return False
        if not self.isAdjacentToCity():
            return False
        if self.isRiver is True:
            return True
        for field in fieldList:
            if field.terrain == TerrainType.MOUNTAINS or \
                field.terrain == TerrainType.LAKE or \
                field.feature == TerrainFeature.OASIS:
                if self.isNeighbour(field):
                    return True
        return False

    def BasicWonderConditions(self):
        if self.x == 4 and self.y == 4:
            return False
        if self.terrain == TerrainType.MOUNTAINS or\
            self.terrain == TerrainType.COAST or\
            self.terrain == TerrainType.LAKE or\
            self.terrain == TerrainType.OCEAN or\
            self.terrain == TerrainType.NATURAL_WONDER or\
            self.terrain == TerrainType.NONE:
                return False
        if self.feature == TerrainFeature.FLOODPLAINS:
            return False
        return True

    def Randomise(self):
        self.terrain = random.choice(list(TerrainType))
        if self.terrain == TerrainType.NATURAL_WONDER:
            self.naturalWonder = random.choice(list(NaturalWonder))
        else:
            if(random.random()>0.5):
                self.feature = random.choice(list(TerrainFeature))
            if(random.random()>0.7):
                self.resource = random.choice(list(Resource))

class TerrainType(Enum):
    COAST = 1
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
    NATURAL_WONDER = 14     #TODO: check if natural wonders have terraintype despite them being natural wonders
    LAKE = 15
    NONE = 16

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
    DELICATE_ARCH = 17
    EYE_OF_THE_SAHARA = 18
    LAKE_RETBA = 19
    MATTERHORN = 20
    MOUNT_RORAIMA = 21
    UBSUNUR_HOLLOW = 22
    ZHANGYE_DANXIA = 23
    KAKADU = 24
    PINNACLES = 25
    VINLAND = 26
    NONE = 27

class Resource(Enum):
    BANANAS = 1
    CATTLE = 2
    COPPER = 3
    CRABS = 4
    DEER= 5
    FISH = 6
    RICE = 7
    SHEEP = 8
    STONE = 9
    WHEAT = 10
    CITRUS = 11
    COCOA = 12
    COFFEE = 13
    COTTON = 14
    DIAMONDS = 15
    DYES = 16
    FURS = 17
    GYPSUM = 18
    INCENSE = 19
    IVORY = 20
    JADE = 21
    MARBLE = 22
    MERCURY = 23
    PEARLS = 24
    SALT = 25
    SILK = 26
    SILVER = 27
    SPICES = 28
    SUGAR = 29
    TEA = 30
    TOBACCO = 31
    TRUFFLES = 32
    WHALES = 33
    WINE = 34
    NONE = 35
