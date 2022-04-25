import pens
import geometry as gm
import tools

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight
    size(600, 600)

    #### COLOR DEFINITIONS
    colors = ['#2a241b','#67482f','#ac3d20','#ebddd8','#3a3f43']
    bg_col = '#a99384'
    strk_col = '#000000'
    
    bg_col = tools.hex_to_rgb(bg_col)
    strk_col = tools.hex_to_rgb(strk_col)
    colors = tools.hex_to_rgb(colors)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 3
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins around the drawing
    margin = 30 * scale_
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 3
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.Pen3(pg)
    
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
        mondrian = gm.Mondrian(0, 0, pwidth, pheight, 5, strk_col, fill_col=None, n_col=10, colors=colors, margin=5, circle_pack=True)
        
        pg.beginDraw()
    
        pen.strokeWeight(stroke_weight)
        # Set background color
        pg.fill(*bg_col)
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
    
        mondrian.generate()
        mondrian.draw(pen)
        
        print('New set of Mondrian squares generated and drawn')
            
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        pg.save("template.png")
