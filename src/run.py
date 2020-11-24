"""Module run.py, starts the program.
"""
from services.game_state import GameState

if __name__ == "__main__":
    game_state = GameState()
    game_state.run()
