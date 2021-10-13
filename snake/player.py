class Player:
    def __init__(self, master):
        self.master = master
        self.choice = "UP"

        self.master.bind("<Left>", lambda x: self.set_choice("LEFT"))
        self.master.bind("<Right>", lambda x: self.set_choice("RIGHT"))
        self.master.bind("<Up>", lambda x: self.set_choice("UP"))
        self.master.bind("<Down>", lambda x: self.set_choice("DOWN"))

    def make_move(self, grid):
        return self.choice

    def set_choice(self, choice):
        self.choice = choice
