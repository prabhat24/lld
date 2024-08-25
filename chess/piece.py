from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, is_white=False):
        self.is_killed = False
        self.is_white = is_white

    def kill_piece(self):
        self.is_killed = True
    
    def can_move(self, player, src_slot, dest_slot):
        if player.is_white != self.is_white:
            raise CannotMoveOppositeTeamPiece("cannot move opposite team's piece")
        if not (0 >= dest_slot.get_x() <= 7) and (0 >= dest_slot.get_y() <= 7):
            raise MoveOutOfBoardBounds("please make sure that destination spot is inside board")
        return True
    
    def move(self, player, src_spot, dest_slot):
        """
        return
        killed_piece
        """
        src_spot.set_piece(None)
        killed_piece = dest_slot.get_piece()
        dest_slot.set_piece(self)
        return killed_piece

    def rev_move(self, src_spot, dest_spot, piece_killed):
        current_piece = src_spot.get_piece()
        dest_spot.set_piece(current_piece)
        src_spot.set_piece(piece_killed)


    @abstractmethod
    def get_symbol(self):
        pass

class PawnPiece(Piece):
    def get_symbol(self):
        if self.is_white:
            return " ♙ "
        return " ♟ "

    def can_move(self, player, src_slot, dest_slot):
        if super().can_move(player, src_slot, dest_slot):
            # check dest move is inside the board
            jump_y = dest_slot.get_y() - src_slot.get_y() if self.is_white else src_slot.get_y() - dest_slot.get_y()
            jump_x = abs(dest_slot.get_x() - src_slot.get_x())
            print("jumpx", "jumpy", jump_x, jump_y)
            if jump_x:
                print("1")
                return self.validate_kill_moves(jump_x, jump_y, dest_slot)

            elif jump_y == 2:
                print("2")
                return self.validate_first_move(jump_x, src_slot)
            else:
                print("3")
                return self.validate_basic_move(jump_x, jump_y)

        return False
    
    def validate_kill_moves(self, jump_x, jump_y, dest_slot):
        try:
            if not (jump_x == 1 and jump_y == 1 and dest_slot.get_piece().is_white != self.is_white):
                return False
        except Exception as e:
            raise WrongMove("cannot move pawn there, No opponent piece present")
        return True

    def validate_first_move(self, jump_x, src_slot):
        if jump_x == 0 and self.is_starting_slot(src_slot):
            return True
        return False
    
    def validate_basic_move(self, jump_x, jump_y):
        if jump_x == 0 and jump_y == 1:
            return True
        return False
        

    def is_starting_slot(self, src_slot):
        # print("src_slot.get_y" , src_slot.get_y(),  self.is_white, src_slot.get_y == 1 and self.is_white, type(src_slot.get_y()) )
        if src_slot.get_y() == 1 and self.is_white:
            print("h2here 80")
            return True
        elif src_slot.get_y() == 6 and not self.is_white:
            return True
        return False

class BishopPiece(Piece):
    
    def get_symbol(self):
        if self.is_white:
            return " ♗ "
        return " ♝ "

    def can_move(self, player, src_slot, dest_slot):
        if super().can_move(player, src_slot, dest_slot):
            return True
        return False

class KnightPiece(Piece):
    
    def get_symbol(self):
        if self.is_white:
            return " ♘ "
        return " ♞ "

    def can_move(self, player, src_slot, dest_slot):
        if super().can_move(player, src_slot, dest_slot):
            return True
        return False

class RookPiece(Piece):
    
    def get_symbol(self):
        if self.is_white:
            return " ♖ "
        return " ♜ "

    def can_move(self, player, src_slot, dest_slot):
        if super().can_move(player, src_slot, dest_slot):
            return True
        return False

class QueenPiece(Piece):
    
    def get_symbol(self):
        if self.is_white:
            return " ♕ "
        return " ♛ "
    
    def can_move(self, player, src_slot, dest_slot):
        if super().can_move(player, src_slot, dest_slot):
            return True
        return False

class KingPiece(Piece):
    
    def get_symbol(self):
        if self.is_white:
            return " ♔ "
        return " ♚ "
    
    def can_move(self, player, src_slot, dest_slot):
        if super().can_move(player, src_slot, dest_slot):
            return True
        return False
    

class CannotMoveOppositeTeamPiece(Exception):
    pass

class MoveOutOfBoardBounds(Exception):
    pass

class WrongMove(Exception):
    pass