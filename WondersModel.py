class WondersModel:
    def __init__(self, wonderList, fieldList, fieldListWithNearestBorders):
        allPlacements = []
        self.possiblePlacements = []
        self.impossiblePlacements = []
        self.chosenPlacements = []
        for wonder in wonderList:
            allPlacements.append((wonder.name, wonder.WhereCanItBeBuilt(fieldList, fieldListWithNearestBorders)))
        for placement in allPlacements:
            if placement[1]:
                self.possiblePlacements.append(placement)
            else:
                self.impossiblePlacements.append(placement)
        self.currentlyPossiblePlacements = self.possiblePlacements

    def GetCurrentlyPossibleWonders(self):
        return [placement[0] for placement in self.currentlyPossiblePlacements]

    def GetCurrentlyImpossibleWonders(self):
        return [placement[0] for placement in self.possiblePlacements if placement not in self.currentlyPossiblePlacements]

    def GetImpossibleWonders(self):
        return [placement[0] for placement in self.impossiblePlacements]

    def ChooseWonder(self, wonderName):
        placement = self.FindPlacement(wonderName, self.possiblePlacements)
        if not placement:
            raise NameError('Tried to choose wonder that was not possible to choose')
        self.chosenPlacements.append(placement)
        self.currentlyPossiblePlacements.remove(placement)
        self.UpdateCurrentlyPossiblePlacements()
    #private
    def FindPlacement(self, wonderName, list):
        for x in list:
            if x[0] == wonderName:
                return x
        return 0

    def UpdateCurrentlyPossiblePlacements(self):
        pass
