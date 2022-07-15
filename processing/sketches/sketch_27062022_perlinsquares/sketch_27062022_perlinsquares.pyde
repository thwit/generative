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
    global flow, img, pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id
    size(500, 500)

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
    margin = 30 * scale_ * 1

    # STYLE PARAMETERS
    stroke_weight = 2 * scale_

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenRandom(pg, fills.ScannerFill(pg))
    pen = pens.PenBasic(pg, fills.BasicFill(pg))

    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    colorMode(HSB, 360, 100, 100)
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
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, img
    
    pen.stroke(colors[4])
    pen.noFill()
    
    pen.fill(colors[3])
    pen.strokeWeight(stroke_weight)
    
    seeds = [int(random(100000)) for _ in range(100)]
    
    rseed = int(random(1000))
    
    for i in range(1):
        randomSeed(rseed)
        sizes = [random(pwidth / 4, pwidth / 1.5) for _ in range(3)]
        sizes = sorted(sizes, reverse=True)
        for j, j_ in enumerate(range(2, -1, -1)):
            pen.fill((colors[3][0] + j * 5, colors[3][1] + j_ * 10, colors[3][2] - j_ * 10))
            c = PVector(pwidth / 2, pheight / 2)
            rp = gm.CircularRandomPolygon(c, sizes[j], int(random(4,8)))
            pen.shape(rp.points)
    
    
    
        
    pen.noStroke()
    pen.fill((0,0,75,3))
    for _ in range(1000 * scale_):
        
        rp = gm.CircularRandomPolygon(PVector(random(-100, pwidth+100), random(-100, pheight+100)), random(25,150), int(random(4,8)))
        pen.shape_mix(rp.points)
    
    pen.noFill()
    pen.strokeWeight(1)
    
    for _ in range(1000 * scale_):
        pen.stroke((0,0,75,13))
        pen.circle(PVector(random(-500, pwidth + 500), random(-500, pheight + 500)), random(200,1000))
        
    pen.strokeWeight(1)
    for _ in range(1000 * scale_):
        pen.stroke((0,0,66,13))
        pen.line(PVector(random(-500, pwidth + 500), random(-500, pheight + 500)), PVector(random(-500, pwidth + 500), random(-500, pheight + 500)))
    
    
    
    
def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, img
    if flag:
        
        colors, palette_id = tools.get_color_palette()
        colors, palette_id = tools.get_color_palette(4282)
        colors = tools.hex_to_hsb(colors)
        seed = int(random(100000))
        seed = 81321
        noiseSeed(seed)
        randomSeed(seed)
        
        flag = False
        pg.beginDraw()

        # Set background color
        #pg.fill(*colors[1])
        pg.fill(0,5,95)
        pg.fill(*colors[4])
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

        draw2()

        pg.loadPixels()
        tools.noisify_brightness(pg.pixels, pg, noise=0.045)
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
