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

def setup2():
    size(700, 700)
    pwidth = pheight = 2100
    pg = createGraphics(pwidth, pheight)
    pg.beginDraw()
    #pg.smooth(8)
    pg.noSmooth()
    pg.strokeCap(PROJECT)
    
    tw = th = 200
    
    padding = 1
    rows = pheight // th - padding
    cols = pwidth // tw - padding
    sw = 5
    n = 7

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
    image(pg, 0, 0, width, height)
    pg.save("arcc_truchet.png")
    
    
class Bezier:
    def __init__(self, x1, y1, cpx1, cpy1, cpx2, cpy2, x2, y2, col, sw, dir=None):
        bezier(x1, y1, cpx1, cpy1, cpx2, cpy2, x2, y2);
        self.x1 = x1
        self.y1 = y1
        self.cpx1 = cpx1
        self.cpy1 = cpy1
        self.cpx2 = cpx2
        self.cpy2 = cpy2
        self.x2 = x2
        self.y2 = y2
        self.col = col
        self.sw = sw
        if dir is None:
            dir = random.randint(0,1)
        self.rot = [0, HALF_PI][dir]
        
    def draw(self, pg):
        
        noFill()
        pg.stroke(self.col)
        pg.strokeWeight(self.sw)
        pg.bezier(self.x1, self.y1, self.cpx1, self.cpy1, self.cpx2, self.cpy2, self.x2, self.y2)

class TileBezier:
    def __init__(self, x, y, r, col, sw, dir=None):
        self.x = x
        self.y = y
        self.r = r
        self.col = col
        self.sw = sw
        if dir is None:
            dir = random.randint(0,1)
        self.rot = [0, HALF_PI][dir]
        
    def draw(self, pg, n=1):
        pg.stroke(self.col)
        pg.strokeWeight(self.sw)
        pg.pushMatrix()
        pg.translate(self.x, self.y)
        pg.rotate(self.rot)
      
        for k, rad1, rad2 in [(1, 0, HALF_PI), (-1, PI, PI + HALF_PI)]:
            x1 = self.r * sin(rad1)
            y1 = self.r * cos(rad1)
            
            cpx1 = x1 + self.r * k * -1
            cpy1 = y1 + self.r * k * -1
            
            x2 = self.r * sin(rad2)
            y2 = self.r * cos(rad2)
            
            cpx2 = x2 - self.r * k
            cpy2 = y2 - self.r * k
            
            pg.bezier(x1, y1, cpx1, cpy1, cpx2, cpy2, x2, y2)
                    
        pg.popMatrix()
        
    def draw_bb(self, pg):
        pg.stroke(0,0,0)
        pg.strokeWeight(1)
        pg.noFill()
        
        pg.pushMatrix()
        pg.translate(self.x, self.y)
        pg.rect(-self.w / 2, -self.h / 2, self.w, self.h)
        pg.popMatrix()
        
    
def setup():
    size(700, 700)
    pwidth = pheight = width
    pg = createGraphics(pwidth, pheight)
    pg.beginDraw()
    #pg.smooth(8)
    pg.noSmooth()
    pg.strokeCap(PROJECT)
    
    # define and set colors
    bg = 0xFFF6E6E4
    strk = 0xFFBB6464
    pg.fill(bg)
    pg.rect(-1, -1, pwidth+1, pheight+1)      
    
    sw = 3
    
    TileBezier(width / 2, height / 2, 100, strk, sw).draw(pg)
    
    
    pg.endDraw();
    image(pg, 0, 0, width, height);
    
