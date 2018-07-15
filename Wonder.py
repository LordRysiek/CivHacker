from enum import Enum

class Wonder:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def WhereCanItBeBuilt(self, fieldList, fieldListWithNearestBorders):
        return self.function(fieldList, fieldListWithNearestBorders)
        #returns list in form [(fieldIndex, districtsList)],
        #where districtsList is a list of tuples(districtName, districtFieldIndex)

class WonderName(Enum):
    ALHAMBRA = 1
    AMUNDSEN_SCOTT_RESEARCH_STATION = 2
    ANGKOR_WAT = 3
    APADANA = 4
    BIG_BEN = 5
    BOLSHOI_THEATRE = 6
    BROADWAY = 7
    CASA_DE_CONTRARACION = 8
    CHICHEN_ITZA = 9
    COLOSSEUM = 10
    COLOSSUS = 11
    CRISTO_REDENTOR = 12
    EIFFEL_TOWER = 13
    ESTADIO_DO_MARACANA = 14
    FORBIDDEN_CITY = 15
    GREAT_LIBRARY = 16
    GREAT_ZIMBABWE = 17
    HAGIA_SOPHIA = 18
    HANGING_GARDENS = 19
    HERMITAGE = 20
    HUEY_TEOCALLI = 21
    JEBEL_BARKAL = 22
    KILWA_KISIWANI = 23
    KOTOKU_IN = 24
    MAHABODHI_TEMPLE = 25
    MAUSOLEUM_AT_HALICARNASSUS = 26
    MONT_ST_MICHEL = 27
    ORACLE = 28
    OXFORD_UNIVERSITY = 29
    PETRA = 30
    POTALA_PALACE = 31
    PYRAMIDS = 32
    RUHR_VALLEY = 33
    STATUE_OF_LIBERTY = 34
    ST_BASILS_BATHEDRAL = 35
    STONEHENGE = 36
    SYDNEY_OPERA_HOUSE = 37
    TAJ_MAHAL = 38
    TEMPLE_OF_ARTEMIS = 39
    TERACOTTA_ARMY = 40
    VENETIAN_ARSENAL = 41
    GREAT_LIGHTHOUSE = 42
    NONE = 43

class DistrictName(Enum):
    CAMPUS = 1
    HOLY_SITE = 2
    THEATER_SQUARE = 3
    ENCAMPMENT = 4
    HARBOR = 5
    COMMERCIAL_HUB = 6
    INDUSTRIAL_ZONE = 7
    ENTERTAINMENT_COMPLEX = 8
    AQUEDUCT = 9
    AERODROME = 10
    SPACEPORT = 11
    GOVERMENT_PLAZA = 12
    WATER_PARK = 13
    NONE = 14
