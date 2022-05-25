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
    pen = pens.PenBrush(pg, fills.BasicFill(pg))
    #pen = pens.PenBasic(pg, fills.BasicFill(pg))

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

def draw3():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, scale_, seed

    r = pwidth / 5
    r_step = r / 5
    
    
    pen.stroke((0,0,0))
    x = r
    pen.noFill()
    for _ in range(1000):
        break
        pen.stroke(colors[int(random(len(colors)))])
        v = PVector(random(pwidth), random(pheight))
        v_ = PVector(random(pwidth), random(pheight))
        v_ = PVector(pwidth / 2, pheight / 2)
        
        u = (v - v_).normalize()
        
        v_ = v + u * random(25, 50)
            
        pen.line(v, v_)
    
    pen.rect(PVector(0,0), pwidth, pheight)
    
    for i, x in enumerate(range(pwidth // 6, pwidth - pwidth // 6, pwidth // 6)):
        pen.stroke(colors[int(random(len(colors)))])
        v = PVector(x, 100)
        v_ = PVector(x, 100 + pheight // 8 * (i + 1))
        pen.line(v, v_)
        
        
    
    for i, x in enumerate(range(pwidth // 6, pwidth - pwidth // 6, pwidth // 6)):
        pen.stroke(colors[int(random(len(colors)))])
        v = PVector(x, pheight // 8 * (i + 1) + 150)
        v_ = PVector(x, pheight - 25)
        pen.line(v, v_)
        
    x = 100
    y = 100
    w = 300
    h = 300
    
   #pen.rect(PVector(x, y), w, h)
    
    for _ in range(333):
        break
        v = PVector(random(x, x + w), random(y, y + h))
        v_ = PVector(random(x, x + w), random(y, y + h))
        
        u = (v - v_)
        if random(1) < 0.5:
            u = PVector(0, 1)
        else:
            u = PVector(0, -1)
        u.normalize().rotate(radians(random(-10, 10)))
        u = u * min(min(abs(y + h - v.y), abs(y - v.y)), random(50, 100))
        
        pen.line(v, v + u)
        

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id
    if flag:
        
        colors, palette_id = tools.get_color_palette()
        #colors, palette_id = tools.get_color_palette(4206)
        colors, palette_id = tools.get_color_palette(929)
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
        pen.strokeWeight(stroke_weight)

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
