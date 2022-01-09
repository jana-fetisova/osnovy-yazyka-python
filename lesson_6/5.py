class Stationary:

    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f'Just start drawing! {self.title}')

class Pen(Stationary):
    def draw(self):
        print(f'Just start drawing with pen! {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Just start drawing with pencil! {self.title}')

class Marker(Stationary):
    def draw(self):
        print(f'Just start drawing with marker! {self.title}')

stat = Stationary()
mark = Marker()
penc = Pencil()
pen = Pen()

stat.draw()
mark.draw()
pen.draw()
penc.draw()


