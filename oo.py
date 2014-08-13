# OOP demo
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

class point():
    def __init__(self, p):
       self.set_coords(p)

    def add_point(self, p):
       self.x += p.x
       self.y += p.y

    def set_coords(self, p):
       (x, y) = p
       self.x = x
       self.y = y

    def get_coords(self):
       return (self.x, self.y)

    def x_coord(self):
       return self.x

    def y_coord(self):
       return self.y

    def render(self):
       print(self.x, self.y)

class color_point(point):

    def __init__(self, p, c):
       super().__init__(p)
       self.set_color(c)
       
    def set_color(self, c):
       self.color = c
    
    def get_color(self):
       return self.color
    
    def render(self):
       print(self.color, self.x, self.y)

class magic_point(point):

    def __init__(self, p):
       super().__init__(p)

    def render(self):
       print('magic!')
       super().render()

p1 = color_point((3, 2), 'red')
p2 = magic_point((1, 1))
p1.add_point(p2)
p3 = point((4,5))
points = [p1, p2, p3]
for p in points:
    p.render()
