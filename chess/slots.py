from piece import *

class Slot:


    def __init__(self, x , y):
        self.piece: Piece = None
        self.x = x
        self.y = y

    def get_slot_name(self):
        return f"{chr(self.x + 97)}{self.y + 1}" 
    
    def set_piece(self, piece: Piece):
        self.piece = piece

    def display(self):
        if not self.piece:
            return " - "
        return self.piece.get_symbol()

    def get_piece(self):
        return self.piece
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y