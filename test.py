from Field import Field
from Field import TerrainType
from Field import TerrainFeature
from Field import NaturalWonder
from Wonder import Wonder
from Wonder import WonderName
from Wonder import DistrictName
"""
field1 = Field(1,1)
field2 = Field(2,2)
field3 = Field(2,3)
field4 = Field(1,1)
print(field1.isNeighbour(field2))
print(field1.isNeighbour(field3))
print(field2.isNeighbour(field3))
print(field1.isNeighbour(field4))
"""
"""
fieldList = []
for x in range(1,8):
    for y in range(max(1,x-3), 7-abs(4-x)+max(1,x-3)):
        field = Field(x,y)
        field.Randomise()
        fieldList.append(field)
"""
fieldListWithNearestBorders = []
for x in range(0,9):
    for y in range(max(0,x-4), 9-abs(4-x)+max(0,x-4)):
        field = Field(x,y)
        field.Randomise()
        fieldListWithNearestBorders.append(field)
fieldList = [field for field in fieldListWithNearestBorders if field.x is not 0 and
            field.x is not 8 and field.y is not 0 and field.y is not 8 and
            field.y - field.x < 4 and field.x-field.y < 4]

for field in fieldListWithNearestBorders:
    print("_________")
    print(field.x)
    print(field.y)
    print(field.terrain)
    print(field.feature)
    print(field.naturalWonder)
    print(field.resource)
"""
print("_____NIZEJ NORMALNE______")
for field in fieldList:
    print("_________")
    print(field.x)
    print(field.y)
    print(field.terrain)
    print(field.feature)
    print(field.naturalWonder)
    print(field.resource)
"""
wonderList = []
wonderList.append(Wonder(WonderName.ALHAMBRA,
                        lambda fieldList: [(field, (DistrictName.ENCAMPMENT, distField))
                                            for field in fieldList if field.isHills() and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainEncampment()]))
wonderList.append(Wonder(WonderName.AMUNDSEN_SCOTT_RESEARCH_STATION,
                        lambda fieldList: [(field, (DistrictName.CAMPUS, distField))
                                            for field in fieldList if field.terrain == TerrainType.SNOW or
                                            field.terrain == TerrainType.SNOW_HILLS
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCampus()]))
wonderList.append(Wonder(WonderName.ANGKOR_WAT,
                        lambda fieldList: [(field, (DistrictName.AQUEDUCT, distField))
                                            for field in fieldList if field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainAqueduct(fieldListWithNearestBorders)]))
wonderList.append(Wonder(WonderName.APADANA,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isAdjacentToCity()]))
wonderList.append(Wonder(WonderName.BIG_BEN,
                        lambda fieldList: [(field, (DistrictName.COMMERCIAL_HUB, distField))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isRiver is True
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCommercialHub()]))
wonderList.append(Wonder(WonderName.BOLSHOI_THEATRE,
                        lambda fieldList: [(field, (DistrictName.THEATER_SQUARE, distField))
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainTheaterSquare()]))
wonderList.append(Wonder(WonderName.BROADWAY,
                        lambda fieldList: [(field, (DistrictName.THEATER_SQUARE, distField))
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainTheaterSquare()]))
wonderList.append(Wonder(WonderName.CASA_DE_CONTRARACION,
                        lambda fieldList: [(field, (DistrictName.GOVERMENT_PLAZA, distField))
                                            for field in fieldList if field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainGovermentPlaza()]))
wonderList.append(Wonder(WonderName.CHICHEN_ITZA,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.feature == TerrainFeature.RAINFOREST]))
wonderList.append(Wonder(WonderName.COLOSSEUM,
                        lambda fieldList: [(field, (DistrictName.ENTERTAINMENT_COMPLEX, distField))
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainEntertainmentComplex()]))
wonderList.append(Wonder(WonderName.COLOSSUS,
                        lambda fieldList: [(field, (DistrictName.HARBOR, distField))
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            or field.terrain == TerrainType.LAKE
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()]))
wonderList.append(Wonder(WonderName.CRISTO_REDENTOR,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.isHills()
                                            and field.BasicWonderConditions()]))
wonderList.append(Wonder(WonderName.EIFFEL_TOWER,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isAdjacentToCity()
                                            and (field.isHills() is not True)]))
wonderList.append(Wonder(WonderName.ESTADIO_DO_MARACANA,
                        lambda fieldList: [(field, (DistrictName.ENTERTAINMENT_COMPLEX, distField))
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainEntertainmentComplex()]))
wonderList.append(Wonder(WonderName.FORBIDDEN_CITY,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isAdjacentToCity()
                                            and (field.isHills() is not True)]))
wonderList.append(Wonder(WonderName.GREAT_LIBRARY,
                        lambda fieldList: [(field, (DistrictName.CAMPUS, distField))
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCampus()]))
wonderList.append(Wonder(WonderName.GREAT_LIGHTHOUSE,
                        lambda fieldList: [(field, (DistrictName.HARBOR, distField))
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            or field.terrain == TerrainType.LAKE
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()]))
wonderList.append(Wonder(WonderName.GREAT_ZIMBABWE,
                        lambda fieldList: [(field, (DistrictName.COMMERCIAL_HUB, distField))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and any(x.resource == Resource.CATTLE
                                                and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCommercialHub()
                                            and distField.resource is not Resource.CATTLE]))
wonderList.append(Wonder(WonderName.HAGIA_SOPHIA,
                        lambda fieldList: [(field, (DistrictName.HOLY_SITE, distField))
                                            for field in fieldList if not field.isHills()
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHolySite()]))
wonderList.append(Wonder(WonderName.HANGING_GARDENS,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.isRiver
                                            and field.BasicWonderConditions()]))
wonderList.append(Wonder(WonderName.HERMITAGE,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.isRiver
                                            and field.BasicWonderConditions()
                                            and field.terrain is not TerrainType.TUNDRA
                                            and field.terrain is not TerrainType.TUNDRA_HILLS
                                            and field.terrain is not TerrainType.DESERT
                                            and field.terrain is not TerrainType.DESERT_HILLS]))
wonderList.append(Wonder(WonderName.HUEY_TEOCALLI,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.terrain == TerrainType.LAKE
                                            and any(x.isNeighbour(field)
                                                and x.terrain is not TerrainType.LAKE
                                                and x.terrain is not TerrainType.COAST
                                                and x.terrain is not TerrainType.OCEAN
                                                for x in fieldListWithNearestBorders)]))
wonderList.append(Wonder(WonderName.JEBEL_BARKAL,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.terrain == TerrainType.DESERT_HILLS
                                            and field.BasicWonderConditions()]))
wonderList.append(Wonder(WonderName.KILWA_KISIWANI,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and not field.isHills()
                                            and any(x.isNeighbour(field)
                                                and (x.terrain is TerrainType.LAKE
                                                or x.terrain is TerrainType.COAST)
                                                for x in fieldListWithNearestBorders)]))
wonderList.append(Wonder(WonderName.KOTOKU_IN,
                        lambda fieldList: [(field, (DistrictName.HOLY_SITE, distField))
                                            for field in fieldList if field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHolySite()]))
wonderList.append(Wonder(WonderName.MAHABODHI_TEMPLE,
                        lambda fieldList: [(field, (DistrictName.HOLY_SITE, distField))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.feature == TerrainFeature.WOODS
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHolySite()]))
wonderList.append(Wonder(WonderName.MAUSOLEUM_AT_HALICARNASSUS,
                        lambda fieldList: [(field, (DistrictName.HARBOR, distField))
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            or field.terrain == TerrainType.LAKE
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()]))
wonderList.append(Wonder(WonderName.MONT_ST_MICHEL,
                        lambda fieldList: [(field,)
                                            for field in fieldList if (field.feature == TerrainFeature.FLOODPLAINS
                                            or field.feature == TerrainFeature.MARSH)
                                            and (self.x is not 4 or self.y is not 4)]))
wonderList.append(Wonder(WonderName.ORACLE,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isHills()]))
wonderList.append(Wonder(WonderName.OXFORD_UNIVERSITY,
                        lambda fieldList: [(field, (DistrictName.CAMPUS, distField))
                                            for field in fieldList if
                                            (field.terrain is TerrainType.GRASSLAND
                                            or field.terrain is TerrainType.PLAINS)
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCampus()]))
wonderList.append(Wonder(WonderName.PETRA,
                        lambda fieldList: [(field,)
                                            for field in fieldList if not field.isHills()
                                            and (field.terrain is TerrainType.DESERT
                                            or field.feature is TerrainFeature.FLOODPLAINS)
                                            and (field.x is not 4 or field.y is not 4)]))
wonderList.append(Wonder(WonderName.POTALA_PALACE,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isHills()
                                            and any(x.isNeighbour(field)
                                                and (x.terrain is TerrainType.MOUNTAINS)
                                                for x in fieldListWithNearestBorders)]))
wonderList.append(Wonder(WonderName.PYRAMIDS,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.terrain == TerrainType.DESERT
                                            and (field.x is not 4 or field.y is not 4)]))
wonderList.append(Wonder(WonderName.RUHR_VALLEY,
                        lambda fieldList: [(field, (DistrictName.INDUSTRIAL_ZONE, distField))
                                            for field in fieldList if field.isRiver
                                            and field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainIndustrialZone()]))
wonderList.append(Wonder(WonderName.STATUE_OF_LIBERTY,
                        lambda fieldList: [(field, (DistrictName.HARBOR, distField))
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            or field.terrain == TerrainType.LAKE
                                            and any(x.isNeighbour(field)
                                                and x.terrain is not TerrainType.LAKE
                                                and x.terrain is not TerrainType.COAST
                                                and x.terrain is not TerrainType.OCEAN
                                                for x in fieldListWithNearestBorders)
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()]))
wonderList.append(Wonder(WonderName.ST_BASILS_BATHEDRAL,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isAdjacentToCity()]))
wonderList.append(Wonder(WonderName.GREAT_ZIMBABWE,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and any(x.resource == Resource.STONE
                                                and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                            and not field.isHills()]))
wonderList.append(Wonder(WonderName.SYDNEY_OPERA_HOUSE,
                        lambda fieldList: [(field, (DistrictName.HARBOR, distField))
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainHarbor()]))
wonderList.append(Wonder(WonderName.TAJ_MAHAL,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and field.isRiver]))
wonderList.append(Wonder(WonderName.TEMPLE_OF_ARTEMIS,
                        lambda fieldList: [(field,)
                                            for field in fieldList if field.BasicWonderConditions()
                                            and any((x.resource == Resource.DEER
                                                    or x.resource == Resource.TRUFFLES
                                                    or x.resource == Resource.FURS
                                                    or x.resource == Resource.IVORY)
                                                and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                            and not field.isHills()]))
wonderList.append(Wonder(WonderName.TERACOTTA_ARMY,
                        lambda fieldList: [(field, (DistrictName.ENCAMPMENT, distField))
                                            for field in fieldList if field.BasicWonderConditions()
                                            and (field.terrain == TerrainType.GRASSLAND
                                            or field.terrain == TerrainType.PLAINS)
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainEncampment()]))
wonderList.append(Wonder(WonderName.VENETIAN_ARSENAL,
                        lambda fieldList: [(field, (DistrictName.INDUSTRIAL_ZONE, distField))
                                            for field in fieldList if field.terrain == TerrainType.COAST
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainIndustrialZone()]))

for wonder in wonderList:
    wonder.WhereCanItBeBuilt()
