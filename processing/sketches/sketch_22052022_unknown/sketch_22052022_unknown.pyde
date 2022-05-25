from __future__ import division

import pens
import tools
import fills


def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id
    size(500, 700)

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
    margin = 30 * scale_

    # STYLE PARAMETERS
    stroke_weight = 2

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    #pen = pens.PenBasic(pg, fills.CurveFill(pg))
    pen = pens.PenBasic(pg, fills.BasicFill(pg))
    #pen = pens.PenRandom(pg, fills.ScannerFill(pg))

    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    # pg.colorMode(RGB, 255, 255, 255)
    pen.strokeWeight(stroke_weight)
    pg.strokeCap(SQUARE)

    pg.endDraw()
    # pen.set_clean(True)
    # pen.prob = 0

    flag = True


def keyReleased():
    global flag

    if key == ENTER:
        flag = True


def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, scale_, seed
    
    s = pwidth // 2

    pen.noStroke()
    pen.fill((0,0,0))
    #pen.rect(PVector(0, 0), pwidth, pheight)
    
    pen.noFill()
    
    pen.stroke(colors[0])
    
    minr = random(10, pwidth / 6)
    maxr = random(pwidth / 6, pwidth)
    
    for _ in range(150):
        x = random(0, pwidth)
        y = random(0, pheight)
        border_dist = min(min(x, pwidth - x), min(y, pheight - y))
        
        if border_dist < minr:
            continue
        
        r = min(maxr, border_dist)
        r = int(random(minr, maxr))
        
        pen.fill((0,0,0))
        pen.circle(PVector(x, y), r)
        pen.noFill()
        
        for i, r in enumerate(range(0, r, 5)):
            pen.stroke(colors[i % len(colors)])
            pen.circle(PVector(x, y), r)
        
        

def draw3():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, scale_, seed
    
    
    pg.rectMode(CENTER)
    
    r = pwidth / 10
    r_step = r / 5
    
    
    x = r
    pen.noFill()
    
    while x < pwidth:
        y = r
        
        while y < pheight:
            if random(1) < 0.15:
                col = colors[int(random(len(colors)))]
            else:
                col = (0,5,0)
            
            r_ = r_step
            while r_ <= r - 1:
                pen.stroke((col[0],col[1], col[2], map(y, r, pheight-r, 150, 0)))
                pg.pushMatrix()
                pg.translate(x, y)
                pg.rotate(radians(randomGaussian() * map(y, r, pheight-r, 1, 15)))
                pen.rect(PVector(0,0), r_, r_)
                pg.popMatrix()
                r_ += r_step
            
            y += r
            
        x += r
    pg.rectMode(CORNER)


def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id
    if flag:
        
        colors, palette_id = tools.get_color_palette()
        colors, palette_id = tools.get_color_palette(4206)
        colors = tools.hex_to_hsb(colors)
        
        print(palette_id, seed)
        
        flag = False
        pg.beginDraw()

        # Set background color
        pg.fill(*bg_col)
        pg.fill(0,5,95)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        
        
        pg.noFill()

        pen.fill(colors[1])
        pen.noStroke()
        # pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)

        pen.stroke(strk_col)

        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)

        draw3()

        pg.loadPixels()
        # tools.noisify_brightness(pg.pixels, pg)
        pg.updatePixels()

        # End drawing on PGraphics
        pg.popMatrix()
        pg.endDraw()

        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        print('ye')
    
    if keyPressed:
        if (key == 's'):
            tools.save_image(pg, seed, palette_id)
