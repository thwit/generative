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
    margin = 30 * scale_ * 0

    # STYLE PARAMETERS
    stroke_weight = 1

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBrush(pg, fills.BasicFill(pg))
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
    
    img = loadImage('starry.jpg')

    if img.width > pwidth and img.width - pwidth > img.height - pheight:
        img.resize(pwidth,0)
    else:
        img.resize(0, pheight)
        
    print(img.width, pwidth)
    print(img.height, pheight)



def keyReleased():
    global flag

    if key == ENTER:
        flag = True
        
def mean_color(img, alpha_=255):
    
    img.loadPixels()
    h = 0
    s = 0
    b = 0
    
    for c in img.pixels:
        h += pg.hue(c)
        s += pg.saturation(c)
        b += pg.brightness(c)
    
    h /= len(img.pixels)
    s /= len(img.pixels)
    b /= len(img.pixels)
    
    return (h, s, b, alpha_)

def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, img
    
    pen.noStroke()
    pen.noFill()
    
    pen.stroke((0,0,0))
    
    step = img.width // 15
    
    img.loadPixels()
    minh = pg.hue(min(img.pixels, key=lambda p: pg.hue(p)))
    maxh = pg.hue(max(img.pixels, key=lambda p: pg.hue(p)))
    
    mins = pg.saturation(min(img.pixels, key=lambda p: pg.saturation(p)))
    maxs = pg.saturation(max(img.pixels, key=lambda p: pg.saturation(p)))
    
    minb = pg.brightness(min(img.pixels, key=lambda p: pg.brightness(p)))
    maxb = pg.brightness(max(img.pixels, key=lambda p: pg.brightness(p)))

    for x in range(0, img.width, step):
        for y in range(0, img.height, step):
            #h = pg.hue(img.get(x, y))
            s = pg.saturation(img.get(x, y))
            #b = pg.brightness(img.get(x, y))
            
            #col = (h, s, b)
            #pen.fill(col)
            
            v = PVector(x, y)
            
            #for _ in range(int(map(s, maxs, mins, 10, 1))):
            for _ in range(int(map(s, mins, maxs, 10, 1))):
                pen.circle(v + PVector(randomGaussian() * 2, randomGaussian() * 2), random(1, step))
    
    

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, img
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

        draw2()

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
