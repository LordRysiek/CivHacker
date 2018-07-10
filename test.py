from Field import Field

field1 = Field(1,1)
field2 = Field(2,2)
field3 = Field(2,3)
field4 = Field(1,1)
print(field1.isNeighbour(field2))
print(field1.isNeighbour(field3))
print(field2.isNeighbour(field3))
print(field1.isNeighbour(field4))
