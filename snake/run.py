from game_runner import GameRunner
from player import Player
from tkinter import *

if __name__ == "__main__":

    root = Tk()
    root.title("Snake")

    player = Player(root)

    gm = GameRunner(10)
    gm.register_player(player)
    gm.run(root)
