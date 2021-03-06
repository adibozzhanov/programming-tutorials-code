from view_handler import ViewHandler
from snake import Snake
from tkinter import *
import time
from random import randint


# grid[y][x] == 0 - nothing
# grid[y][x] == 1 - snake
# grid[y][x] == 2 - food
# food
class GameRunner:
    def __init__(self, width):
        self.grid = [[0 for i in range(width)] for i in range(width)]
        self.width = width

    def spawn_snake(self):
        self.snake = Snake(self.width // 2, self.width // 2)
        for x, y in self.snake.body:
            self.grid[y][x] = 1

    def calculate_coord(self, x, y, move):
        new_x = x
        new_y = y

        if move == "UP":
            new_y -= 1
        elif move == "LEFT":
            new_x -= 1
        elif move == "RIGHT":
            new_x += 1
        elif move == "DOWN":
            new_y += 1

        new_x %= self.width
        new_y %= self.width
        return new_x, new_y

    def spawn_food(self):
        check = False
        while not check:
            x = randint(0, 4)
            y = randint(0, 4)
            if self.grid[x][y] != 1:
                self.grid[x][y] = 2
                check = True
                print("(spawning) EAT ME!")

    def register_player(self, player):
        self.player = player

    def run(self, root):

        # i added a comment
        vh = ViewHandler(root, width=500, height=500)

        # one more comment

        alive = True
        self.spawn_snake()
        self.spawn_food()
        self.spawn_food()

        while alive:
            move = self.player.make_move(self.grid, self.snake.body[0])
            x, y = self.snake.body[0]
            new_x, new_y = self.calculate_coord(x, y, move)

            point = self.grid[new_y][new_x]

            if point == 0:
                tail_x, tail_y = self.snake.move(new_x, new_y)
                self.grid[new_y][new_x] = 1
                self.grid[tail_y][tail_x] = 0

            if point == 1:
                alive = False

            if point == 2:
                self.snake.move(new_x, new_y, True)
                self.grid[new_y][new_x] = 1

            time.sleep(0.1)
            vh.draw_grid(self.grid)
