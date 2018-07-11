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
wonderList.append(Wonder(WonderName.ALHAMBRA, lambda fieldList: [(field, (DistrictName.ENCAMPMENT, distField))
                                                        for field in fieldList if field.isHills() is True
                                                    for distField in fieldList if distField.isNeighbour(field)
                                                    and distField.canContainEncampment() is True]))
wonderList.append(Wonder(WonderName.AMUNDSEN_SCOTT_RESEARCH_STATION,
                        lambda fieldList: [(field, (DistrictName.CAMPUS, distField))
                                            for field in fieldList if field.terrain == TerrainType.SNOW or
                                            field.terrain == TerrainType.SNOW_HILLS is True
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainCampus() is True]))
wonderList.append(Wonder(WonderName.ANGKOR_WAT,
                        lambda fieldList: [(field, (DistrictName.AQUEDUCT, distField))
                                            for field in fieldList if field.BasicWonderConditions()
                                            for distField in fieldList if distField.isNeighbour(field)
                                            and distField.canContainAqueduct(fieldListWithNearestBorders) is True]))

print([(field[0].terrain,field[0].x,field[0].y) for field in wonderList[2].WhereCanItBeBuilt(fieldList)])
