from texture_draw import PenLine

class Square:
    def __init__(self, x, y, w, h, strk_col, fill_col):
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
        
        pg.stroke(*self.strk_col)
        pg.fill(*self.fill_col)
        pg.rect(self.x, self.y, self.w, self.h)
        
        PenLine(PVector(self.x, self.y), PVector(self.x + self.w, self.y)).draw(pg, self.strk_col)
        PenLine(PVector(self.x, self.y), PVector(self.x, self.y + self.h)).draw(pg, self.strk_col)
        
        PenLine(PVector(self.x + self.w, self.y), PVector(self.x + self.w, self.y + self.h)).draw(pg, self.strk_col)
        PenLine(PVector(self.x, self.y + self.h), PVector(self.x + self.w, self.y + self.h)).draw(pg, self.strk_col)
        
        
        
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
    global colors, strk_col, fill_col, pwidth, pheight
    squares = [Square(0,0,pwidth, pheight, strk_col, fill_col)]
    
    for _ in range(7):
        for i in range(len(squares)-1, -1, -1):
            sq_ = squares[i].split_random(25)
            if sq_:
                squares.append(sq_)
    
    for _  in range (3):
        for col in colors:
            squares[int(random(len(squares)))].fill_col = col
    
    return squares
        

def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin
    size(600, 600)
    colors = ['#282b37','#6a4a42','#728f57','#c4ccc2','#f5f9fa']

    b = '#dde3de'
    #### COLOR DEFINITIONS
    bg_col = '#f5f9fa'
    strk_col = '#282b37'
    fill_col = bg_col
    
    bg_col = hex_to_rgb(bg_col)
    strk_col = hex_to_rgb(strk_col)
    fill_col = hex_to_rgb(fill_col)
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
