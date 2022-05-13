from __future__ import division
import pens
import tools
import geometry as gm
import fills

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_
    size(700, 700)

    #### COLOR DEFINITIONS
    colors = ['#1f0f12','#6e0d16','#ea2a44','#ca6368','#e4a4a8']
    strk_col = '#fffffa'
    bg_col = '#000000'
    
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
    pen = pens.PenBasic(pg, fills.LineFill(pg))
    
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
    #return sin(col) * noise( col, row) * TWO_PI
    return noise(col, row, strength * size_* noise(col, row)) * TWO_PI

def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, scale_
    
    pen.stroke(strk_col)
    pen.noStroke()
    pen.fill(strk_col)
    
    pen.rect(PVector(250, 250), 250, 250)
    pen.circle(PVector(500, 500), 125)
    

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    if flag:
        flag = False
        pg.beginDraw()
        noiseSeed(int(random(100000)))
    
        
        # Set background color
        pg.fill(*bg_col)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
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
        pg.save("template.png")
