from __future__ import division
import random

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
            xss = list(range(xs1_, xs2_, abs(xs1_-xs2_) // (self.n-1)))
        elif abs(xs1_ - xs2_) < self.n:
            diff = xs1_ - xs2_
            xss = [xs1_ + i * diff / (self.n-1) for i in range(self.n)]
            
        if abs(xe1_ -xe2_) >= self.n:
            xes = list(range(xe1_, xe2_, abs(xe1_-xe2_) // (self.n-1)))
        elif abs(xe1_ - xe2_) < self.n:
            diff = xe1_ - xe2_
            xes = [xe1_ + i * diff / (self.n-1) for i in range(self.n)]
            
        if abs(ys1_ - ys2_) >= self.n:
            yss = list(range(ys1_, ys2_, abs(ys1_-ys2_) // (self.n-1)))
        elif abs(ys1_ - ys2_) < self.n:
            diff = ys1_ - ys2_
            yss = [ys1_ + i * diff / (self.n-1) for i in range(self.n)]
            
        if abs(ye1_ - ye2_) >= self.n:
            yes = list(range(ye1_, ye2_, abs(ye1_-ye2_) // (self.n-1)))
        elif abs(ye1_ - ye2_) < self.n:
            diff = ye1_ - ye2_
            yes = [ye1_ + i * diff / (self.n-1) for i in range(self.n)]
            
        xss.append(self.xs2)
        yss.append(self.ys2)
        xes.append(self.xe2)
        yes.append(self.ye2)
        
        for i, (xs, ys, xe, ye) in enumerate(zip(xss, yss, xes, yes)):
            if i == len(xss) - 1:
                break
            cpx1 = xs
            cpy1 = ye
            
            cpx2 = xs
            cpy2 = ye
            pg.bezier(xs, ys, cpx1, cpy1, cpx2, cpy2, xe, ye)
        
        
def setu2p():
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
    
 

def setup():
    global pg, bg_col, strk_col, n, stroke_weight, th, xs1, xs2, ys1, ys2, nb, nbeziers
    size(800, 800)
    frameRate(60)
    pg = createGraphics(width, height)
    
    #### COLOR DEFINITIONS
    bg_col = 0xFFF6E6E4
    strk_col = 0xFFBB6464
    stroke_weight = 2
    n = 20
    
    th = 100

    xs1 = xs2 = ys1 = ys2 = nb = None
    nbeziers = []
    
    
def mouseClicked():
    global pg, bg_col, strk_col, n, stroke_weight, th, xs1, xs2, ys1, ys2, nb, nbeziers
    
    if xs1 is None:
        xs1 = mouseX - th // 2
        xs2 = mouseX + th // 2
        ys1 = mouseY
        ys2 = mouseY
    elif xs1 is not None:
        xe1 = mouseX
        ye1 = mouseY
        
        xe2 = xe1
        ye2 = ye1 + th
        
        nb = NBezier(xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, strk_col, stroke_weight, n)
        nbeziers.append(nb)
        
        xs1 = None
 
def draw():
    global pg, bg_col, strk_col, n, stroke_weight, th, xs1, xs2, ys1, ys2, nb, nbeziers
    pg.beginDraw()
    pg.background(102)
    pg.stroke(255)
    
    for nb_ in nbeziers:
        nb_.draw(pg)
        
    
    
    if xs1 is not None:
        # NBezier(xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, n)     
        xe1 = mouseX
        ye1 = mouseY
        
        xe2 = xe1
        ye2 = ye1 + th
        
        nb = NBezier(xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, strk_col, stroke_weight, n)
        nb.draw(pg)
    
            
    
    
    pg.endDraw();
    image(pg, 0, 0); 
