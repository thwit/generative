import pens
import fills
import geometry as gm
import tools

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight
    size(600, 600)

    #### COLOR DEFINITIONS
    colors = ['#2a241b','#67482f','#ac3d20','#ebddd8','#3a3f43']
    bg_col = '#fffffa'
    strk_col = '#000000'
    
    bg_col = tools.hex_to_hsb(bg_col)
    strk_col = tools.hex_to_hsb(strk_col)
    colors = tools.hex_to_hsb(colors)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 2
    
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
    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    pg.endDraw()
    pen = pens.PenRandom(pg, fills.ScannerFill(pg))
    
    flag = True
    
def keyReleased():
    global flag
    
    if key == ENTER:
        flag = True
    
def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
    
    if flag:
        print('Generating new set of Mondrian squares')
        flag = False
        mondrian = gm.Mondrian(0, 0, pwidth, pheight, 10, strk_col, fill_col=bg_col, n_col=int(random(20,100)), colors=[(0,0,0)], margin=5, circle_pack=False)
        
        pg.beginDraw()
    
        pen.strokeWeight(stroke_weight)
        
        # Set background color
        pg.fill(*bg_col)
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
        pen.noFill()
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
        pen.stroke(strk_col)
        mondrian.generate()
        mondrian.draw(pen)
        
        print('New set of Mondrian squares generated and drawn')
        pg.loadPixels()
        tools.noisify_brightness(pg.pixels, pg)
        pg.updatePixels()
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        pg.save("template.png")
