from __future__ import division
import pens
import tools
import geometry as gm
import fills

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_
    size(1000, 500)

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
    
    flow = gm.FlowField(0, 0, pwidth, pheight)
    flow.set_angles(noise_)
    
    grid = flow.grid
    pen.fill(strk_col)
    for col in range(0, flow.num_columns, 4):
        break
        for row in range(0, flow.num_rows, 4):
            
            pen.circle(flow.grid[col][row].pos, 2)

    pen.stroke(strk_col)
    circles = []
    
    for _ in range(5000):
        r = random(5,50)
        x, y = random(pwidth), random(pheight)
        
        #points = flow.curve(PVector(random(pwidth), random(pheight)), int(random(8,16)) * scale_, 0.015 / scale_)
        points = flow.curve(PVector(x,y), 500, 0.01)
        
        #pen.stroke((358, map(points[0].y, 0, pheight, 10, 100), map(points[0].y, 0, pheight, 100, 10)))
        #pen.fill((358, map(points[0].y, 0, pheight, 10, 73), map(points[0].y, 0, pheight, 100, 23)))
        
        pen.noFill()
        col = colors[int(random(len(colors)))]
        pen.stroke(col)
    
    
        c_ = []
        ps = []
        
        for i, p in enumerate(points):
            #pen.stroke((358,  map(i, 0, len(points), 23, 73), map(i, 0, len(points), 73, 23)))
            #pen.fill((358,  map(i, 0, len(points), 23, 73), map(i, 0, len(points), 73, 23)))
            
            #pen.stroke((358,  map(p.y, 0, pheight, 10, 73), map(i, 0, len(points), 100, 23)))
            #pen.fill((358,  map(p.y, 0, pheight, 10, 73), map(i, 0, len(points), 100, 23)))
            h = pg.hue(color(*col))
            s = pg.saturation(color(*col))
            b = pg.brightness(color(*col))
            #pen.fill((h, map(p.y, 0, pheight, 0, 100), map(p.y, 0, pheight, 100, 0)))
            
                
            c = gm.Circle(p.x, p.y, r / 2 + 3)
            
            if not c.intersects_list(circles):
                c_.append(c)
                ps.append(p)
                #c.draw(pen)
            else:
                break
        print(len(c_))
        
        if len(c_) < 5 and False:
            continue
        
        
        pen.strokeWeight(r)
        pen.shape_curve(ps)
        
        for i, c in enumerate(c_):
            break
            r_ = map(i, 0, len(c_), 2, 15)
            #r_ = 10
            pen.circle(PVector(c.x, c.y), r_)
            c.r = r_
        circles.extend(c_)
        

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight
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
        pg.save("template.png")
