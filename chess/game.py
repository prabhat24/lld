from board import Board
from enum import Enum
from player import Player
from move import Move
from piece import CannotMoveOppositeTeamPiece, Piece
from collections import deque

class GameStatus(Enum):
    ACTIVE = "ACTIVE"
    ENDED = "ENDED"
    CANCELLED = "CANCELLED"

class Game:

    def __init__(self, player1, player2):
        
        # TODO make sure player1 is always 1st one in the list
        self.active_player: Player = player1
        self.players: list[Player] = [player1, player2]
        self.board = Board()
        self.board.reset_board()
        self.moves_stack = deque()
        self.status = GameStatus.ACTIVE
        self.move_cnt = 0


    def move_request(self, player, src, dest):
        try:
            self.process_move(player, src, dest)
            self.move_cnt += 1
            self.active_player = self.players[self.move_cnt % 2]
        except (InvalidMove, CannotMoveOppositeTeamPiece) as im:
            print(im)
        except NoPieceSelectedForMove as nps:
            print(nps)
        


    def process_move(self, player, src, dest):
        srcx, srcy = get_system_coodinates_from_chess_coodinates(src)
        destx, desty = get_system_coodinates_from_chess_coodinates(dest)
        print("src", srcx, srcy)
        print("destr", destx, desty)
        src_spot = self.board.get_slot(srcx, srcy)
        dest_spot = self.board.get_slot(destx, desty)
        src_piece = src_spot.get_piece()
        if not src_piece:
            raise NoPieceSelectedForMove("Please select the piece for movement")
        if not src_piece.can_move(player, src_spot, dest_spot):
            raise InvalidMove("Move is invalid")
        print(player)
        self.make_move(
                player=player, 
                src=src_spot,
                current_piece=src_piece,
                dest=dest_spot)
        
    def make_move(self, player, current_piece: Piece, src, dest):
        killed_piece = current_piece.move(player, src, dest)
        move = Move(player, current_piece, src, dest, killed_piece)
        self.moves_stack.append(move)
        print("move complete")
        return True

    def undo_move(self):
        try:
            last_move = self.moves_stack.pop()
            last_move.undo_move()
            self.move_cnt -= 1
            self.active_player = self.players[self.move_cnt % 2]
            print("move complete")
        except IndexError as e:
            print("no moves to undo")

    def play(self):
        print("Game started")
        

        action = None
        while action != "q":
            self.board.print()
            print("whites Move!!" if self.active_player.is_white else "Blacks Move!!")

            action = input("enter move <source_move>-<dest_move>")
            if action == "u":
                self.undo_move()
            if action == "q":
                self.status = GameStatus.ENDED
                print("game interputted by user")
                raise SystemExit()
            if "-" in action:
                src, dest = action.split("-")
                self.move_request(self.active_player, src, dest)
                



def get_system_coodinates_from_chess_coodinates(coordinate: str) -> tuple:
    return ord(coordinate[0].lower()) - 97  , int(coordinate[1]) - 1


class InvalidMove(Exception):
    pass

class NoPieceSelectedForMove(Exception):
    pass