from __future__ import division
import random as random_
import math

import pens
import tools
import fills
import geometry as gm
import sdfs


def noise_(col, row):
    strength = 0.5
    size_ = 1
    col *= 0.03
    row *= 0.03
    return noise(col, row) * TWO_PI
    #return noise(col, row, strength * size_* noise(col, row)) * TWO_PI


def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id, penb, objects, s, frames, img, sdflist
    size(500, 500, P3D)
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
    colors = [(156, 35, 17), (169, 60, 54), (148, 27, 28), (37, 64, 75), (188, 57, 31)]

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
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2, P3D)
    pen = pens.PenBasic(pg, fills.BasicFill(pg))
    #pen = pens.PenBrush2(pg, fills.BasicFill(pg))
    penb = pens.PenBasic(pg, fills.BasicFill(pg))

    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    colorMode(HSB, 360, 100, 100)
    #pg.colorMode(RGB, 255, 255, 255)
    pen.strokeWeight(stroke_weight)
    pg.strokeCap(SQUARE)
    pg.smooth(8)

    # pen.set_clean(True)
    # pen.prob = 0
    objects = [(random(TWO_PI), TWO_PI - TWO_PI / 10, random(0.1, 1), colors[int(random(len(colors)))]) for _ in range(60)]
    flag = True
    frameRate(100000)
    s = 0
    pg.hint(ENABLE_STROKE_PURE)
    sdflist = []
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            for k in range(1, 15):
                sdflist.append((PVector(pwidth / 4 * (i + 1), pheight / 4 * (j + 1)), 20 * k))
    
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


def update(objects, s):
    global pg, sdflist
    
    
    #c = PVector(pwidth / 2, pheight / 2)
    #c = PVector(0, 0)
    #r = 100
    w = h = 100
    
    #sdflist = [(PVector(pwidth / 3, pheight / 2), pheight / 3), (PVector(pwidth / 3 * 2, pheight / 2), pheight / 3)]
    pg.noStroke()
    
    for _ in range(250):
        p = PVector(random(pwidth), random(pheight))
        col = None
        
        sdfdists = [sdfs.sdCircleAnnular(p, c, r, 5) for c, r in sdflist]
        ds = []
        for i in range(len(sdfdists)):
            break
            breakk = False
            for j in range(i+1, len(sdfdists)):
                ds.append(max(sdfdists[i], sdfdists[j]))
                if ds[-1] < 0:
                    breakk = True
                    break
            if breakk:
                break        
        
        d1 = sdfs.sdCircleAnnular(p, PVector(450, 100), 5, 2.5)
        d1 = sdfs.sdRep(d1, 50)
        
        d2 = sdfs.sdCircleAnnular(p, PVector(117, 280), 5, 2.5)
        d2 = sdfs.sdRep(d2, 100)
        
        if sdfs.opIntersection(d1, d2) < 0:
            #pen.stroke((0,0,0))
            col = color(0,80,70)
            pg.fill(col)
            pg.circle(p.x, p.y, 4)
        else:
            #pen.stroke((0,0,100))
            col = color(0,0,0)
            pg.fill(col)
            pg.circle(p.x, p.y, 4)
            
        #pg.set(int(p.x), int(p.y), col)
            

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, objects, s
    
    
    pg.beginDraw()
        
    #print(palette_id)
    
    # Set background color
   # pg.fill(0,0,85)
   # pg.noStroke()
    #pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
   # pg.noFill()
    #randomSeed(1000)
    
    
    #pen.stroke(strk_col)
    
    # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
   # pg.pushMatrix()
    #pg.translate(margin, margin)
    
    #draw2()
    update(objects, s)
    s += 1
    
    #pg.loadPixels()
    #tools.noisify_brightness(pg.pixels, pg)
    #pg.updatePixels()
    
    # End drawing on PGraphics    
    #pg.popMatrix()
    pg.endDraw()
    
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    
    
    #colors, palette_id = tools.get_color_palette()
    #colors = tools.hex_to_hsb(colors)
    
    if keyPressed:
        if (key == 's'):
            tools.save_image(pg, 'imgcorrup')
        if key == ENTER:
            objects = [(random(TWO_PI), TWO_PI - TWO_PI / 10, random(0.1, 1), colors[int(random(len(colors)))]) for _ in range(60)]
