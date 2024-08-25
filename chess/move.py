from player import Player

class Move:

    def __init__(self, player, piece_moved, src_spot, dest_slot, piece_killed):
        self.player = player
        self.piece_moved = piece_moved
        self.src_spot = src_spot
        self.dest_spot = dest_slot
        self.piece_killed = piece_killed
    
    def undo_move(self):
        self.piece_moved.rev_move(self.dest_spot, self.src_spot, self.piece_killed)
