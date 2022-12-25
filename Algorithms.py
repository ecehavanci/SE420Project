from queue import Queue
from queue import PriorityQueue


class Algorithm:
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState
        self.InitialTiles = []
        self.GoalTiles = []
        self.getIndexes()

    def getIndexes(self):
        # tile i,j for entered initiaal states
        for i in range(3):
            for j in range(3):
                if self.initialState[i][j]["bg"]:
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

    def A_StarSearch(self):
        fringe = PriorityQueue()

    def UniformCost(self):
        print("uniform cost")
