from Field import Field
from Field import TerrainType
from Field import TerrainFeature
from Field import NaturalWonder
from Field import Resource
from Wonder import Wonder
from Wonder import WonderName
from Wonder import DistrictName
from WonderListGenerator import GenerateWonderList
from WondersModel import WondersModel

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
wonderList = GenerateWonderList()
wmodel = WondersModel(wonderList, fieldList, fieldListWithNearestBorders)
#print(wmodel.GetCurrentlyPossibleWonders())
#print(wmodel.GetImpossibleWonders())
wmodel.ChooseWonder(WonderName.ALHAMBRA)
wmodel.ChooseWonder(WonderName.KOTOKU_IN)
wmodel.ChooseWonder(WonderName.HAGIA_SOPHIA)
wmodel.ChooseWonder(WonderName.MAHABODHI_TEMPLE)
