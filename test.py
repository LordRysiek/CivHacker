from Field import Field
from enums import TerrainType
from enums import TerrainFeature
from enums import NaturalWonder
from enums import Resource
from enums import WonderName
from enums import DistrictName
from WonderModel import WonderModel

fieldListWithNearestBorders = []
for x in range(0,9):
    for y in range(max(0,x-4), 9-abs(4-x)+max(0,x-4)):
        field = Field(x,y)
        field.Randomise()
        fieldListWithNearestBorders.append(field)
fieldList = [field for field in fieldListWithNearestBorders if field.x is not 0 and
            field.x is not 8 and field.y is not 0 and field.y is not 8 and
            field.y - field.x < 4 and field.x-field.y < 4]
"""
for field in fieldListWithNearestBorders:
    print("_________")
    print(field.x)
    print(field.y)
    print(field.terrain)
    print(field.feature)
    print(field.naturalWonder)
    print(field.resource)
"""
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
wonderList = [name for name in WonderName if name is not WonderName.NONE]
wmodel = WonderModel(wonderList, fieldList, fieldListWithNearestBorders)
for pair in wmodel.nextWonders:
    print(pair, wmodel.nextWonders[pair])
#print(wmodel.GetCurrentlyPossibleWonders())
#print(wmodel.GetImpossibleWonders())
#wmodel.ChooseWonder(WonderName.ALHAMBRA)
#wmodel.ChooseWonder(WonderName.KOTOKU_IN)
