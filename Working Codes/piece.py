class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False

    def is_Bomb(self):
        return self.hasBomb

    def is_clicked(self):
        return self.clicked

    def is_flagged(self):
        return self.flagged

    