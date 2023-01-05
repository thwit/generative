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
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed, palette_id, penb, roads, s, frames, dt
    size(500, 500)
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
    
    for _ in range(25):
        c = gm.Circle(random(pwidth), random(pheight), 7, random(-1, 1), random(-1, 1))
        if not c.intersects_list(roads):
            roads.append(c)
    
    #roads.append(Road([Car(0, pheight / 2, 1, 0)]))
    
    flag = True
    frameRate(1)
    s = 0
    dt = 1.25
    
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

    if key == ENTER:
        flag = True

def updatesssss(objects, s):
    global pen, colors
    
    
    # T: T-intersection
    # X: X-intersection
    a = 'A'
    r = {'X': '[FFFA]FF[+FFFA][++FFFA][+++FFFA]',
         'T': '[A][+A][++A]',
         'A': '[FF[+FA][-AF]FFA]'}
    
    n = 3
    for _ in range(n):
        tmp = ""
        for c in a:
            tmp += r.get(c, c)
        a = tmp
    angle = 90
    linelength = 5
    pg.pushMatrix()
    pg.translate(pwidth / 2, pheight / 2)
    for c in a:
        if random(1) < 0.25:
            angle = 45
        else:
            angle = 90
        if c == 'F':
            pg.line(0, 0, 0, linelength)
            pg.translate(0, linelength)
        elif c == '+':
            pg.rotate(radians(angle))
        elif c == '-':
            pg.rotate(radians(-angle))
        elif c == '[':
            pg.pushMatrix()
        elif c == ']':
            pg.popMatrix()
            
    pg.popMatrix()

    
def update1(roads, s):
    global dt, pen, pg
    
    ticked = set()
    
    for c in roads:
        intersects = c.intersects_list(roads)
        
        if not intersects or intersects and intersects not in ticked:
            c.x += c.vx * dt
            c.y += c.vy * dt
            c.x = c.x % pwidth
            c.y = c.y % pheight
            ticked.add(c)
            
            
            
        closest = c.closest(roads)
        pen.circle(PVector(c.x, c.y), c.r-2)
        
        pen.line(PVector(c.x, c.y), PVector(closest.x, closest.y))
            
        
            
def update(roads, s):
    
    

def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed, palette_id, roads, s
    
    
    pg.beginDraw()
        
    #print(palette_id)
    
    # Set background color
    pg.fill(0,0,100)
    pg.noStroke()
    pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
    pg.noFill()
    
    
    pen.stroke(strk_col)
    update(roads, s)
    s += 1
    
    
    pg.endDraw()
    
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    
    
    #colors, palette_id = tools.get_color_palette()
    #colors = tools.hex_to_hsb(colors)
    
    if keyPressed:
        if (key == 's'):
            tools.save_image(pg, seed, palette_id)
