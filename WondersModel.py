class WondersModel:
    """
    using modified Ford-Fulkerson algorithm for biparite graphs
    """
    def __init__(self, wonderList, fieldList, fieldListWithNearestBorders):
        allPlacements = []
        self.possiblePlacements = []
        self.impossiblePlacements = []
        self.chosenPlacements = []
        self.FFCurrentMatching = [-1 for x in range(36)]
        self.FFCurrentCombinations = []
        self.FFCurrentCombinationsPossibleMatchingSets = []
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
        self.UpdateCurrentlyPossiblePlacements(placement)
    #private
    def FindPlacement(self, wonderName, list):
        for x in list:
            if x[0] == wonderName:
                return x
        return 0

    def UpdateCurrentlyPossiblePlacements(self, placement):
        newCombinationIndex = -1
        if len(placement) == 1:
            newCombinationIndex = len(self.FFCurrentCombinations)
            self.FFCurrentCombinations.append(placement)
            self.FFCurrentCombinationsPossibleMatchingSets.append([fieldPair[0] for fieldPair in placement[1]])
        elif len(placement) == 2:
            for i in range(len(self.FFCurrentCombinations)):
                if(self.FFCurrentCombinations[i][1][1][0] == placement[1][0]):
                    self.FFCurrentMatching[:] = [x for x in self.FFCurrentMatching
                                                            if x is not i]
                    self.FFCurrentCombinations[i].append(placement)
                    newCombinationIndex = i
                    self.FFCurrentCombinationsPossibleMatchingSets[newCombinationIndex] =\
                        self.FindPossibleMatchingSets(self.FFCurrentCombinations[newCombinationIndex])
                    break
            if newCombinationIndex == -1:
                newCombinationIndex = len(self.FFCurrentCombinations)
                self.FFCurrentCombinations.append(placement)
                self.FFCurrentCombinationsPossibleMatchingSets.append([[fieldPair[0], fieldPair[1]] for
                                                                            fieldPair in placement[1]])
        else:
            raise NameError('Got a placement of zero or more than two length')

    def FindPossibleMatchingSets(self, combination):
        possibleDistrictFields = [fieldPair[1] for fieldPair in combination[0][1]]
        for placement in combination:
            districtFieldsToRemove = []
            for pdf in possibleDistrictFields:
                for districtField in [fieldPair[1] for fieldPair in placement[1]]:
                    if districtField == pdf:
                        break
                districtFieldsToRemove.append(pdf)
            possibleDistrictFields = [pdf for pdf in possibleDistrictFields if pdf not in districtFieldsToRemove]

        possibleMatchingSets = []
        for pdf in possibleDistrictFields:
            combinationFieldsForPdf = []
            for placement in combination:
                combinationFieldsForPdf.append(placement[0], [fieldPair[0] for fieldPair in placement[1] if fieldPair[1] is pdf])
            chosenFields = []
            visitedFields = [0 for x in range(len(combination))]
            i = 0
            while True:
                if i == len(combination):
                    chosenFields.append(pdf)
                    possibleMatchingSets.append(chosenFields)
                    chosenFields.pop()
                    chosenFields.pop()
                    i = i-1
                    continue
                if len(combinationFieldsForPdf[i][1]) == visitedFields[i]:
                    if i==0:
                        break
                    chosenFields.pop()
                    i = i-1
                    continue
                chosenFields.append(combinationFieldsForPdf[i][1][visitedFields[i]])
                visitedFields[i] = visitedFields[i] + 1
                i = i+1
        return possibleMatchingSets
