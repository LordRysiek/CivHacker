class WondersModel:
    def __init__(self, wonderList, fieldList, fieldListWithNearestBorders):
        allPlacements = []
        self.possiblePlacements = []
        self.impossiblePlacements = []
        for wonder in wonderList:
            allPlacements.append((wonder.name, wonder.WhereCanItBeBuilt(fieldList, fieldListWithNearestBorders)))
        for placement in allPlacements:
            if placement[1]:
                self.possiblePlacements.append(placement)
            else:
                self.impossiblePlacements.append(placement)
        self.currentlyPossiblePlacements = self.possiblePlacements

    def GetCurrentlyPossibleWonders(self):
        return [placement[0].name for placement in self.currentlyPossiblePlacements]

    def GetCurrentlyImpossibleWonders(self):
        return [placement[0].name for placement in self.possiblePlacements if placement not in self.currentlyPossiblePlacements]

    def GetImpossibleWonders(self):
        return [placement[0].name for placement in self.impossiblePlacements]

    def ChooseWonder(self, wonderName):
        
