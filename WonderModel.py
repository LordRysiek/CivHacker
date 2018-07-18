from enums import *
from Field import Field
import copy
class WonderModel:
    def __init__(self, wonderList, fieldList, fieldListWithNearestBorders):
        self.groupList = []
        self.fieldsByWonder = {}
        self.nextWonders = {}
        for key in wonderList:
            self.fieldsByWonder[key] = functionByWonder[key](fieldList, fieldListWithNearestBorders)
        for key in self.fieldsByWonder:
             if self.fieldsByWonder[key]:
                 self.nextWonders[key] = Prediction([]) #it doens't really matter,
                                                #we only need keys in the first PredictNextWonders() iteration
        self.nextWonders = self.PredictNextWonders()

    def GetPossibleWonders(self):
        return self.nextWonders.keys()

    def ChooseWonder(self, wonderName):
        district = districtByWonder[wonderName]
        for group in self.groupList:
            if group.district == district:
                group.wonders.append(wonderName)
                group.combinations = self.nextWonders[wonderName].combinations
                del self.nextWonders[wonderName]
                self.nextWonders = self.PredictNextWonders()
                return
        self.groupList.append(Group(wonderName, self.fieldsByWonder[wonderName]))
        del self.nextWonders[wonderName]
        self.nextWonders = self.PredictNextWonders()
        return

    def GetAllPossibleMatches(self):
        i = 0
        if not self.groupList:
            return []
        visited = [0 for x in range(len(self.groupList))]
        matches = []
        matchedFields = []
        while True:
            if visited[i] == len(self.groupList[i].combinations):
                if i==0:
                    return matches
                for j in range(i, len(self.groupList)):
                    visited[j] = 0
                i = i-1
                for j in range(len(groupList[i].combinations[visited[i]].wondersFields)):
                    matchedFields.pop()
                matchedFields.pop()
                visited[i] = visited[i] + 1
                continue
            if self.groupList[i].combinations[visited[i]].districtField in matchedFields:
                visited[i] = visited[i] + 1
                continue
            isClashing = False
            for field in self.groupList[i].combinations[visited[i]].wondersFields:
                if field in matchedFields:
                    isClashing = True
                    break
            if isClashing:
                visited[i] = visited[i] + 1
                continue
            matchedFields.extend(self.groupList[i].combinations[visited[i]].wondersFields)
            matchedFields.append(self.groupList[i].combinations[visited[i]].districtField)
            i = i + 1
            if i==len(self.groupList):
                newMatch = Match()
                for j in range(len(self.groupList)):
                    for k in range(len(self.groupList[j].combinations[visited[j]].wondersFields)):
                        newMatch.wondersMatch[self.groupList[j].wonders[k]] = self.groupList[j].combinations[visited[j]].wondersFields[k]
                    newMatch.districtsMatch[self.groupList[j].district] = self.groupList[j].combinations[visited[j]].districtField
                matches.append(newMatch)
                i = i-1
                for j in range(len(self.groupList[i].combinations[visited[i]].wondersFields)):
                    matchedFields.pop()
                matchedFields.pop()
                visited[i] = visited[i] + 1


    def PredictNextWonders(self):
        toReturn = {}
        for wonderName in self.nextWonders:
            newGroups = copy.deepcopy(self.groupList)
            districtOfNewWonder = districtByWonder[wonderName]
            foundGroup = 0
            for group in newGroups:
                if group.district == districtOfNewWonder:
                    foundGroup = group
                    break
            if foundGroup == 0:
                foundGroup = Group(wonderName, self.fieldsByWonder[wonderName])
                newGroups.append(foundGroup)
            else:
                foundGroup.wonders.append(wonderName)
                combinationsToRemove = []
                for combination in foundGroup.combinations:
                    isFound2 = False
                    for possibleFieldPair in self.fieldsByWonder[wonderName]:
                        if possibleFieldPair[1] == combination.districtField and\
                            possibleFieldPair[0] not in combination.wondersFields:
                            combination.wondersFields.append(possibleFieldPair[0])
                            isFound2 = True
                            break
                    if not isFound2:
                        combinationsToRemove.append(combination)
                for cTR in combinationsToRemove:
                    foundGroup.combinations.remove(cTR)
            if self.DoesMatchExist(newGroups):
                combinations = foundGroup.combinations
                toReturn[wonderName] = Prediction(combinations)
        return toReturn

    def DoesMatchExist(self, groupList):
        i = 0
        visited = [0 for x in range(len(groupList))]
        matchedFields = []
        while True:
            if visited[i] == len(groupList[i].combinations):
                if i==0:
                    return False
                for j in range(i, len(groupList)):
                    visited[j] = 0
                i = i-1
                for j in range(len(groupList[i].combinations[visited[i]].wondersFields)):
                    matchedFields.pop()
                matchedFields.pop()
                visited[i] = visited[i] + 1
                continue
            if groupList[i].combinations[visited[i]].districtField in matchedFields:
                visited[i] = visited[i] + 1
                continue
            isClashing = False
            for field in groupList[i].combinations[visited[i]].wondersFields:
                if field in matchedFields:
                    isClashing = True
                    break
            if isClashing:
                visited[i] = visited[i] + 1
                continue
            matchedFields.extend(groupList[i].combinations[visited[i]].wondersFields)
            matchedFields.append(groupList[i].combinations[visited[i]].districtField)
            i = i + 1
            if i==len(groupList):
                return True

class Group:
    def __init__(self, firstWonder, fieldsOfThisWonder):
        self.wonders = []
        self.wonders.append(firstWonder)
        self.combinations = []
        for fieldPair in fieldsOfThisWonder:
            self.combinations.append(Combination(fieldPair[0], fieldPair[1]))
        self.district = districtByWonder[firstWonder]

class Combination:
    def __init__(self, wonderField, districtField):
        self.wondersFields = []
        self.wondersFields.append(wonderField)
        self.districtField = districtField

class Prediction:
    def __init__(self, combinations):
        self.combinations = combinations

class Match:
    def __init__(self):
        self.districtsMatch = {}
        self.wondersMatch = {}
districtByWonder = {
WonderName.ALHAMBRA: DistrictName.ENCAMPMENT,
WonderName.AMUNDSEN_SCOTT_RESEARCH_STATION: DistrictName.CAMPUS,
WonderName.ANGKOR_WAT: DistrictName.AQUEDUCT,
WonderName.APADANA: DistrictName.NONE,
WonderName.BIG_BEN: DistrictName.COMMERCIAL_HUB,
WonderName.BOLSHOI_THEATRE: DistrictName.THEATER_SQUARE,
WonderName.BROADWAY: DistrictName.THEATER_SQUARE,
WonderName.CASA_DE_CONTRARACION: DistrictName.GOVERMENT_PLAZA,
WonderName.CHICHEN_ITZA: DistrictName.NONE,
WonderName.COLOSSEUM: DistrictName.ENTERTAINMENT_COMPLEX,
WonderName.COLOSSUS: DistrictName.HARBOR,
WonderName.CRISTO_REDENTOR: DistrictName.NONE,
WonderName.EIFFEL_TOWER: DistrictName.NONE,
WonderName.ESTADIO_DO_MARACANA: DistrictName.ENTERTAINMENT_COMPLEX,
WonderName.FORBIDDEN_CITY: DistrictName.NONE,
WonderName.GREAT_LIBRARY: DistrictName.CAMPUS,
WonderName.GREAT_LIGHTHOUSE: DistrictName.HARBOR,
WonderName.GREAT_ZIMBABWE: DistrictName.COMMERCIAL_HUB,
WonderName.HAGIA_SOPHIA: DistrictName.HOLY_SITE,
WonderName.HANGING_GARDENS: DistrictName.NONE,
WonderName.HERMITAGE: DistrictName.NONE,
WonderName.HUEY_TEOCALLI: DistrictName.NONE,
WonderName.JEBEL_BARKAL: DistrictName.NONE,
WonderName.KILWA_KISIWANI: DistrictName.NONE,
WonderName.KOTOKU_IN: DistrictName.HOLY_SITE,
WonderName.MAHABODHI_TEMPLE: DistrictName.HOLY_SITE,
WonderName.MAUSOLEUM_AT_HALICARNASSUS: DistrictName.HARBOR,
WonderName.MONT_ST_MICHEL: DistrictName.NONE,
WonderName.ORACLE: DistrictName.NONE,
WonderName.OXFORD_UNIVERSITY: DistrictName.CAMPUS,
WonderName.PETRA: DistrictName.NONE,
WonderName.POTALA_PALACE: DistrictName.NONE,
WonderName.PYRAMIDS: DistrictName.NONE,
WonderName.RUHR_VALLEY: DistrictName.INDUSTRIAL_ZONE,
WonderName.STATUE_OF_LIBERTY: DistrictName.HARBOR,
WonderName.STONEHENGE: DistrictName.NONE,
WonderName.ST_BASILS_CATHEDRAL: DistrictName.NONE,
WonderName.GREAT_ZIMBABWE: DistrictName.NONE,
WonderName.SYDNEY_OPERA_HOUSE: DistrictName.HARBOR,
WonderName.TAJ_MAHAL: DistrictName.NONE,
WonderName.TEMPLE_OF_ARTEMIS: DistrictName.NONE,
WonderName.TERACOTTA_ARMY: DistrictName.ENCAMPMENT,
WonderName.VENETIAN_ARSENAL: DistrictName.INDUSTRIAL_ZONE,
}
functionByWonder = {
WonderName.ALHAMBRA:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.isHills() and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainEncampment()],
WonderName.AMUNDSEN_SCOTT_RESEARCH_STATION:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.terrain == TerrainType.SNOW or
                                            field.terrain == TerrainType.SNOW_HILLS
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCampus()],
WonderName.ANGKOR_WAT:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainAqueduct(fieldListWithNearestBorders)],
WonderName.APADANA:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isAdjacentToCity()],
WonderName.BIG_BEN:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isRiver is True
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCommercialHub()],
WonderName.BOLSHOI_THEATRE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainTheaterSquare()],
WonderName.BROADWAY:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainTheaterSquare()],
WonderName.CASA_DE_CONTRARACION:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainGovermentPlaza()],
WonderName.CHICHEN_ITZA:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.feature == TerrainFeature.RAINFOREST],
WonderName.COLOSSEUM:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainEntertainmentComplex()],
WonderName.COLOSSUS:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            or field.terrain == TerrainType.LAKE
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()],
WonderName.CRISTO_REDENTOR:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.isHills()
                                            and field.BasicWonderConditions()],
WonderName.EIFFEL_TOWER:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isAdjacentToCity()
                                            and (field.isHills() is not True)],
WonderName.ESTADIO_DO_MARACANA:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainEntertainmentComplex()],
WonderName.FORBIDDEN_CITY:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isAdjacentToCity()
                                            and (field.isHills() is not True)],
WonderName.GREAT_LIBRARY:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCampus()],
WonderName.GREAT_LIGHTHOUSE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            or field.terrain == TerrainType.LAKE
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()],
WonderName.GREAT_ZIMBABWE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and any(x.resource == Resource.CATTLE
                                                and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCommercialHub()
                                            and distField.resource is not Resource.CATTLE],
WonderName.HAGIA_SOPHIA:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHolySite()],
WonderName.HANGING_GARDENS:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.isRiver
                                            and field.BasicWonderConditions()],
WonderName.HERMITAGE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.isRiver
                                            and field.BasicWonderConditions()
                                            and field.terrain is not TerrainType.TUNDRA
                                            and field.terrain is not TerrainType.TUNDRA_HILLS
                                            and field.terrain is not TerrainType.DESERT
                                            and field.terrain is not TerrainType.DESERT_HILLS],
WonderName.HUEY_TEOCALLI:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.terrain == TerrainType.LAKE
                                            and any(x.isNeighbour(field)
                                                and x.terrain is not TerrainType.LAKE
                                                and x.terrain is not TerrainType.COAST
                                                and x.terrain is not TerrainType.OCEAN
                                                for x in fieldListWithNearestBorders)],
WonderName.JEBEL_BARKAL:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.terrain == TerrainType.DESERT_HILLS
                                            and field.BasicWonderConditions()],
WonderName.KILWA_KISIWANI:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and not field.isHills()
                                            and any(x.isNeighbour(field)
                                                and (x.terrain is TerrainType.LAKE
                                                or x.terrain is TerrainType.COAST)
                                                for x in fieldListWithNearestBorders)],
WonderName.KOTOKU_IN:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHolySite()],
WonderName.MAHABODHI_TEMPLE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.feature == TerrainFeature.WOODS
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHolySite()],
WonderName.MAUSOLEUM_AT_HALICARNASSUS:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            or field.terrain == TerrainType.LAKE
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()],
WonderName.MONT_ST_MICHEL:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if (field.feature == TerrainFeature.FLOODPLAINS
                                            or field.feature == TerrainFeature.MARSH)
                                            and (field.x is not 4 or field.y is not 4)],
WonderName.ORACLE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isHills()],
WonderName.OXFORD_UNIVERSITY:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if
                                            (field.terrain is TerrainType.GRASSLAND
                                            or field.terrain is TerrainType.PLAINS)
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCampus()],
WonderName.PETRA:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if not field.isHills()
                                            and (field.terrain is TerrainType.DESERT
                                            or field.feature is TerrainFeature.FLOODPLAINS)
                                            and (field.x is not 4 or field.y is not 4)],
WonderName.POTALA_PALACE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isHills()
                                            and any(x.isNeighbour(field)
                                                and (x.terrain is TerrainType.MOUNTAINS)
                                                for x in fieldListWithNearestBorders)],
WonderName.PYRAMIDS:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.terrain == TerrainType.DESERT
                                            and (field.x is not 4 or field.y is not 4)],
WonderName.RUHR_VALLEY:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.isRiver
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainIndustrialZone()],
WonderName.STATUE_OF_LIBERTY:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            or field.terrain == TerrainType.LAKE
                                            and any(x.isNeighbour(field)
                                                and x.terrain is not TerrainType.LAKE
                                                and x.terrain is not TerrainType.COAST
                                                and x.terrain is not TerrainType.OCEAN
                                                for x in fieldListWithNearestBorders)
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()],
WonderName.STONEHENGE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and not field.isHills()
                                            and any(x.isNeighbour(field)
                                                and (x.resource is Resource.STONE)
                                                for x in fieldListWithNearestBorders)],
WonderName.ST_BASILS_CATHEDRAL:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isAdjacentToCity()],
WonderName.GREAT_ZIMBABWE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and any(x.resource == Resource.STONE
                                                and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                            and not field.isHills()],
WonderName.SYDNEY_OPERA_HOUSE:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()],
WonderName.TAJ_MAHAL:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isRiver],
WonderName.TEMPLE_OF_ARTEMIS:
                        lambda fieldList, fieldListWithNearestBorders: [(field, Field(0,0))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and any((x.resource == Resource.DEER
                                                    or x.resource == Resource.TRUFFLES
                                                    or x.resource == Resource.FURS
                                                    or x.resource == Resource.IVORY)
                                                and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                            and not field.isHills()],
WonderName.TERACOTTA_ARMY:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and (field.terrain == TerrainType.GRASSLAND
                                            or field.terrain == TerrainType.PLAINS)
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainEncampment()],
WonderName.VENETIAN_ARSENAL:
                        lambda fieldList, fieldListWithNearestBorders: [(field, distField)
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainIndustrialZone()],
}
