from __future__ import division

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
    global flow, img, pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id, rects
    size(1500 // 2, 1187 // 2)
    frameRate(60)
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
    scale_ = 2

    # PGraphics drawing size
    pwidth, pheight = width * scale_, height * scale_

    # Margins around the drawing
    margin = 30 * scale_ * 0

    # STYLE PARAMETERS
    stroke_weight = 2

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBrush(pg, fills.BasicFill(pg))
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
    
    
    rects = []
    
    for _ in range(4):
        w = random(250, 750)
        h = random(250, 750)
        
        x = random(pwidth - w)
        y = random(pheight - h)
        
        rects.append(gm.Rect(x, y, w, h))
        
    for r in rects:
        pen.stroke((0,0,0))
        pen.rect(PVector(r.x, r.y), r.w, r.h)
    

def keyReleased():
    global flag

    if key == ENTER:
        flag = True

def draw():
    global flow, img, flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, rects

    pg.beginDraw()
    pen.noFill()
    pg.noFill()
    
    v = PVector(random(pwidth), random(pheight))
    v_ = PVector(v.x, v.y - 20)
    
    for i, r in enumerate(rects):
        if r.inside(v):
            pen.stroke(colors[i])
            break
        else:
            pen.stroke(colors[4])
    
    pen.line(v, v_, d= 5)
    
    pg.endDraw()
    # Display final drawing and save to .png in same folder
    fill(0,5,95)
    rect(0,0,width,height)
    image(pg, 0, 0, width, height)
    noFill()
    
    if keyPressed:
        if (key == 's'):
            tools.save_image(pg, seed, palette_id)
