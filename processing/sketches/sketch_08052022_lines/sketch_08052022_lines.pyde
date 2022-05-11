from __future__ import division
import pens
import tools
import geometry as gm
import fills

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, dw, dh, rows, cols, grid_margin, tw, th, scale_
    size(500, 500)

    #### COLOR DEFINITIONS
    colors = ['#2a241b','#67482f','#ac3d20','#ebddd8','#3a3f43']
    bg_col = '#fffffa'
    strk_col = '#000000'
    fill_col = '#B22727'
    
    bg_col = tools.hex_to_hsb(bg_col)
    strk_col = tools.hex_to_hsb(strk_col)
    colors = tools.hex_to_hsb(colors)
    fill_col = tools.hex_to_hsb(fill_col)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 3
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    #pwidth, pheight = 500, 500
    
    # Margins around the drawing
    margin = 100
    
    # Margins between each grid cell
    grid_margin = 5
    
    # Outer size of grid cell
    tw = 25
    th = 100
        
    # Inner size of grid cell
    dw = tw - grid_margin
    dh = th - grid_margin
    
    # Number of rows and columns in grid
    rows = int(pheight // th)
    cols = int(pwidth // tw)
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 1
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenRandom(pg, fills.ScannerFill(pg))
    pen = pens.PenBasic(pg, fills.BasicFill(pg))
    
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
    
def draw3():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, dw, dh, rows, cols, grid_margin, scale_
    pen.noFill()
    pen.stroke((0,0,0))
    pen.rect(PVector(0,0), pwidth, pheight)
    #pg.rectMode(CENTER)

    c = PVector(pwidth / 2, pheight / 2)
    
    inc = 0.005
    t = 0
    
    n = 4
    
    s = pwidth // n

    marg = 25 * scale_
    
    points = []
    
    for x in range(0, pwidth, s):
        for y in range(0, pheight, s):
            ul = PVector(x + marg / 2, y + marg / 2)
            for _ in range(4):
                pen.rect(ul, s - marg, s - marg)
                offset = (c - PVector(ul.x + (s - marg) / 2, ul.y + (s - marg) / 2)).normalize() * 12
                
                points.extend(pen.rectPanto(ul, s - marg, s - marg))   
                ul_new = ul + offset
                
                ul = ul_new


    x, y = tools.to_panto_a4(points, pwidth, pheight)
    
    print 'x =', x
    print 'y =', y
    
    pen.noFill()


def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    if flag:
        flag = False
        pg.beginDraw()
    
        
        # Set background color
        pg.fill(0,0,50)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
        pen.fill(bg_col)
        pen.noStroke()
        pen.rect(PVector(-3, -3), pwidth + margin * 2 + 10, pheight + margin * 2 + 10)
        pen.noFill()
        
        
        pen.stroke(strk_col)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
        
        draw3()
        
        pg.loadPixels()
        #tools.noisify_brightness(pg.pixels, pg)
        pg.updatePixels()
           
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        
        pg.save("template.png")
