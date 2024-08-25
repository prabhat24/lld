from game_manager import GameManager


game_manager = GameManager.get_instance()

game, game_id = game_manager.create_game()

game.play()
