from __future__ import division
import random as random_
import math

import pens
import tools
import fills
import geometry as gm


def noise_(col, row):
    strength = 0.5
    size_ = 1
    col *= 0.03
    row *= 0.03
    return noise(col, row) * TWO_PI
    #return noise(col, row, strength * size_* noise(col, row)) * TWO_PI


def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id, penb
    size(500, 750)
    
    # SEEDS
    seed = int(random(1000000))
    randomSeed(seed)
    noiseSeed(seed)

    # COLOR DEFINITIONS
    colors = ['#8fa57f', '#FA8246', '#FEB139', '#F6F54D']
    colors = ['#252524','#505049','#808580','#c9cbca','#e4d7be']
    colors, palette_id = tools.get_color_palette()
    bg_col = '#fffffa'
    strk_col = '#000000'

    bg_col = tools.hex_to_hsb(bg_col)
    strk_col = tools.hex_to_hsb(strk_col)
    colors = tools.hex_to_hsb(colors)

    # LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 1

    # PGraphics drawing size
    pwidth, pheight = width * scale_, height * scale_

    # Margins around the drawing
    margin = 50 * scale_

    # STYLE PARAMETERS
    stroke_weight = 1

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBrush(pg, fills.BasicFill(pg))
    penb = pens.PenBasic(pg, fills.BasicFill(pg))
    #pen = pens.PenBasic(pg, fills.ScannerFill(pg))
    #pen = pens.PenBasic(pg, fills.BasicFill(pg))

    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    colorMode(HSB, 360, 100, 100)
    # pg.colorMode(RGB, 255, 255, 255)
    pen.strokeWeight(stroke_weight)
    pg.strokeCap(SQUARE)

    # pen.set_clean(True)
    # pen.prob = 0

    flag = True
    

def keyReleased():
    global flag

    if key == ENTER:
        flag = True
        
def draw3():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, penb
    
    penb.noStroke()
    penb.fill(bg_col)
    penb.rect(PVector(0,0), pwidth, pheight)
    
    pen.noStroke()
    pen.noFill()
    
    
    c = PVector(pwidth / 2, pheight / 2)
    h, s, b = colors[2]
    
    colors = [(h, s + 50, b - 50), (h, s + 20, b - 26), (h, s, b)]
    
    penb.stroke((0,0,0))
    maxr = int(pheight / 10)
    
    d = 15
    step = d

    
    for r in range(step, maxr+1, step):
        
        n = int(2 * math.pi * r / 25)
        x_ = c.x
        y_ = c.y
        
        #points = [(cos(TWO_PI / n * x) * r + x_, sin(TWO_PI / n * x) * r + y_) for x in range(0, n + 1)]
        points = []
        
        for k in range(n + 4):
            x = cos(TWO_PI / n * k) * r + x_
            y = sin(TWO_PI / n * k) * r + y_
            
            v = PVector(x, y)
            points.append(v)
            
            k += step
            
        for i in range(2, len(points)):
        
            pen.stroke((h, random(-5, 5) + s, random(-15, 15) + b))
            pen.stroke(colors[int(random(len(colors)))])
            penb.stroke(colors[int(random(len(colors)))])
            v_ = points[i-2]
            v__ = points[i-1]
            v = points[i]
            
            pen.shape_curve([v_, v__, v], d=7)
            #penb.strokeWeight(10)
            #penb.line(v, v_)

       
    
    
def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, penb
    
    print('redraw')
    
    pen.noStroke()
    pen.noFill()
    
    y = 50
    for x in range(0, pwidth, 25):
        v = PVector(x, y)
        v_ = PVector(x, y + x + 5)
        pen.line(v, v_)
    

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id
    
    if flag:
        flag = False
        pg.beginDraw()
        
        colors, palette_id = tools.get_color_palette(1491)
        colors = tools.hex_to_hsb(colors)
        
        # Set background color
        pg.fill(0,0,100)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
        '''pen.fill(bg_col)
        pen.noStroke()
        pen.rect(PVector(-3, -3), pwidth + margin * 2 + 10, pheight + margin * 2 + 10)
        pen.noFill()
        '''
        
        pen.stroke(strk_col)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
        
        draw3()
        
        pg.loadPixels()
        #tools.noisify_brightness(pg.pixels, pg)
        pg.updatePixels()
        
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
    
    if keyPressed:
        if (key == 's'):
            tools.save_image(pg, seed, palette_id)
