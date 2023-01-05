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
    
def update(objects, s):
    global pen, colors
    
    
    # T: T-intersectionr
    # X: X-intersection
    a = 'FX+FX+'
    r = {'X': 'X+[FFY]F',
         'Y': 'F[FFX]-YZ',
         'Z': 'X+F[FFFZ-Y]'}
    
    n = 7
    for _ in range(n):
        tmp = ""
        for i, c in enumerate(a):
            if random(1) < 0.9 or c in '[]':
                tmp += r.get(c, c)
            else:
                tmp += r.get('X', c)
        a = tmp
        
    #print(a)
    angle = HALF_PI * 1.03
    linelength = 75
    pen.stroke((0,0,100,50))
    pg.pushMatrix()
    pg.translate(pwidth / 2, pheight / 2)
    for c in a:
        if c == 'F':
            pg.line(0, 0, 0, linelength)
            pg.translate(0, linelength)
        elif c == f:
            pg.translate(0, linelength)
        elif c == '+':
            pg.rotate(angle)
        elif c == '-':
            pg.rotate(-angle)
        elif c == '[':
            pg.pushMatrix()
        elif c == ']':
            pg.popMatrix()
    
    linelength = 25
    pen.stroke((200,50,100,125))
    
    for c in a:
        if c == 'F':
            pg.line(0, 0, 0, linelength)
            pg.translate(random(linelength), linelength * 2)
        elif c == f:
            pg.translate(0, linelength)
        elif c == '+':
            pg.rotate(angle / 1.1)
        elif c == '-':
            pg.rotate(-angle * 1.1)
        elif c == '[':
            pg.pushMatrix()
        elif c == ']':
            pg.popMatrix()
            
    pg.popMatrix()
    
    x, y = -13, -7
    ftsize = 12
    for c in a:
        pg.textSize(ftsize)
        if c in '[]':
            pg.fill(0,100,100)
        elif c in 'FXYZ':
            pg.fill(0,0,100)
        elif c in '+-':
            pg.fill(100,100,100)
        pg.text(c, x, y)
        x += ftsize
        if x > pwidth:
            x = random(-13,-5)
            y += ftsize
       

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, roads, s
    
    
        
    #print(palette_id)
    
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
            for i in range(100):
                pg.beginDraw()
                pen.noStroke()
                pen.fill((0,0,0))
                pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
                update(roads, s)
                pg.endDraw()
                
                tools.save_image(pg, str(i).zfill(4))
        elif key == 'h':
            colors, palette_id = tools.get_color_palette()
            
            colors = tools.hex_to_hsb(colors)
            
    
          
    
    flag = False
