class State:
    def __init__(self, initialTiles):  # current & next move
        self.initialTiles = initialTiles
        self.cost = 0
        self.lastMovedTileColor = ""

    def setCost(self, cost):
        self.cost = cost

    def getCost(self):
        return self.cost

    def setLastMovedTileColor(self, lastMovedTileColor):
        self.lastMovedTileColor = lastMovedTileColor

    def getLastMovedTileColor(self):
        return self.lastMovedTileColor

    def isEqual(self, State):
        for i in range(3):
            for j in range(3):
                if (self.initialTiles[i][j] != State.initialTiles[i][j]):
                    return False
        return True

    def getTiles(self):
        return self.initialTiles

    def findTilePlaceByColor(self, TileColor):
        # tile i,j for entered initial states
        for i in range(3):
            for j in range(3):
                if str(self.initialTiles[i][j]["bg"]) == TileColor:
                    return [i, j]
        return 0

    def isTileColored(self, TilePlace):   #coordinate
        list = ["blue", "red", "green"]
        # tile i,j for entered initiaal states
        for i in range(3):
            for j in range(3):
                if str(self.initialTiles[TilePlace[i]][TilePlace[j]]["bg"]) in list:
                    return False
        return True

    def findTileColorByPlace(self, TilePlace):
        return self.initialTiles[TilePlace[0]][TilePlace[1]]

    def setTiles(self, Tiles):
        self.initialTiles = Tiles
