class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        self.questioned = False
        self.cleared = False
        self.lockedStatus = False
        self.opened = False
        self.rClicksNumber = 1

    def is_Bomb(self):
        return self.hasBomb

    def is_clicked(self):
        return self.clicked

    def is_flagged(self):
        return self.flagged

    def is_questioned(self):
        return self.questioned
    
    def is_cleared(self):
        return self.cleared

    def click(self):
        self.clicked = True
        return self.clicked

    def makeFlag(self):
        self.flagged = True
        self.rClicksNumber = 2
        return self.flagged
    
    def makeQuestion(self):
        self.flagged = False
        self.questioned = True
        self.rClicksNumber = 3
        return self.questioned

    def clear(self):
        self.questioned = False
        self.cleared = True
        self.rClicksNumber = 1
        return self.cleared

    def get_rClicksNumber(self):
        return self.rClicksNumber

    def lock(self):
        self.lockedStatus = True
        return self.lockedStatus

    def is_locked(self):
        return self.lockedStatus

    def isOpened(self):
        return self.opened
    
    def openIt(self):
        self.opened = True
        return self.opened

    def makeNoBomb(self):
        self.hasBomb = False
        return self.hasBomb