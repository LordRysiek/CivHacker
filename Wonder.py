from enum import Enum

class Wonder:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def CanItBeBuilt(self, fieldsList, field):
        return function(fields, field)

    def WhereCanItBeBuilt(self, fieldsList):
        indexes = []
        for i in range(len(fieldsList)):
            if self.CanItBeBuilt(self, fieldsList, fieldsList[i]):
                indexes.append(i)
        return indexes

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

#http://civilization.wikia.com/wiki/Wonder_(Civ6)
#
