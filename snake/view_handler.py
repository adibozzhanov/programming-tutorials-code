from tkinter import *


class ViewHandler(Canvas):
    def __init__(self, master, width, height):
        super().__init__(master, width=500, height=500, bg='black')
        self.pack()

    def draw_grid(self, grid):
        self.delete("all")
        grid_w = len(grid)
        cell_w = 500 / grid_w
        for row in range(grid_w):
            for col in range(grid_w):
                x = col * cell_w
                y = row * cell_w

                if grid[row][col] == 1:
                    self.create_rectangle(x + 1,
                                          y + 1,
                                          x + cell_w - 1,
                                          y + cell_w - 1,
                                          fill='white')
                if grid[row][col] == 2:
                    self.create_rectangle(x + 1,
                                          y + 1,
                                          x + cell_w - 1,
                                          y + cell_w - 1,
                                          fill='red')

        self.master.update()


if __name__ == "__main__":

    root = Tk()
    root.title('Snake')

    vh = ViewHandler(root, width=500, height=500)
    grid = [[0 for i in range(10)] for j in range(10)]

    vh.draw_grid(grid)

    root.mainloop()
