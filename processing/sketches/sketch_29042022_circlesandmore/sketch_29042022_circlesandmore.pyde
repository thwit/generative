from __future__ import division
import pens
import tools
import geometry as gm
import fills

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight
    size(600, 700)

    #### COLOR DEFINITIONS
    colors = ['#2a241b','#67482f','#ac3d20','#ebddd8','#3a3f43']
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
    margin = 75 * scale_
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 1
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenRandom(pg, fills.ScannerFill(pg))
    
    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
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
    

def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight

    r = 100
    step = int((pwidth-r)/80)
    for x in range(r,pwidth-r, step):
        pen.circle(PVector(x, r), r)
        
    for x in range(r,pwidth-r, step):
        pen.circle(PVector(x, pheight-r), r)
    
    i = 0
    i_step = step / (PVector(r, r)-PVector(pwidth-r, pheight-r)).mag()
    
    while (i+i_step <= 1):
        x = lerp(r, pwidth-r, i)
        y = lerp(r, pheight-r, i)
        pen.circle(PVector(x, y), r)
        i += i_step
        
def draw3():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    
    y_step = 25
    skip_y = int(random(1, pheight/y_step))
    skip_x = int(random(1, pwidth/y_step))
    
    rv = PVector(y_step * int(random(1, pwidth/y_step)), y_step * int(random(1, pheight/y_step)))
    rw = int(random(1, (pwidth - rv.x)/y_step)) * y_step
    rh = int(random(1, (pheight - rv.y)/y_step)) * y_step
    
    pen.fill((0,0,0))
    pen.rect(rv, rw, rh)
    pen.noFill()
    
    for y in range(0, pheight, y_step):
        
        x = 0
        while x < pwidth:
            if (not rv.x - y_step <= x < rv.x + rw + y_step or \
               not rv.y - y_step <= y < rv.y + rh + y_step) and \
               (not y_step * skip_x <= x <= y_step * (skip_x+1) or y > y_step * skip_y):
                pen.line(PVector(x, y), PVector(x + random(-2, 2), y + y_step))
            x += random(1, 3.5)


def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    if flag:
        flag = False
        pg.beginDraw()
    
        
        # Set background color
        pg.fill(0,0,80)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
        pen.fill(bg_col)
        pen.noStroke()
        pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pen.noFill()
        
        
        pen.stroke(strk_col)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
        
        draw3()
        
        #pg.loadPixels()
        #tools.noisify_brightness(pg.pixels, pg)
        #pg.updatePixels()
           
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        pg.save("template.png")
