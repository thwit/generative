from __future__ import division
import pens
import tools
import geometry as gm
import fills

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed
    size(720, 840)

    #### SEEDS
    seed = int(random(1000000))
    randomSeed(seed)
    noiseSeed(seed)

    #### COLOR DEFINITIONS
    colors = ['#1f0f12','#6e0d16','#ea2a44','#ca6368','#e4a4a8']
    bg_col = '#fffffa'
    strk_col = '#000000'
    
    bg_col = tools.hex_to_hsb(bg_col)
    strk_col = tools.hex_to_hsb(strk_col)
    colors = tools.hex_to_hsb(colors)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 1
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins around the drawing
    margin = 50 * scale_
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 3
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBasic(pg, fills.BasicFill(pg))
    pen = pens.PenBrush(pg, fills.BasicFill(pg))
    
    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    pg.strokeCap(SQUARE)
    #pg.colorMode(RGB, 255, 255, 255)
    pen.strokeWeight(stroke_weight)
    
    pg.endDraw()
    #pen.set_clean(True)
    #pen.prob = 0
    
    flag = True
    
def keyReleased():
    global flag
    
    if key == ENTER:
        flag = True
    

def noise_(col, row):
    strength = 0.5
    size_ = 1
    col *= 0.05
    row *= 0.05
    return noise(col, row)
    #return sin(col) * noise( col, row) * TWO_PI
    return noise(col, row, strength * size_* noise(col, row)) * TWO_PI

def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, scale_, seed
    
    flow = gm.FlowField(0, 0, pwidth, pheight)
    flow.set_angles(noise_)
    
    grid = flow.grid
    pen.fill(strk_col)

    r = None

    while r is None or pwidth % (r * 2) != 0 or pheight % (r * 2) != 0:
        r = int(random(10, 100))

    #r = 2 * scale_
    s = 2 * (r - 3)
    n = pwidth / (r * 2)
    
    r = 100

    pen.noStroke()
    pen.noFill()
    pen.stroke(colors[0])
    for x in range(r, pwidth, r * 2):
        for y in range(r, pheight, r * 2):
            v = PVector(x,y)
            u = PVector(0, 1)
            u.rotate(flow.angle(v))
            
            v_ = v + u * 20
            
            pen.line(v, v_, d=5)
        

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed
    if flag:
        flag = False
        pg.beginDraw()
        noiseSeed(int(random(100000)))
    
        
        # Set background color
        pen.fill(bg_col)
        pen.noStroke()
        pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pen.noFill()
        print('ye')
        
        
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

        tools.save_image(pg, seed)
