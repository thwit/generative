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
        
    def draw(self, pg, n):
        
        pg.fill(self.bg)
        pg.stroke(self.col)
        pg.strokeWeight(self.sw)
        pg.pushMatrix()
        pg.translate(self.x, self.y)
        pg.rotate(self.rot)
        
        for k in range(n//2, -n//2, -1):
                
            k *= 5
            pg.arc(-self.w / 2, -self.h / 2, self.w + self.sw * k, self.h + self.sw * k, 0, HALF_PI, OPEN)
            pg.arc(self.w / 2, self.h / 2, self.w + self.sw * k, self.h + self.sw * k, PI, PI + HALF_PI, OPEN)
            
        pg.popMatrix()
        
    def draw_bb(self, pg):
        pg.stroke(0,0,0)
        pg.strokeWeight(1)
        pg.noFill()
        
        pg.pushMatrix()
        pg.translate(self.x, self.y)
        pg.rect(-self.w / 2, -self.h / 2, self.w, self.h)
        pg.popMatrix()
        
def draw_line(pg, x1, y1, x2, y2):
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
            
        random_dots(pg, new_x, new_y);

def random_dots(pg, dot_x, dot_y):
    dmi = 10
    for _ in range(dmi):
        dir_x = random.uniform(-rand, rand)
        dir_y = random.uniform(-rand, rand)
        new_x = dot_x+dir_x
        new_y = dot_y+dir_y
        pg.circle(new_x, new_y, 0.075)


def setup():
    size(700, 700)
    pwidth = pheight = 2100
    pg = createGraphics(pwidth, pheight)
    pg.beginDraw();
    #pg.smooth(8)
    pg.noSmooth()
    pg.strokeCap(PROJECT)
    
    tw = th = 200
    
    padding = 1
    rows = pheight // th - padding
    cols = pwidth // tw - padding
    sw = 5
    n = 15

    bg = 0xFFF6E6E4
    strk = 0xFFBB6464
    pg.fill(bg)
    pg.rect(-1, -1, pwidth+1, pheight+1)
    tiles = []

    for _ in range(1):
        for r in range(padding+1,rows):
            for c in range(padding+1,cols):
                rd = random.randint(1, rows)
                dir = random.randint(0,1) if rd < r else 0
                t = Tile(c * th, r * tw, tw, th, strk, bg, sw, None)
                t.draw(pg, n)
                tiles.append(t)
    
    for t in tiles:
        break
        t.draw_bb(pg)
        
        
    pg.endDraw();
    image(pg, 0, 0, width, height);
    pg.save("arcc_truchet.png");
                
