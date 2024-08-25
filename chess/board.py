from slots import Slot
from piece import *

class Board:

    def __init__(self):
        self.slots =  [ ([None,] * 8)  for i in range(0, 8) ]
        
        for j in range(0, 8):
            for i in range(0, 8):
                slot = Slot(i, j)
                self.slots[j][i] = slot
                slot = None

    def reset_board(self):

        for i in range(0, 8):
            self.get_slot(i, 1).set_piece(PawnPiece(is_white=True))
            self.get_slot(i, 6).set_piece(PawnPiece())


        self.get_slot(0, 0).set_piece(RookPiece(is_white=True))
        self.get_slot(7, 0).set_piece(RookPiece(is_white=True))
        self.get_slot(0, 7).set_piece(RookPiece())
        self.get_slot(7, 7).set_piece(RookPiece())


        self.get_slot(1, 0).set_piece(KnightPiece(is_white=True))
        self.get_slot(6, 0).set_piece(KnightPiece(is_white=True))
        self.get_slot(1, 7).set_piece(KnightPiece())
        self.get_slot(6, 7).set_piece(KnightPiece())

        self.get_slot(2, 0).set_piece(BishopPiece(is_white=True))
        self.get_slot(5, 0).set_piece(BishopPiece(is_white=True))
        self.get_slot(2, 7).set_piece(BishopPiece())
        self.get_slot(5, 7).set_piece(BishopPiece())

        self.get_slot(3, 0).set_piece(QueenPiece(is_white=True))
        self.get_slot(4, 0).set_piece(KingPiece(is_white=True))
        self.get_slot(3, 7).set_piece(QueenPiece())
        self.get_slot(4, 7).set_piece(KingPiece())

    def print(self):
        for j in range(7, -1, -1):
            for i in range(0, 8):
                print(self.get_slot(i, j).display(), end="")
            print()
            

    def get_slot(self, x, y) -> Slot:
        return self.slots[y][x]
