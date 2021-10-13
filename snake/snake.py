class Snake:
    def __init__(self, x, y):
        self.body = [(x, y), (x, y + 1), (x, y + 2)]

    def move(self, x, y, eat=False):
        self.body.insert(0, (x, y))

        if not eat:
            return self.body.pop()
        return None
