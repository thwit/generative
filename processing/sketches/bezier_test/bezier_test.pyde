from __future__ import division
import random
import pens
import geometry as gm

def setup():
    global pg, bg_col, strk_col, n, stroke_weight, th, xs1, xs2, ys1, ys2, nb, nbeziers, pen
    size(800, 800)
    frameRate(60)
    pg = createGraphics(width, height)
    pen = pens.Pen3(pg)
    
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
        
        nb = gm.NBezier(PVector(xs1, ys1), PVector(xs2, ys2), PVector(xe1, ye1), PVector(xe2, ye2), n)
        nbeziers.append(nb)
        nb.draw(pen)
        
        xs1 = None
 
def draw():
    global pg, bg_col, strk_col, n, stroke_weight, th, xs1, xs2, ys1, ys2, nb, nbeziers, pen
    
    pg.beginDraw()
    if xs1 is not None:
        
        pg.background(102)
        pg.stroke(255)
        pen.strokeWeight(2)
        
        for nb_ in nbeziers:
            nb_.draw(pen)
        # NBezier(xs1, ys1, xs2, ys2, xe1, ye1, xe2, ye2, n)     
        xe1 = mouseX
        ye1 = mouseY
        
        xe2 = xe1
        ye2 = ye1 + th
        nb = gm.NBezier(PVector(xs1, ys1), PVector(xs2, ys2), PVector(xe1, ye1), PVector(xe2, ye2), n)
    
        nb.draw(pen)
    
            
    
    
    pg.endDraw();
    image(pg, 0, 0); 
