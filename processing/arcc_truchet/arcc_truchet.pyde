import random

rand = 0.5

class Tile:
    def __init__(self, x, y, w, h, col, bg, sw, dir=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.sw = sw
        self.bg = bg
        if dir is None:
            dir = random.randint(0,1)
        self.rot = [0, HALF_PI][dir]
        
    def draw(self, n):
        
        fill(self.bg)
        stroke(self.col)
        strokeWeight(self.sw)
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.rot)
        
        for k in range(n//2, -n//2, -1):
                
            k *= 5
            arc(-self.w / 2, -self.h / 2, self.w + self.sw * k, self.h + self.sw * k, 0, HALF_PI, OPEN)
            arc(self.w / 2, self.h / 2, self.w + self.sw * k, self.h + self.sw * k, PI, PI + HALF_PI, OPEN)
            
        popMatrix()
        
    def draw_bb(self):
        stroke(0,0,0)
        strokeWeight(1)
        noFill()
        
        pushMatrix()
        translate(self.x, self.y)
        rect(-self.w / 2, -self.h / 2, self.w, self.h)
        popMatrix()
        
def draw_line(x1, y1, x2, y2):
    x_length = abs(x1-x2)
    y_length = abs(y1-y2)
    div_num = max(x_length, y_length)
    div_x = x_length/div_num
    div_y = y_length/div_num
    
    for i in range(div_num+1):
        if(x1<x2):
            new_x = x1 + div_x * i
        else:
            new_x = x1 - div_x * i
        if y1 < y2:
            new_y = y1 + div_y * i
        else:
            new_y = y1 - div_y * i
            
        random_dots(new_x, new_y);

def random_dots(dot_x, dot_y):
    dmi = 10
    for _ in range(dmi):
        dir_x = random.uniform(-rand, rand)
        dir_y = random.uniform(-rand, rand)
        new_x = dot_x+dir_x
        new_y = dot_y+dir_y
        circle(new_x, new_y, 0.075)


def setup():
    size(2100, 2100)
    smooth(8)
    strokeCap(PROJECT)
    
    tw = th = 100
    
    padding = 1
    rows = height // th - padding
    cols = width // tw - padding
    sw = 5
    n = 91

    bg = '#F6E6E4'
    strk = '#BB6464'
    fill(bg)
    rect(-1, -1, width+1, height+1)
    tiles = []

    for _ in range(10):
        for r in range(padding+1,rows):
            for c in range(padding+1,cols):
                rd = random.randint(1, rows)
                dir = random.randint(0,1) if rd < r else 0
                t = Tile(c * th, r * tw, tw, th, strk, bg, sw, None)
                t.draw(n)
                tiles.append(t)
    
    for t in tiles:
        break
        t.draw_bb()
    save("arcc_truchet.png");
                
