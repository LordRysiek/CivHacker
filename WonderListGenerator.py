from Wonder import Wonder
from Wonder import WonderName
from Wonder import DistrictName
from Field import Field
from Field import TerrainType
from Field import TerrainFeature
from Field import NaturalWonder
from Field import Resource
def GenerateWonderList():
    wonderList = []
    wonderList.append(Wonder(WonderName.ALHAMBRA,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.ENCAMPMENT, distField))
                                                for field in fieldList if field.isHills() and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainEncampment()]))
    wonderList.append(Wonder(WonderName.AMUNDSEN_SCOTT_RESEARCH_STATION,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.CAMPUS, distField))
                                                for field in fieldList if field.terrain == TerrainType.SNOW or
                                                field.terrain == TerrainType.SNOW_HILLS
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainCampus()]))
    wonderList.append(Wonder(WonderName.ANGKOR_WAT,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.AQUEDUCT, distField))
                                                for field in fieldList if field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainAqueduct(fieldListWithNearestBorders)]))
    wonderList.append(Wonder(WonderName.APADANA,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.isAdjacentToCity()]))
    wonderList.append(Wonder(WonderName.BIG_BEN,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.COMMERCIAL_HUB, distField))
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.isRiver is True
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainCommercialHub()]))
    wonderList.append(Wonder(WonderName.BOLSHOI_THEATRE,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.THEATER_SQUARE, distField))
                                                for field in fieldList if not field.isHills()
                                                and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainTheaterSquare()]))
    wonderList.append(Wonder(WonderName.BROADWAY,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.THEATER_SQUARE, distField))
                                                for field in fieldList if not field.isHills()
                                                and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainTheaterSquare()]))
    wonderList.append(Wonder(WonderName.CASA_DE_CONTRARACION,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.GOVERMENT_PLAZA, distField))
                                                for field in fieldList if field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainGovermentPlaza()]))
    wonderList.append(Wonder(WonderName.CHICHEN_ITZA,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.feature == TerrainFeature.RAINFOREST]))
    wonderList.append(Wonder(WonderName.COLOSSEUM,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.ENTERTAINMENT_COMPLEX, distField))
                                                for field in fieldList if not field.isHills()
                                                and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainEntertainmentComplex()]))
    wonderList.append(Wonder(WonderName.COLOSSUS,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.HARBOR, distField))
                                                for field in fieldList if field.terrain == TerrainType.COAST
                                                or field.terrain == TerrainType.LAKE
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainHarbor()]))
    wonderList.append(Wonder(WonderName.CRISTO_REDENTOR,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.isHills()
                                                and field.BasicWonderConditions()]))
    wonderList.append(Wonder(WonderName.EIFFEL_TOWER,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.isAdjacentToCity()
                                                and (field.isHills() is not True)]))
    wonderList.append(Wonder(WonderName.ESTADIO_DO_MARACANA,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.ENTERTAINMENT_COMPLEX, distField))
                                                for field in fieldList if not field.isHills()
                                                and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainEntertainmentComplex()]))
    wonderList.append(Wonder(WonderName.FORBIDDEN_CITY,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.isAdjacentToCity()
                                                and (field.isHills() is not True)]))
    wonderList.append(Wonder(WonderName.GREAT_LIBRARY,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.CAMPUS, distField))
                                                for field in fieldList if not field.isHills()
                                                and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainCampus()]))
    wonderList.append(Wonder(WonderName.GREAT_LIGHTHOUSE,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.HARBOR, distField))
                                                for field in fieldList if field.terrain == TerrainType.COAST
                                                or field.terrain == TerrainType.LAKE
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainHarbor()]))
    wonderList.append(Wonder(WonderName.GREAT_ZIMBABWE,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.COMMERCIAL_HUB, distField))
                                                for field in fieldList if field.BasicWonderConditions()
                                                and any(x.resource == Resource.CATTLE
                                                    and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainCommercialHub()
                                                and distField.resource is not Resource.CATTLE]))
    wonderList.append(Wonder(WonderName.HAGIA_SOPHIA,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.HOLY_SITE, distField))
                                                for field in fieldList if not field.isHills()
                                                and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainHolySite()]))
    wonderList.append(Wonder(WonderName.HANGING_GARDENS,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.isRiver
                                                and field.BasicWonderConditions()]))
    wonderList.append(Wonder(WonderName.HERMITAGE,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.isRiver
                                                and field.BasicWonderConditions()
                                                and field.terrain is not TerrainType.TUNDRA
                                                and field.terrain is not TerrainType.TUNDRA_HILLS
                                                and field.terrain is not TerrainType.DESERT
                                                and field.terrain is not TerrainType.DESERT_HILLS]))
    wonderList.append(Wonder(WonderName.HUEY_TEOCALLI,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.terrain == TerrainType.LAKE
                                                and any(x.isNeighbour(field)
                                                    and x.terrain is not TerrainType.LAKE
                                                    and x.terrain is not TerrainType.COAST
                                                    and x.terrain is not TerrainType.OCEAN
                                                    for x in fieldListWithNearestBorders)]))
    wonderList.append(Wonder(WonderName.JEBEL_BARKAL,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.terrain == TerrainType.DESERT_HILLS
                                                and field.BasicWonderConditions()]))
    wonderList.append(Wonder(WonderName.KILWA_KISIWANI,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and not field.isHills()
                                                and any(x.isNeighbour(field)
                                                    and (x.terrain is TerrainType.LAKE
                                                    or x.terrain is TerrainType.COAST)
                                                    for x in fieldListWithNearestBorders)]))
    wonderList.append(Wonder(WonderName.KOTOKU_IN,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.HOLY_SITE, distField))
                                                for field in fieldList if field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainHolySite()]))
    wonderList.append(Wonder(WonderName.MAHABODHI_TEMPLE,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.HOLY_SITE, distField))
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.feature == TerrainFeature.WOODS
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainHolySite()]))
    wonderList.append(Wonder(WonderName.MAUSOLEUM_AT_HALICARNASSUS,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.HARBOR, distField))
                                                for field in fieldList if field.terrain == TerrainType.COAST
                                                or field.terrain == TerrainType.LAKE
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainHarbor()]))
    wonderList.append(Wonder(WonderName.MONT_ST_MICHEL,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if (field.feature == TerrainFeature.FLOODPLAINS
                                                or field.feature == TerrainFeature.MARSH)
                                                and (field.x is not 4 or field.y is not 4)]))
    wonderList.append(Wonder(WonderName.ORACLE,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.isHills()]))
    wonderList.append(Wonder(WonderName.OXFORD_UNIVERSITY,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.CAMPUS, distField))
                                                for field in fieldList if
                                                (field.terrain is TerrainType.GRASSLAND
                                                or field.terrain is TerrainType.PLAINS)
                                                and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainCampus()]))
    wonderList.append(Wonder(WonderName.PETRA,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if not field.isHills()
                                                and (field.terrain is TerrainType.DESERT
                                                or field.feature is TerrainFeature.FLOODPLAINS)
                                                and (field.x is not 4 or field.y is not 4)]))
    wonderList.append(Wonder(WonderName.POTALA_PALACE,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.isHills()
                                                and any(x.isNeighbour(field)
                                                    and (x.terrain is TerrainType.MOUNTAINS)
                                                    for x in fieldListWithNearestBorders)]))
    wonderList.append(Wonder(WonderName.PYRAMIDS,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.terrain == TerrainType.DESERT
                                                and (field.x is not 4 or field.y is not 4)]))
    wonderList.append(Wonder(WonderName.RUHR_VALLEY,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.INDUSTRIAL_ZONE, distField))
                                                for field in fieldList if field.isRiver
                                                and field.BasicWonderConditions()
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainIndustrialZone()]))
    wonderList.append(Wonder(WonderName.STATUE_OF_LIBERTY,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.HARBOR, distField))
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
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.isAdjacentToCity()]))
    wonderList.append(Wonder(WonderName.GREAT_ZIMBABWE,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and any(x.resource == Resource.STONE
                                                    and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                                and not field.isHills()]))
    wonderList.append(Wonder(WonderName.SYDNEY_OPERA_HOUSE,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.HARBOR, distField))
                                                for field in fieldList if field.terrain == TerrainType.COAST
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainHarbor()]))
    wonderList.append(Wonder(WonderName.TAJ_MAHAL,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and field.isRiver]))
    wonderList.append(Wonder(WonderName.TEMPLE_OF_ARTEMIS,
                            lambda fieldList, fieldListWithNearestBorders: [(field,)
                                                for field in fieldList if field.BasicWonderConditions()
                                                and any((x.resource == Resource.DEER
                                                        or x.resource == Resource.TRUFFLES
                                                        or x.resource == Resource.FURS
                                                        or x.resource == Resource.IVORY)
                                                    and x.isNeighbour(field) for x in fieldListWithNearestBorders)
                                                and not field.isHills()]))
    wonderList.append(Wonder(WonderName.TERACOTTA_ARMY,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.ENCAMPMENT, distField))
                                                for field in fieldList if field.BasicWonderConditions()
                                                and (field.terrain == TerrainType.GRASSLAND
                                                or field.terrain == TerrainType.PLAINS)
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainEncampment()]))
    wonderList.append(Wonder(WonderName.VENETIAN_ARSENAL,
                            lambda fieldList, fieldListWithNearestBorders: [(field, (DistrictName.INDUSTRIAL_ZONE, distField))
                                                for field in fieldList if field.terrain == TerrainType.COAST
                                                for distField in fieldList if distField.isNeighbour(field)
                                                and distField.canContainIndustrialZone()]))
    return wonderList
