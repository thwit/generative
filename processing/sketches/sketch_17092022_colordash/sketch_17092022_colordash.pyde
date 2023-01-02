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
    size(750, 750)
    
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
    pen = pens.PenBasic(pg, fills.BasicFill(pg))
    #pen = pens.PenRandom(pg, fills.ScannerFill(pg))
    penb = pens.PenBasic(pg, fills.BasicFill(pg))

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
    
def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, penb

    pen.noStroke()
    pen.noFill()
    
    for _ in range(100000):
        x = random(0, pwidth)
        y = random(0, pheight)
        
        v = PVector(x, y)
        
        dir = [-1, 1][int(random(2))]
        
        lngth = random(5, 10)
        
        v_ = v + PVector(lngth * dir, lngth)
        
        #v_ = PVector(random(0, pheight), random(0, pheight))
        
        pen.stroke((map(y, 0, pheight, 0, 100), 25, 50, 75))
        pen.stroke((0, 0, map(y, 0, pheight, 95, 25), 75))
        
        h, s, b = colors[int(random(len(colors)))]
        if random(1) < 0 or dir == -1:
            h, s, b = colors[1]
        pen.stroke((h, s, b, random(10, 100)))
        
        pen.line(v, v_)
        
        r = random(5, 75)
        if random(1) < -0.003 and x > r and x < pwidth - r and y > r and y < pheight - r:
            h, s, b = colors[int(random(len(colors)))]
            pen.fill((h, s, b, random(10, 100)))
            pen.circle(v, r)
            pen.noFill()
    
    
    

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id
    
    if flag:
        flag = False
        pg.beginDraw()
        
        colors, palette_id = tools.get_color_palette(3846)
        colors = tools.hex_to_hsb(colors)
        
        # Set background color
        pg.fill(0,0,100)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
        
        
        
        pen.stroke(strk_col)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
        
        draw2()
        
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
