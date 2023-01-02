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
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id, penb, objects, s, frames
    size(400, 400)
    frames = set()
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
    margin = 0 * scale_

    # STYLE PARAMETERS
    stroke_weight = 1

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBasic(pg, fills.BasicFill(pg))
    #pen = pens.PenBrush2(pg, fills.BasicFill(pg))
    penb = pens.PenBasic(pg, fills.BasicFill(pg))

    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    colorMode(HSB, 360, 100, 100)
    # pg.colorMode(RGB, 255, 255, 255)
    pen.strokeWeight(stroke_weight)
    pg.strokeCap(SQUARE)

    # pen.set_clean(True)
    # pen.prob = 0
    objects = [(x, pheight / 2) for x in range(-100, pwidth+1, 5)]
    flag = True
    frameRate(1000)
    s = 0
    
def IsIntersecting(a, b, c, d):
    denominator = ((b.x - a.x) * (d.y - c.y)) - ((b.y - a.y) * (d.x - c.x));
    numerator1 = ((a.y - c.y) * (d.x - c.x)) - ((a.x - c.x) * (d.y - c.y));
    numerator2 = ((a.y - c.y) * (b.x - a.x)) - ((a.x - c.x) * (b.y - a.y));

    if (denominator == 0):
        return numerator1 == 0 and numerator2 == 0;
    
    r = numerator1 / denominator;
    s = numerator2 / denominator;

    return (r >= 0 and r <= 1) and (s >= 0 and s <= 1)

def keyReleased():
    global flag

    if key == ENTER:
        flag = True
    
def draw2a():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, penb

    pen.stroke(strk_col)
    pen.fill(strk_col)
    
    rects = []
    for _ in range(2000):
        d = random(1)
        if d < 0.5:
            rects.append((random(pwidth), random(pheight), random(-pwidth, pwidth), random(5, 15), colors[int(random(len(colors)))], d, random(180)))
        else:
            rects.append((random(pwidth), random(pheight), random(5, 25), random(-pheight, pheight), colors[int(random(len(colors)))], d, random(180)))
    
    for i in range(0, 181, 1):            
        pen.noStroke()
        pen.fill((0,0,100))
        pen.rect(PVector(-margin, -margin), pwidth+margin*2, pheight+margin*2)
        pen.noFill()
        
        pen.fill(colors[1])
        
        pen.stroke((0,0,0))
        for r in rects:
            x, y, w, h, c, d, o = r
            
            pen.fill(c)
            if d < 0.5:
                pen.rect(PVector(x, y), w * sin(radians((i+int(o)) % 180)), h)
            else:   
                pen.rect(PVector(x, y), w, h * sin(radians((i+int(o)) % 180)))    
                
        tools.save_image(pg, 'frame_' + str(i).zfill(4))    

def update(objects, s):
    global pen, colors
    stepx = 0.025
    stepy = 0.0025
    pen.noStroke()
    pg.rectMode(CENTER)
    for x in range(0, pwidth+1, 2):
        for y in range(0, pheight+1, 2):
            n = noise(x*stepx, y*stepy, 0.13 * abs((100 - (s % 200))))
            n1 = noise(x*stepy, y*stepx, 0.13 * abs((100 - (s % 200))))
            if n < 0.45:
                pen.fill((0,10,15))
            elif n1 * n < 0.25:
                pen.fill((0,80,80))
            else:
                pen.fill((0,0,75))
            pen.rect(PVector(x, y), 3, 3)
    pg.rectMode(CORNER)
    pen.strokeWeight(3)
    pen.stroke((0,0,75))
    
    for _ in range(5):
        if random(1) < 0.25:
            c = PVector(random(pwidth), random(pheight))
            c_ = PVector(c.x, c.y)
            c_.normalize()
            if random(1) < 0.5:
                pen.stroke((0,10,15))
            else:
                pen.stroke((0,0,75))
            pen.line(c, c + c_ * random(-55, 55))
    

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, objects, s
    
    
    pg.beginDraw()
        
    #print(palette_id)
    
    # Set background color
    pg.fill(0,0,100)
    pg.noStroke()
    pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
    pg.noFill()
    
    
    
    pen.stroke(strk_col)
    
    # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
    pg.pushMatrix()
    pg.translate(margin, margin)
    
    #draw2()
    update(objects, s)
    s += 1
    
    pg.loadPixels()
    #tools.noisify_brightness(pg.pixels, pg)
    pg.updatePixels()
    
    # End drawing on PGraphics    
    pg.popMatrix()
    pg.endDraw()
    
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    
    
    step = abs((100 - (s % 200)))
    if step not in frames:
        frames.add(step)
        tools.save_image(pg, 'frame_' + str(step).zfill(4))
    else:
        noLoop()
    
    if keyPressed:
        if (key == 's'):
            tools.save_image(pg, seed, palette_id)
