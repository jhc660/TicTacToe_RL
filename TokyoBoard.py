import cardDeck

class TokyoBoard():
    def __init__(self):
        self.stations = []
        self.trainLines = []
        self.trainLines.append(TrainLine(2,2))
        self.trainLines[0].addStations(self.stations, 11)
        
        self.trainLines.append(TrainLine(2,4))
        self.trainLines[1].addStation(self.trainLines[0].stations[0])
        self.trainLines[1].addStation(self.trainLines[0].stations[1])
        self.trainLines[1].addStation(self.trainLines[0].stations[2])
        self.trainLines[1].addStation(self.trainLines[0].stations[3])
        self.trainLines[1].addStation(self.trainLines[0].stations[4])
        self.trainLines[1].addStation(self.trainLines[0].stations[5])
        self.trainLines[1].addStations(self.stations, 8)
        
        self.trainLines.append(TrainLine(3,7))
        self.trainLines[2].addStations(self.stations, 3)
        self.trainLines[2].addStation(self.trainLines[1].stations[7])
        self.trainLines[2].addStations(self.stations, 10)
        
        self.trainLines.append(TrainLine(3,5))
        self.trainLines[3].addStations(self.stations, 4)
        self.trainLines[3].addStation(self.trainLines[0].stations[8])
        self.trainLines[3].addStations(self.stations, 1)
        self.trainLines[3].addStation(self.trainLines[1].stations[9])
        self.trainLines[3].addStations(self.stations, 3)
        self.trainLines[3].addStation(self.trainLines[2].stations[5])
        self.trainLines[3].addStations(self.stations, 4)
        self.trainLines[3].addStation(self.trainLines[0].stations[5])
        
        self.trainLines.append(TrainLine(3,4))
        self.trainLines[4].addStations(self.stations, 1)
        self.trainLines[4].addStation(self.trainLines[0].stations[9])
        self.trainLines[4].addStations(self.stations, 2)
        self.trainLines[4].addStation(self.trainLines[3].stations[7])
        self.trainLines[4].addStation(self.trainLines[3].stations[8])
        self.trainLines[4].addStation(self.trainLines[1].stations[10])
        self.trainLines[4].addStation(self.trainLines[2].stations[5])
        self.trainLines[4].addStation(self.trainLines[3].stations[11])
        self.trainLines[4].addStations(self.stations, 5)
        
        self.trainLines.append(TrainLine(2,4))
        self.trainLines[5].addStation(self.trainLines[0].stations[10])
        self.trainLines[5].addStation(self.trainLines[4].stations[2])
        self.trainLines[5].addStations(self.stations, 1)
        self.trainLines[5].addStation(self.trainLines[1].stations[9])
        self.trainLines[5].addStation(self.trainLines[2].stations[4])
        self.trainLines[5].addStations(self.stations, 1)
        self.trainLines[5].addStation(self.trainLines[2].stations[5])
        self.trainLines[5].addStations(self.stations, 4)
        
        self.trainLines.append(TrainLine(2,5))
        self.trainLines[6].addStation(self.trainLines[5].stations[0])
        self.trainLines[6].addStation(self.trainLines[5].stations[1])
        self.trainLines[6].addStation(self.trainLines[5].stations[2])
        self.trainLines[6].addStation(self.trainLines[5].stations[3])
        self.trainLines[6].addStation(self.trainLines[3].stations[7])
        self.trainLines[6].addStations(self.stations, 1)
        self.trainLines[6].addStation(self.trainLines[3].stations[9])
        self.trainLines[6].addStation(self.trainLines[2].stations[6])
        self.trainLines[6].addStation(self.trainLines[5].stations[7])
        self.trainLines[6].addStations(self.stations, 4)
        
        self.trainLines.append(TrainLine(3,6))
        self.trainLines[7].addStations(self.stations, 3)
        self.trainLines[7].addStation(self.trainLines[3].stations[8])
        self.trainLines[7].addStation(self.trainLines[1].stations[10])
        self.trainLines[7].addStation(self.trainLines[3].stations[9])
        self.trainLines[7].addStations(self.stations, 2)
        self.trainLines[7].addStation(self.trainLines[2].stations[7])
        self.trainLines[7].addStations(self.stations, 1)
        self.trainLines[7].addStation(self.trainLines[6].stations[9])
        self.trainLines[7].addStation(self.trainLines[6].stations[10])
        self.trainLines[7].addStations(self.stations, 1)
        self.trainLines[7].addStation(self.trainLines[4].stations[12])
        
        self.trainLines.append(TrainLine(3,4))
        self.trainLines[8].addStations(self.stations, 3)
        self.trainLines[8].addStation(self.trainLines[3].stations[7])
        self.trainLines[8].addStation(self.trainLines[3].stations[6])
        self.trainLines[8].addStation(self.trainLines[3].stations[5])
        self.trainLines[8].addStation(self.trainLines[1].stations[8])
        self.trainLines[8].addStation(self.trainLines[1].stations[7])
        self.trainLines[8].addStation(self.trainLines[3].stations[13])
        self.trainLines[8].addStations(self.stations, 4)

    def __str__(self):
        string = ''
        for trainLine in self.trainLines:
            string+=str(trainLine)+'\n'
        return string

    def getState(self):
        state = ''
        for trainLine in self.trainLines:
            state += trainLine.getState()
        for station in self.stations:
            state += station.getState()
        return state

    def getValidMoves(self):
        moves = []
        for i in range(len(self.trainLines)):
            if trainLine[i].maxCars > cars:
                moves.append[i]
        return moves

    def makeMove(self, line, card):
        if card == '2':
            advanceLine(line, 2, 'normal')
        if card == '3':
            advanceLine(line, 2, 'normal')
        if card == '4':
            advanceLine(line, 4, 'normal')
        if card == '5':
            advanceLine(line, 5, 'normal')
        if card == '6':
            advanceLine(line, 6, 'normal')
        if card == 's':
            advanceLine(line, 1, 'star')
        if card == 'c2':
            advanceLine(line, 2, 'circle')
        if card == 'c3':
            advanceLine(line, 3, 'circle')

    def advanceLine(self, line, number, cardType):
        if self.trainLines[line].maxCars > self.trainLines[line].cars:
            self.trainLines[line].advance(number, cardType)

    def gameOver(self):
        gameOver = False
        emptyStations = 0
        for trainLine in self.trainLines:
            emptyStations += trainLine.maxCars - cars
        if emptyStations == 0:
            gameOver = True
        return gameOver
        

    def calculateScore(self):
        return 0
            

class TrainLine():
    def __init__(self, cars, points):
        self.maxCars = cars
        self.cars = 0
        self.points = points
        self.stations = []

    def addStation(self, trainStation):
        self.stations.append(trainStation)
        trainStation.connections+=1

    def addStations(self, stationList, times):
        while times > 0:
            times-=1
            trainStation = TrainStation()
            stationList.append(trainStation)
            self.stations.append(trainStation)

    def __str__(self):
        printValue = 'Points: '+ str(self.points) + ' '
        for station in self.stations:
            if station.fill == 'Empty':
                printValue+='[ ]'
            elif station.fill == 'Star':
                printValue+='['+str(2*station.connections)+']'
            else:
                printValue+='[X]'
        return printValue

    def getState(self):
        state = str(self.cars)
        return state

    def advance(self, number, cardType):
        self.cars += 1
        advancesLeft = number
        startedAdvance = False
        for station in self.stations:
            if station.fill == 'Empty':
                startedAdvance = True
                advancesLeft-=1
                if cardType == 'star':
                    station.fill = 'Star'
                else:
                    station.fill = 'Filled'
                if advancesLeft == 0:
                    break
            else:
                if startedAdvance and cardType != 'circle':
                    break

class TrainStation():
    def __init__(self):
        self.fill = 'Empty'
        self.connections = 1
        
    def getState(self):
        state = '0'
        if self.fill == 'Filled':
            state = '1'
        elif self.fill == 'Star':
            state = '2'
        return state

def testRoutine():
    tokyoBoardTest = TokyoBoard()
    print(tokyoBoardTest.getState())
    tokyoBoardTest.advanceLine(4, 6, 'normal')
    tokyoBoardTest.advanceLine(5, 2, 'circle')
    tokyoBoardTest.advanceLine(5, 1, 'star')
    print(tokyoBoardTest)
    print(tokyoBoardTest.getState())

#testRoutine()