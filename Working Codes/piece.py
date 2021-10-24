class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        self.neighbors = []

    def is_Bomb(self):
        return self.hasBomb

    def is_clicked(self):
        return self.clicked

    def is_flagged(self):
        return self.flagged
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
   
    def setNumAround(self):
        self.numAround  = 0
        for neighbor in self.neighbors:
            if neighbor.is_Bomb:
                self.numAround += 1
        return self.numAround
        
    def getNumAround(self):
        return self.setNumAround()
    

    def getNeighbors(self):
        return self.neighbors

    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True

    def getNeighbors(self):
        return self.neighbors
