from player import Player
from game import Game

class GameManager:

    __instance = None

    def __init__(self):
        if self.__instance:
            raise Exception("Singleton Class: directly call const is not allowed")
        self.games_list = []
        GameManager.__instance = self
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls()
        return cls.__instance


    def create_game(self):
        player1 = Player(is_white=True)
        player2 = Player()
        game = Game(player1, player2)
        self.games_list.append(game)
        return game, len(self.games_list)

    