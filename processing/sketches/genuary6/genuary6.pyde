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
    scale_ = 2

    # PGraphics drawing size
    pwidth, pheight = width * scale_, height * scale_

    # Margins around the drawing
    margin = 50 * scale_

    # STYLE PARAMETERS
    stroke_weight = 1

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBasic(pg, fills.BasicFill(pg))
    #pen = pens.PenBrush2(pg, fills.BasicFill(pg))
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
    
def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, penb

    pen.stroke(strk_col)
    pen.fill(strk_col)    
    print(seed)
    #pg.translate(width / 2, 0)
    mondrian = gm.Mondrian(0, 0, pwidth, pheight, 5, strk_col, fill_col=colors[0], n_col=13, colors=colors[1:], margin=int(random(5, 25)), circle_pack=False)
        
    
    mondrian.generate()
    mrs = []
    mrs.append(mondrian)
    #mrs.extend([gm.Mondrian(r.x+5, r.y+5, r.w-10, r.h-10, 5, strk_col, fill_col=bg_col, n_col=5, colors=colors, margin=10, circle_pack=False) for r in mondrian.rects])
    
    circles = [gm.Circle(random(pwidth), random(pheight), random(250,500)) for _ in range (1)]
    #circles = [gm.Circle(pwidth / 2, pheight / 2, pwidth / 2) for _ in range (1)]

    mrscopy = [mr for mr in mrs]
    for i in range(15):
        #break
        newmrs = []
        for mr in mrscopy:
            for r in mr.rects:
                if r.x+mr.margin/2 >= r.x + r.w-mr.margin or r.w-mr.margin <= 4 or r.y+mr.margin/2 >= r.y + r.h-mr.margin or r.h-mr.margin <= 4:
                    continue
                print(i)
                newmrs.append(gm.Mondrian(r.x+mr.margin/2, r.y+mr.margin/2, r.w-mr.margin, r.h-mr.margin, int(1), strk_col, fill_col=colors[0], n_col=1, colors=colors, margin=int(random(5, 25)), circle_pack=False))
                newmrs[-1].generate()
        mrs.extend(newmrs)
        mrscopy = [mr for mr in newmrs]
            
    for mr in mrs:
        for r in mr.rects:
            corners = [(r.x, r.y), (r.x, r.y + r.h), (r.x + r.w, r.y), (r.x + r.w, r.y + r.h)]
            draw_flag = True
            
            '''for c in circles:
                draw_flag = True
                for x, y in corners:
                    if not c.inside(x, y):
                        draw_flag = False
                        break
                if draw_flag:
                    break
            
            if not draw_flag:
                continue
            '''
            #pen.stroke(r.strk_col)
            pen.noStroke()
            pen.fill(r.fill_col)
            pen.rect(PVector(r.x, r.y), r.w, r.h)
    

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id
    
    if flag:
        seed = int(random(1000000))
        randomSeed(seed)
        noiseSeed(seed)
        flag = False
        pg.beginDraw()
        
        colors, palette_id = tools.get_color_palette(3846)
        colors, palette_id = tools.get_color_palette(1744)
        colors = tools.hex_to_hsb(colors)
        
        # Set background color
        pg.fill(60,10,96)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
        
        
        
        pen.stroke(strk_col)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
        
        draw2()
        
        #pg.loadPixels()
        #tools.noisify_brightness(pg.pixels, pg, 0.045)
        #pg.updatePixels()
        
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
    
    if keyPressed:
        if (key == 's'):
            tools.save_image(pg, seed, palette_id)
