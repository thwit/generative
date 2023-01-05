from __future__ import division
import random as random_
import math

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

class Intersection:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.queue = []

class Road:
    def __init__(self, cars, intersections):
        self.cars = cars
        self.intersections = intersections
        

class Car:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.c = gm.Circle(x, y, 8)
        self.vx = vx
        self.vy = vy
    
    def tick(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        
def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id, penb, roads, s, frames, dt, grid, lines
    size(750, 750)
    frames = set()
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
    margin = 0 * scale_

    # STYLE PARAMETERS
    stroke_weight = 1

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pg.noSmooth()
    pen = pens.PenBasic(pg, fills.BasicFill(pg))
    #pen = pens.PenBrush2(pg, fills.BasicFill(pg))
    penb = pens.PenBasic(pg, fills.BasicFill(pg))

    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    colorMode(HSB, 360, 100, 100)
    # pg.colorMode(RGB, 255, 255, 255)
    pen.strokeWeight(stroke_weight)
    pg.strokeCap(SQUARE)

    # pen.set_clean(True)
    # pen.prob = 0
    roads = []
    lines = []
    
    for _ in range(25):
        c = gm.Circle(random(pwidth), random(pheight), 7, random(-1, 1), random(-1, 1))
        if not c.intersects_list(roads):
            roads.append(c)
    
    grid = [[0 for _ in range(width)] for _ in range(height)]
    print(len(grid), len(grid[0]))
    #roads.append(Road([Car(0, pheight / 2, 1, 0)]))
    
    flag = True
    frameRate(1000)
    s = 0
    dt = 1.25
    
    
    # Set background color
    pen.fill((0,0,0))
    pen.noStroke()
    if s == 0:
        pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        print('yeet')
    pen.noFill()
    
    
    pen.stroke((0,0,100))
    #pen.circle(PVector(pwidth / 2, pheight / 2), pwidth / 2.2)
    #pen.fill((0,0,0))
    #pen.noStroke()
    for _ in range(0):
        #pen.fill(colors[int(random(len(colors)))])
        crp = gm.CircularRandomPolygon(PVector(pwidth / 2 + 0*random(-200, 200), pheight / 2 + 0*random(-200, 200)), pwidth / 2.5, int(random(4, 10)))
        pen.shape_curve(crp.points + crp.points[:1])
        
    
def line_intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

def keyReleased():
    global flag
    flag = True

def getPixelValue(x, y):
    global pg, pwidth, pheight
    
    if y < 0 or y > pheight or x < 0 or x > pheight:
        raise IndexError
    return pg.pixels[int(y)*width+int(x)]
    
            
def update(roads, s):
    global grid, pen, lines
    
    x, y = random(pwidth), random(pheight)
    
    vx, vy = random(-1, 1), random(-1, 1)
    vx = vy = 0
    while vx == 0 and vy == 0:
        vx = [i for i in range(-1,2)][int(random(3))]
        vy = [i for i in range(-1,2)][int(random(3))]
    #vy = 0
    
    vx += random(-0.15, 0.15)
    vy += random(-0.15, 0.15)
    
    x1, y1 = int(x), int(y)
    xo, yo = x, y
    x2, y2 = None, None
    
    
    old_grid = [[val for val in row] for row in grid]
    nbs = [(0,0), (1,1), (0,1), (-1,1), (1,0), (-1,0), (1,-1), (0, -1), (-1, -1)]
    pg.loadPixels()
    d = 1
    while True:
        try:
            for dx, dy in nbs:
                if brightness(getPixelValue(x + dx, y + dy)) > 0.1:
                    #print(brightness(pg.pixels[(int(y)+dy)*width+(int(x)+dx)]))
                    raise NameError('ø')
        except IndexError:
            break
        except NameError:
            x += vx * d
            y += vy * d
            if d == 1:
                x2, y2 = int(x), int(y)
                x, y = xo, yo
                #print(x1, y1, x2, y2)
                d = -1
                continue
            x1, y1 = x, y
            pen.stroke((0,0,100))
            #print('draw')
            pen.line(PVector(x1, y1), PVector(x2, y2))
            pen.noStroke()
            pen.fill(colors[2])
            #pen.circle(PVector(x1, y1), 5)
            pen.fill(colors[3])
            #pen.circle(PVector(x2, y2), 5)
            break

        x += vx * d
        y += vy * d
    
    #grid = [[x for x  in row] for row in oldgrid]
    #pen.line(PVector(x1, y1), PVector(x2, y2))
        
    
    

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, roads, s
    
    
    pg.beginDraw()
        
    #print(palette_id)
    
    update(roads, s)
    s += 1

    
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    
    
    #colors, palette_id = tools.get_color_palette()
    #colors = tools.hex_to_hsb(colors)
    
    if flag:
        if (key == 's'):
            tools.save_image(pg, 'latest')
        
        elif key == ENTER:
            pen.stroke((0,0,100))
            pen.fill((0,0,0))
            crp = gm.CircularRandomPolygon(PVector(pwidth / 2 + 0*random(-200, 200), pheight / 2 + 0*random(-200, 200)), pwidth / 2, int(random(4, 10)))
            pen.shape(crp.points + crp.points[:1])
        elif key == 'c':
            pen.stroke((0,0,100))
            pen.fill((0,0,0))
            pen.circle(PVector(pwidth / 2 + random(-100, 100), pheight / 2 + random(-100, 100)), random(25,150))
        elif key == 'r':
            pen.noStroke()
            pen.fill((0,0,0))
            pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        elif key == 'h':
            colors, palette_id = tools.get_color_palette()
            
            colors = tools.hex_to_hsb(colors)
            
    
          
    pg.endDraw()  
    
    flag = False
