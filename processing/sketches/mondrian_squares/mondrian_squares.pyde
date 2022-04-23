from texture_draw import PenLine

class Circle:
    def __init__(self, x, y, r, strk_col, fill_col=None):
        self.x = x
        self.y = y
        self.r = r
        self.strk_col = strk_col
        self.fill_col = fill_col
        
    def intersects(self, other):
        return (self.x-other.x)**2 + (self.y-other.y)**2 <= (self.r+other.r)**2 
    
    def inside(self, x, y):
        return (sq(self.x - x) + sq(self.y - y)) < sq(self.r)
    
    def inside_list(self, circles):
        for c in circles:
            if c.inside(self.x, self.y):
                return True
        return False
    
    def intersects_list(self, circles):
        for c in circles:
            if self.intersects(c):
                return True
        return False
    
    def draw(self, pg):
        pg.stroke(*self.strk_col)
        if self.fill_col is None:
            pg.noFill()
        else:
            pg.fill(*self.fill_col)
        
        pg.circle(self.x, self.y, self.r * 2)
        
def pack_circles(x, y, w, h, n, minr, maxr, strk_col, fill_col=None):
    circles = []
    
    for _ in range(n):
        for _ in range(100):
            flag = False
            c = Circle(random(x, x+w), random(y, y+h), maxr, strk_col, fill_col)
            
            if c.inside_list(circles):
                continue
            
            
            while c.intersects_list(circles) or c.x + c.r >= x+w or c.x - c.r <= x or c.y + c.r >= y+h or c.y - c.r <= y:
                c.r -= 1
                if c.r < minr:
                    flag = True
                    break
                
            if flag:
                continue
                
            circles.append(c)
            break
        
    return circles

class Square:
    def __init__(self, x, y, w, h, strk_col, fill_col=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.strk_col = strk_col
        self.fill_col = fill_col
        
    def split_random(self, step):
        if random(1) < 0.15:
            return
        
        if random(1) < 0.5 and self.w >= (2 * step):
            return self.split_x(int(random(step, self.w - step)))
        elif self.h >= (2 * step):
            return self.split_y(int(random(step, self.h - step)))
            
    def split_x(self, s):
        self.w = self.w - s
        return Square(self.x + self.w, self.y, s, self.h, self.strk_col, self.fill_col)
    
    
    def split_y(self, s):
        self.h = self.h - s
        return Square(self.x, self.y + self.h, self.w, s, self.strk_col, self.fill_col)
    
    def draw(self, pg):
        
        if self.fill_col is not None:
            self.circle_fill(pg)
            
        pg.noFill()
        #pg.rect(self.x, self.y, self.w, self.h)
        
        #PenLine(PVector(self.x, self.y), PVector(self.x + self.w, self.y)).draw(pg, self.strk_col)
        #PenLine(PVector(self.x, self.y), PVector(self.x, self.y + self.h)).draw(pg, self.strk_col)
        
        #PenLine(PVector(self.x + self.w, self.y), PVector(self.x + self.w, self.y + self.h)).draw(pg, self.strk_col)
        #PenLine(PVector(self.x, self.y + self.h), PVector(self.x + self.w, self.y + self.h)).draw(pg, self.strk_col)
        
        pg.noFill()
        pg.stroke(*self.strk_col)
        pg.rect(self.x, self.y, self.w, self.h)
        
    def circle_fill(self, pg):
        for c in pack_circles(self.x, self.y, self.w, self.h, 100, 2, 100, self.fill_col):
            c.draw(pg)
        
        
        
def hex_to_rgb(h):
    if isinstance(h, list):
        cols = []
        for h_ in h:
            h_ = h_.lstrip('#')
            cols.append(tuple(int(h_[i:i+2], 16) for i in (0, 2, 4)))
        return cols
        
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def mondrian():
    global colors, strk_col, pwidth, pheight
    squares = [Square(0,0,pwidth, pheight, strk_col)]
    
    for _ in range(7):
        for i in range(len(squares)-1, -1, -1):
            sq_ = squares[i].split_random(25)
            if sq_:
                squares.append(sq_)
    
    colored = []
    for _  in range (3):
        for col in colors:
            r = int(random(len(squares)))
            squares[r].fill_col = col
            
    
    return squares
        

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin
    size(600, 600)

    #### COLOR DEFINITIONS
    colors = ['#2a241b','#67482f','#ac3d20','#ebddd8','#3a3f43']
    bg_col = '#a99384'
    strk_col = '#000000'
    
    bg_col = hex_to_rgb(bg_col)
    strk_col = hex_to_rgb(strk_col)
    colors = hex_to_rgb(colors)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 1
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins around the drawing
    margin = 30 * scale_
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 2
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    
    flag = True
    
def keyReleased():
    global flag
    
    if key == ENTER:
        flag = True
    
def draw():
    global flag, bg_col, pwidth, margin, pheight
    
    if flag:
        print('Generating new set of Mondrian squares')
        flag = False
        squares = mondrian()
        
        pg.beginDraw()
    
        pg.strokeWeight(2)
        # Set background color
        pg.fill(*bg_col)
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
    
        for square in squares:
            square.draw(pg)
            
            
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        pg.save("template.png")
