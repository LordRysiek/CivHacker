from enums import *
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

    def canContainIndustrialZone(self):
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
            self.feature == TerrainFeature.NATURAL_WONDER or\
            self.terrain == TerrainType.NONE:
                return False
        if self.feature == TerrainFeature.FLOODPLAINS:
            return False
        return True

    def Randomise(self):
        self.terrain = random.choice(list(TerrainType))
        if(random.random()>0.5):
            self.feature = random.choice(list(TerrainFeature))
        if self.feature == TerrainFeature.NATURAL_WONDER:
            self.naturalWonder = random.choice(list(NaturalWonder))
        if(random.random()>0.7):
            self.resource = random.choice(list(Resource))
