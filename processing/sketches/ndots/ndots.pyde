from __future__ import division
import pens

class TileNDot:
    def __init__(self, x, y, w, h, n):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.dots = [PVector(random(self.w), random(self.h)) for _ in range(n)]
        
    def draw(self, pg, stroke_weight, col):
        if isinstance(col, tuple):
            pg.stroke(*col)
        else:
            pg.stroke(col)
        #pg.strokeWeight(self.stroke_weight)
        pg.noFill()
        
        pg.pushMatrix()
        pg.translate(self.x, self.y)
        
        pg.beginShape()
        
        for d in self.dots:
            
            pg.curveVertex(d.x, d.y)
            
        pg.endShape()
            
        
        pg.popMatrix()

def setup():
    size(500, 500)
    
    #### COLOR PARAMTERS
    bg_col = 0xFFFFFFFC
    strk_col = 0xFF000000
    
    #### LAYOUT PARAMETERS
    # Paper size
    scale_ = 1
    
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins
    margin = 100 * scale_
    grid_margin = 30 * scale_
    
    # Tile size
    tw = 100 * scale_
    th = 100 * scale_
    
    # Drawn tile size
    dw = tw - grid_margin
    dh = th - grid_margin
    
    # Number of rows and columns
    rows = int(pheight // th)
    cols = int(pwidth // tw)
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 2
    n = 12
    n_loop = 1
    
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pg.beginDraw()
    pg.smooth(8)
    pg.strokeCap(stroke_cap)
    
    # set background color
    pg.fill(bg_col)
    pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
    
    pg.pushMatrix()
    pg.translate(margin, margin)
        
    max_p = sqrt((rows//2)**2 + (cols//2)**2)
    
    for _ in range(n_loop):
        for r in range(rows):
            for c in range(cols):
                p = sqrt((r-rows//2)**2 + (c-cols//2)**2)
                intensity = int(map(p, 0, max_p, 0, 255))
                intensity = 0
                offset = 1
                t = TileNDot(c * tw + (tw-dw)/2, r * th + (th-dh)/2 + offset, dw, dh, n)
                t.draw(pg, stroke_weight, (intensity, intensity, intensity))
        
    pg.popMatrix()
    pg.endDraw()

    image(pg, 0, 0, width, height)
    pg.save("ndots.png")
