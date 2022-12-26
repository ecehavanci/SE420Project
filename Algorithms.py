from enum import Enum
from queue import Queue
from queue import PriorityQueue


class Algorithm:
    def __init__(self, initialState, goalState, algoOrder):
        self.initialState = initialState
        self.goalState = goalState
        self.algoOrder = algoOrder
        self.expansion = []
        self.InitialTiles = []
        self.GoalTiles = []
        self.getIndexes()
        self.stepLimitCounter = 0
        self.fringe = []
        self.cost = 0

    def decideCost(self, TileColor, direction):
        if (TileColor == "red"):
            return 1
        elif (TileColor == "green"):
            return 2 if direction == direction.Vertical else 1
        elif (TileColor == "blue"):
            return 1 if direction == direction.Vertical else 2

        return 0

    def checkLeft(self, State, TilePlace):
        if ((TilePlace[1] - 1) == -1):
            return False
        leftCoordinate = [TilePlace[0], TilePlace[1] - 1]

        if (TilePlace[1] > 0 and State.findTileColorByPlace(leftCoordinate) == State.isTileColored(TilePlace)):
            return True
        return False

    def checkRight(self, State, TilePlace):
        if ((TilePlace[1] + 1) == 3):
            return False
        leftCoordinate = [TilePlace[0], TilePlace[1] + 1]

        if (TilePlace[1] < 2 and State.findTileColorByPlace(leftCoordinate) == State.isTileColored(TilePlace)):
            return True
        return False

    def checkDown(self, State, TilePlace):
        if ((TilePlace[0] + 1) == 3):
            return False
        leftCoordinate = [TilePlace[0] + 1, TilePlace[1]]

        if (TilePlace[0] < 2 and State.findTileColorByPlace(leftCoordinate) == State.isTileColored(TilePlace)):
            return True
        return False

    def checkUp(self, State, TilePlace):
        if ((TilePlace[0] - 1) == -1):
            return False
        leftCoordinate = [TilePlace[0] - 1, TilePlace[1]]

        if (TilePlace[0] < 2 and State.findTileColorByPlace(leftCoordinate) == State.isTileColored(TilePlace)):
            return True
        return False

    def getPossibleNextStates(self, State):
        print("fdfhgfhgfgdvwamk")
        if (self.stepLimitCounter == 10):
            return None

        goal_state = State(self.goalState)

        currentColor = self.algoOrder[self.tileOrder(State)]
        currentColorPlace = State.findTileColorByPlace(currentColor)

        if ((currentColorPlace[0] == goal_state.findTileColorByPlace(currentColor)[0]) and (
                currentColorPlace[1] == goal_state.findTileColorByPlace(currentColor)[1]) and not State.isEqual(
                goal_state)):
            State.setLastMovedTileColor(currentColor)
            return self.getPossibleNextStates(State)

        self.stepLimitCounter += 1

        possibleStates = []

        if (self.checkUp(State, currentColorPlace)):
            newState = State
            # Todo tonların rengi duruma göre değişecek && 90. satır
            newState.setCost(self.decideCost(currentColor, direction.Vertical))

            newState.getTiles()[currentColorPlace[0]][currentColorPlace[1]] = newState.isTileColored(newState)
            newState.getTiles()[currentColorPlace[0] - 1][currentColorPlace[1]] = currentColor
            newState.setLastMovedTile(currentColor)
            possibleStates.append(newState)

        if (self.checkDown(State, currentColorPlace)):
            newState = State
            # Todo tonların rengi duruma göre değişecek && 101. satır
            newState.setCost(self.decideCost(currentColor, direction.Vertical))

            newState.getTiles()[currentColorPlace[0]][currentColorPlace[1]] = newState.isTileColored(newState)
            newState.getTiles()[currentColorPlace[0] + 1][currentColorPlace[1]] = currentColor
            newState.setLastMovedTile(currentColor)
            possibleStates.append(newState)

        if (self.checkRight(State, currentColorPlace)):
            newState = State
            # Todo tonların rengi duruma göre değişecek && 111. satır
            newState.setCost(self.decideCost(currentColor, direction.Horizontal))

            newState.getTiles()[currentColorPlace[0]][currentColorPlace[1]] = newState.isTileColored(newState)
            newState.getTiles()[currentColorPlace[0]][currentColorPlace[1] + 1] = currentColor
            newState.setLastMovedTile(currentColor)
            possibleStates.append(newState)

        if (self.checkLeft(State, currentColorPlace)):
            newState = State
            # Todo tonların rengi duruma göre değişecek  && 121. satır
            newState.setCost(self.decideCost(currentColor, direction.Horizontal))

            newState.getTiles()[currentColorPlace[0]][currentColorPlace[1]] = newState.isTileColored(newState)
            newState.getTiles()[currentColorPlace[0]][currentColorPlace[1] - 1] = currentColor
            newState.setLastMovedTile(currentColor)
            possibleStates.append(newState)

        moves_array = []

        for i in possibleStates:
            moves_array.append(i)
        return moves_array

    def tileOrder(self, State):
        counter = 0
        for color in self.algoOrder:
            if (color == State.getLastMovedTileColor()):
                counter = counter + 1
                return 0 if counter == 3 else counter
            counter = counter + 1
        return 0

    def getIndexes(self):
        list = ["blue", "red", "green"]
        # tile i,j for entered initiaal states
        for i in range(3):
            for j in range(3):
                if str(self.initialState[i][j]["bg"]) in list:
                    self.InitialTiles.append([i, j])
        # ex: [[0,1],[2,4],[4,5]]
        for m in range(3):
            for n in range(2):
                print(self.InitialTiles[m][n])

        # tile i,j for entered goal states
        for i in range(3):
            for j in range(3):
                if self.goalState[i][j]["bg"]:
                    self.GoalTiles.append([i, j])
        # ex: [[0,1],[2,4],[4,5]]
        for m in range(3):
            for n in range(2):
                print(self.GoalTiles[m][n])

    def fringePush(self, state):
        if (len(self.fringe) == 25):
            for i in self.fringe:
                if i > self.cost:
                    self.cost = i
        self.fringe.append(state)          #Todo haven't completed here yet

    def fringePop(self):
        return self.fringe.pop()

    def A_StarSearch(self, path):
        print("A* cost")

        self.cost = 0
        for state in path:
            self.cost += state.getCost()
        self.cost = self.cost + self.h(path) #Todo haven't completed here yet
        return self.cost

    def h(self, state):
        self.cost = 0
        redTileC = []
        redTileG = []
        greenTileC = []
        greenTileG = []
        blueTileC = []
        blueTileG = []

        redTileG = state.findTilePlaceByColor("red")
        greenTileG = state.findTilePlaceByColor("green")
        blueTileG = state.findTilePlaceByColor("blue")

        redTileC = state.findTilePlaceByColor("red")
        greenTileC = state.findTilePlaceByColor("green")
        blueTileC = state.findTilePlaceByColor("blue")

        return self.cost



    def UniformCost(self, path):
        print("uniform cost")
        self.cost = 0
        for state in path:
            self.cost += state.getCost()
        return self.cost


class direction(Enum):
    Horizontal = 1
    Vertical = 2





