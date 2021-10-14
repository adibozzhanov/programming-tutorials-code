class Player:
    def __init__(self, master):
        self.master = master
        self.choice = "UP"

        self.master.bind("<Left>", lambda x: self.set_choice("LEFT"))
        self.master.bind("<a>", lambda x: self.set_choice("LEFT"))
        self.master.bind("<Right>", lambda x: self.set_choice("RIGHT"))
        self.master.bind("<d>", lambda x: self.set_choice("RIGHT"))
        self.master.bind("<Up>", lambda x: self.set_choice("UP"))
        self.master.bind("<w>", lambda x: self.set_choice("UP"))
        self.master.bind("<Down>", lambda x: self.set_choice("DOWN"))
        self.master.bind("<s>", lambda x: self.set_choice("DOWN"))

    def make_move(self, grid, head):
        return self.choice

    def set_choice(self, choice):
        self.choice = choice
