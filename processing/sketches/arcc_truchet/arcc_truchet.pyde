import random

rand = 0.5

def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    
    return x

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
    
class Bezier:
    def __init__(self, x1, y1, cpx1, cpy1, cpx2, cpy2, x2, y2, col, sw):
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
        
    def draw(self, pg):
        
        pg.noFill()
        pg.stroke(self.col)
        pg.strokeWeight(self.sw)
        pg.bezier(self.x1, self.y1, self.cpx1, self.cpy1, self.cpx2, self.cpy2, self.x2, self.y2)
        
        
class NBezier:
    def __init__(self, xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, col, sw, n):
        
        
        self.xs1 = xs1
        self.xs2 = xs2
        self.ys1 = ys1
        self.ys2 = ys2
        self.xe1 = xe1
        self.xe2 = xe2
        self.ye1 = ye1
        self.ye2 = ye2
        self.col = col
        self.sw = sw
        self.n = n
        
    def draw(self, pg):
        pg.noFill()
        pg.stroke(self.col)
        pg.strokeWeight(self.sw)
        
        
        xs1_ = min(self.xs1, self.xs2)
        xs2_ = max(self.xs1, self.xs2)
        
        ys1_ = min(self.ys1, self.ys2)
        ys2_ = max(self.ys1, self.ys2)
        
        xe1_ = min(self.xe1, self.xe2)
        xe2_ = max(self.xe1, self.xe2)
        
        ye1_ = min(self.ye1, self.ye2)
        ye2_ = max(self.ye1, self.ye2)
        
        #pg.line(xs1_, ys1_, xs2_, ys2_)
        #pg.line(xe1_, ye1_, xe2_, ye2_)
    
        
        xss = []
        xes = []
        yss = []
        yes = []
        
        if abs(xs1_ - xs2_) >= self.n:
            xss = list(range(xs1_, xs2_, abs(xs1_-xs2_) / (self.n-1)))
        elif abs(xs1_ - xs2_) < self.n:
            diff = xs1_ - xs2_
            xss = [xs1_ + i * diff / (self.n-1) for i in range(self.n)]
            
        if abs(xe1_ -xe2_) >= self.n:
            xes = list(range(xe1_, xe2_, abs(xe1_-xe2_) / (self.n-1)))
        elif abs(xe1_ - xe2_) < self.n:
            diff = xe1_ - xe2_
            xes = [xe1_ + i * diff / (self.n-1) for i in range(self.n)]
            
        if abs(ys1_ - ys2_) >= self.n:
            yss = list(range(ys1_, ys2_, abs(ys1_-ys2_) / (self.n-1)))
        elif abs(ys1_ - ys2_) < self.n:
            diff = ys1_ - ys2_
            yss = [ys1_ + i * diff / (self.n-1) for i in range(self.n)]
            
        if abs(ye1_ - ye2_) >= self.n:
            yes = list(range(ye1_, ye2_, abs(ye1_-ye2_) / (self.n-1)))
        elif abs(ye1_ - ye2_) < self.n:
            diff = ye1_ - ye2_
            yes = [ye1_ + i * diff / (self.n-1) for i in range(self.n)]
            
        xss.append(self.xs2)
        yss.append(self.ys2)
        xes.append(self.xe2)
        yes.append(self.ye2)
        
        for xs, ys, xe, ye in zip(xss, yss, xes, yes):
            cpx1 = xs
            cpy1 = ye
            
            cpx2 = xs
            cpy2 = ye
            pg.bezier(xs, ys, cpx1, cpy1, cpx2, cpy2, xe, ye)
        
        

class TileBezier:
    def __init__(self, x, y, r, col, sw, spacing, cp_mult, dir=None):
        self.x = x
        self.y = y
        self.r = r
        self.col = col
        self.sw = sw
        if dir is None:
            dir = random.randint(0,1)
        self.rot = [0, HALF_PI][dir]
        self.spacing = spacing
        self.cp_mult = cp_mult
        
    def draw(self, pg, n=1):
        pg.stroke(self.col)
        pg.strokeWeight(self.sw)
        pg.pushMatrix()
        pg.translate(self.x, self.y)
        pg.rotate(self.rot)
      
        for i in range(n//2, -n//2, -1):
            for k, rad1, rad2 in [(1, 0, HALF_PI), (-1, PI, PI + HALF_PI)]:
                x1 = self.r * sin(rad1)
                y1 = self.r * cos(rad1) + self.sw * i * self.spacing
                
                cpx1 = x1
                cpy1 = y1 - self.r * k * self.cp_mult
                
                x2 = self.r * sin(rad2) + self.sw * i * self.spacing
                y2 = self.r * cos(rad2)
                
                cpx2 = x2 - self.r * k * self.cp_mult
                cpy2 = y2 
                
                
                if False:
                    pg.circle(x1,y1,5)
                    pg.circle(x2,y2,5)
                    pg.circle(cpx1,cpy1,5)
                    pg.circle(cpx2,cpy2,5)
                    
                Bezier(x1, y1, cpx1, cpy1, cpx2, cpy2, x2, y2, self.col, self.sw).draw(pg)
            
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
    pwidth = pheight = 1000
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
    
    
    tr = 50
    n_loop = 1
    n = 10
    sw = 1
    padding = 1
    spacing = 1
    cp_mult = 1
    
    rows = pheight // tr - padding
    cols = pwidth // tr - padding

    tiles = []

    #TileBezier(pwidth / 2, pheight / 2, tr, strk, sw).draw(pg)
    
    for _ in range(n_loop):
        for r in range(padding+1, rows, 2):
            for c in range(padding+1, cols, 2):
                t = TileBezier(c * tr, r * tr, tr, strk, sw, spacing, cp_mult, dir=None)
                t.draw(pg, n)
                tiles.append(t)
    
    print('done')
    pg.endDraw();
    image(pg, 0, 0, width, height)

    
    
def setup3():
    size(700, 700)
    pwidth = pheight = 1000
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
    
    
    tr = 125
    n_loop = 1
    n = 10
    sw = 3
    padding = 1
    spacing = 1
    cp_mult = 1
    
    rows = pheight // tr - padding
    cols = pwidth // tr - padding

    for _ in range(n_loop):
        for r in range(padding, rows, 2):
            for c in range(padding, cols, 2):
                # NBezier(xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, n)
                xs1 = c * tr
                ys1 = r * tr
                
                xs2 = xs1
                ys2 = ys1 + tr
                
                
                xe1 = random.randint(padding, cols) * tr
                ye1 = random.randint(padding, rows) * tr
                
                while xe1==xs1 or ye1==ys1:
                    xe1 = random.randint(padding, cols) * tr
                    ye1 = random.randint(padding, rows) * tr
                
                xe2 = xe1
                ye2 = ye1 + tr
                
                nb = NBezier(xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, strk, sw, n)
                nb.draw(pg)
        
    print('done')
    pg.endDraw();
    image(pg, 0, 0, width, height)
    
    
    
    
    
    
    
    
    
    
    
    
    
def setup3():
    size(700, 700)
    
    #### COLOR DEFINITIONS
    bg_col = 0xFFF6E6E4
    strk_col = 0xFFBB6464
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 3
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins around the drawing
    margin = 50 * scale_
    
    # Margins between each grid cell
    grid_margin = 0 * scale_
    
    # Outer size of grid cell
    tw = 50 * scale_
    th = 50 * scale_
    
    # Inner size of grid cell
    dw = tw - grid_margin
    dh = th - grid_margin
    
    # Number of rows and columns in grid
    rows = int(pheight // th)
    cols = int(pwidth // tw)
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 3
    n = 19
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pg.beginDraw()
    pg.smooth(8)
    pg.strokeCap(stroke_cap)
    
    # Set background color
    pg.fill(bg_col)
    pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
    
    # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
    pg.pushMatrix()
    pg.translate(margin, margin)
    
    for _ in range(n_loop):
        for r in range(1, rows):
            for c in range(1, cols):
                # Coordinates, heights, and widths for the drawn grid:
                # (x                 , y                 , w , h )
                # (c * tw + (tw-dw)/2, r * th + (th-dh)/2, dw, dh)
                t = Tile(c * tw + (tw-dw)/2, r * th + (th-dh)/2, dw, dh, strk_col, bg_col, stroke_weight)
                t.draw(pg, n)
    
    # End drawing on PGraphics    
    pg.popMatrix()
    pg.endDraw()
    
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    pg.save("arcc_truchet.png")
    
    
def setup():
    size(700, 700)
    
    #### COLOR DEFINITIONS
    bg_col = 0xFFF6E6E4
    strk_col = 0xFFBB6464
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 3
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins around the drawing
    margin = 50 * scale_
    
    # Margins between each grid cell
    grid_margin = 0 * scale_
    
    # Outer size of grid cell
    tw = 50 * scale_
    th = 50 * scale_
    
    # Inner size of grid cell
    dw = tw - grid_margin
    dh = th - grid_margin
    
    # Number of rows and columns in grid
    rows = int(pheight // th)
    cols = int(pwidth // tw)
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 5
    n = 15
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pg.beginDraw()
    pg.smooth(8)
    pg.strokeCap(stroke_cap)
    
    # Set background color
    pg.fill(bg_col)
    pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
    
    # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
    pg.pushMatrix()
    pg.translate(margin, margin)
    
    for _ in range(n_loop):
        for r in range(1, rows, 2):
            for c in range(1, cols, 2):
                # NBezier(xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, n)
                xs1 = c * tw
                ys1 = r * th
                
                xs2 = xs1
                ys2 = ys1 + th
                
                
                xe1 = random.randint(1, cols) * tw
                ye1 = random.randint(1, rows) * th
                
                while xe1==xs1 or ye1==ys1:
                    xe1 = random.randint(1, cols) * tw
                    ye1 = random.randint(1, rows) * th
                
                xe2 = xe1
                ye2 = ye1 + th
                
                nb = NBezier(xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, strk_col, stroke_weight, n)
                nb.draw(pg)
    
    # End drawing on PGraphics    
    pg.popMatrix()
    pg.endDraw()
    
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    pg.save("bezier_truchet.png")
