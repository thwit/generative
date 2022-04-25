from __future__ import division
import pens
import tools
import geometry as gm
import fills

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight
    size(600, 600)

    #### COLOR DEFINITIONS
    colors = ['#2a241b','#67482f','#ac3d20','#ebddd8','#3a3f43']
    bg_col = '#fffffa'
    strk_col = '#000000'
    
    bg_col = tools.hex_to_rgb(bg_col)
    strk_col = tools.hex_to_rgb(strk_col)
    colors = tools.hex_to_rgb(colors)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 1
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins around the drawing
    margin = 30 * scale_
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 1
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBasic(pg, fills.LayerFill(pg))
    #pen.set_clean(True)
    #pen.prob = 0
    
    flag = True
    
def keyReleased():
    global flag
    
    if key == ENTER:
        flag = True
        
        
def draw1():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    pen.prob = 0.25
    s = 50
    s_ = 15
    r_ = 125
    c = PVector(pwidth / 2, pheight / 2)
    for r in range(r_, 25, -s_):
        pen.circle(c, r)
        c = PVector(c.x, c.y + s)
        
    c = PVector(pwidth / 2, pheight / 2)
    for r in range(r_, 25, -s_):
        pen.circle(c, r)
        c = PVector(c.x, c.y - s)
    
    c = PVector(pwidth / 2, pheight / 2)
    for r in range(r_, 25, -s_):
        pen.circle(c, r)
        c = PVector(c.x + s, c.y)
        
    c = PVector(pwidth / 2, pheight / 2)
    for r in range(r_, 25, -s_):
        pen.circle(c, r)
        c = PVector(c.x - s, c.y)
            
def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    cp = gm.CirclePack(0, 0, pwidth, pheight, 500, 5, pwidth/3)
    circles = cp.generate()
    for c in circles:
        if random(1) < 0.2:
            pen.fill(colors[int(random(len(colors)))])
        c.draw(pen)
        pen.noFill()
            

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    
    if flag:
        flag = False
        mondrian = gm.Mondrian(0, 0, pwidth, pheight, 5, strk_col, fill_col=None, n_col=10, colors=colors, margin=5, circle_pack=True)
        
        pg.beginDraw()
    
        pen.strokeWeight(stroke_weight)
        pen.stroke(strk_col)
        # Set background color
        pen.fill(bg_col)
        pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pen.noFill()
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
        
        draw2()
        
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        pg.save("template.png")
