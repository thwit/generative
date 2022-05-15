from __future__ import division
import pens
import tools
import geometry as gm
import fills

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, dw, dh, rows, cols, grid_margin, tw, th, bg_col2
    size(600, 600)

    #### COLOR DEFINITIONS
    colors = ['#F7C85E', '#F3EBD6', '#EABA92', '#4A3635', '#BA8041']
    #colors = ['#678b8b','#96a4c1','#c3d2e5','#f3a195','#7d6f86']
    #colors = ['#161f1f','#1e0b08','#5e100a','#b3320b','#d75c1e']
    bg_col = '#fffffa'
    #bg_col = '#3a1814'
    strk_col = '#000000'
    fill_col = '#B22727'
    
    bg_col = tools.hex_to_hsb(bg_col)
    strk_col = tools.hex_to_hsb(strk_col)
    colors = tools.hex_to_hsb(colors)
    fill_col = tools.hex_to_hsb(fill_col)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 2
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
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
    stroke_weight = 3
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBasic(pg, fills.CurveFill(pg))
    #pen = pens.PenBasic(pg, fills.BasicFill(pg))
    
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
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, dw, dh, rows, cols, grid_margin, bg_col2
    pen.noFill()
    pen.noStroke()
    
    v1 = PVector(0, 0)
    v2 = PVector(pwidth, pheight)
    
    s = pwidth // 3
    
    for x in range(0, pwidth, s):
        for y in range(0, pheight, s):
            
            grid_col = colors[int(random(len(colors)))]
            element_col = colors[int(random(len(colors)))]
            
            while element_col == grid_col:
                element_col = colors[int(random(len(colors)))]
            
            pen.fill(grid_col)
            #pen.stroke(grid_col)
            pen.rect(PVector(x, y), s, s)
            
            pen.fill(element_col)
            #pen.stroke(element_col)
            if random(1) < 0.2:
                pen.circle(PVector(x + s / 2, y + s / 2), s / 3)
            elif random(1) < 0.15:
                pen.rect(PVector(x + s / 4, y + s / 4), s / 2, s / 2)
            elif random(1) < 0.15:
                if random(1) < 0.5:
                    pen.rect(PVector(x + s / 4, y + s / 4), s / 4, s / 4)
                    pen.rect(PVector(x + s - s / 2, y + s - s / 2), s / 4, s / 4)
                else:
                    pen.rect(PVector(x + s / 2, y + s / 4), s / 4, s / 4)
                    pen.rect(PVector(x + s / 4, y + s / 2), s / 4, s / 4)
                


def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, bg_col2
    if flag:
        flag = False
        for _ in range(1):
            pg.beginDraw()
        
            
            # Set background color
            pg.fill(0,0,70)
            pg.noStroke()
            pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
            pg.noFill()
            pen.fill(bg_col)
            pen.noStroke()
            pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
            pen.noFill()
            print('bg')

            pen.stroke(strk_col)
            
            # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
            pg.pushMatrix()
            pg.translate(margin, margin)
            
            
            
            seed = int(random(100000))
            randomSeed(seed)
            
            draw2()
            
            pg.loadPixels()
            #tools.noisify_brightness(pg.pixels, pg)
            pg.updatePixels()
            
            # End drawing on PGraphics    
            pg.popMatrix()
            pg.endDraw()
            
            # Display final drawing and save to .png in same folder
            image(pg, 0, 0, width, height)
            #pg.save(str(seed) + '.png')
            tools.save_image(pg, seed)
