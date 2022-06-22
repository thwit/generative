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
    global flow, flow2, img, pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id, visited, v
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
    scale_ = 1

    # PGraphics drawing size
    pwidth, pheight = width * scale_, height * scale_

    # Margins around the drawing
    margin = 30 * scale_ * 0

    # STYLE PARAMETERS
    stroke_weight = 5

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
    
    img = loadImage('IMG_1632.JPG')

    if img.width > pwidth and img.width / pwidth > img.height / pheight:
        img.resize(pwidth,0)
    else:
        img.resize(0, pheight)
        
    print(img.width, pwidth)
    print(img.height, pheight)
    
    pg.beginDraw()
    
    #pg.image(img, 0, 0)
    pg.endDraw()

    flow = gm.FlowField(0, 0, pwidth + 201, pheight + 201)
    flow.set_angles(noise_)
    
    noiseSeed(seed)
    
    flow2 = gm.FlowField(0, 0, pwidth + 201, pheight + 201)
    flow2.set_angles(noise_)
    
    visited = set()
    v = PVector(random(pwidth), random(pheight))



def keyReleased():
    global flag

    if key == ENTER:
        flag = True
        
def hsb_distance(c0, c1):
    h0 = pg.hue(c0)
    s0 = pg.saturation(c0)
    b0 = pg.brightness(c0)
    
    
    h1 = pg.hue(c1)
    s1 = pg.saturation(c1)
    b1 = pg.brightness(c1)
    
    
    dh = min(abs(h1-h0), 360-abs(h1-h0)) / 360
    ds = abs(s1-s0) / 100
    dv = abs(b1-b0) / 100
    
    return dh*dh+ds*ds+dv*dv

def most_similar_color(v, img, w, h, visited=set()):
    v_start = v - PVector(w / 2, h / 2)
    img.loadPixels()
    
    min_dist = 10000000
    min_pos = v
    
    c0 = img.get(int(v.x), int(v.y))
    
    for x in range(int(v_start.x), int(v_start.x) + w):
        for y in range(int(v_start.y), int(v_start.y) + h):
            if x == v.x and y == v.y or (x, y) in visited or x < 0 or x > pwidth or y < 0 or y > pheight:
                continue
            try:
                c1 = img.pixels[y*pwidth+x]
            except Exception:
                continue
            distance = hsb_distance(c0, c1)
            if distance < min_dist:
                min_dist = distance
                min_pos = PVector(x, y)
                
    visited.add((min_pos.x, min_pos.y))
    return min_pos
        
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
    
    return (h, s, b, alpha_);

def draw():
    global flow, flow2, img, flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, visited, v

    pg.beginDraw()
    pen.noFill()
    pg.noFill()
    
    w = int(random(10, 50))
    h = int(random(10, 150))
    
    h = int(constrain(map(frameCount, 0, 60 * 3, 250, 20), 20, 250))
    h = 30
    
    x = int(random(img.width - w))
    y = int(random(img.height - h))
    
    v_ = most_similar_color(v, img, 25, 25, visited)
    
    
    #col = colors[int(random(len(colors)))]
    col = img.get(int(v.x), int(v.y))
    col = (pg.hue(col), pg.saturation(col), pg.brightness(col))
    pen.stroke(col)

    pen.line(v, v_)
    print(v)
    v = v_
    #pen.circle(v, max((v-v_).mag(), 5))

    
    '''
    d = int(constrain(map(frameCount, 0, 60 * 3, 50, 7), 50, 7))
    d = 7
    pen.line(v, v_, d)
    '''
    
    
    pg.endDraw()
    # Display final drawing and save to .png in same folder
    fill(0,5,95)
    rect(0,0,width,height)
    image(pg, 0, 0, width, height)
    noFill()
    
    if keyPressed:
        if (key == 's'):
            tools.save_image(pg, seed, palette_id)
