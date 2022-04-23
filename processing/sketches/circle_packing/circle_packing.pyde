def hex_to_rgb(h):
    if isinstance(h, list):
        cols = []
        for h_ in h:
            h_ = h_.lstrip('#')
            cols.append(tuple(int(h_[i:i+2], 16) for i in (0, 2, 4)))
        return cols
        
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

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
        
def pack_circles(w, h, n, minr, maxr, strk_col, fill_col=None):
    circles = []
    
    for _ in range(n):
        for _ in range(100):
            flag = False
            c = Circle(random(w), random(h), maxr, strk_col, fill_col)
            
            if c.inside_list(circles):
                continue
            
            
            while c.intersects_list(circles) or c.x + c.r >= w or c.x - c.r <= 0 or c.y + c.r >= h or c.y - c.r <= 0:
                c.r -= 1
                if c.r < minr:
                    flag = True
                    break
                
            if flag:
                continue
                
            circles.append(c)
            break
        
    return circles
        
        
    

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
    global flag, bg_col, strk_col, pwidth, margin, pheight
    
    if flag:
        print('Generating new set of packed circles!')
        flag = False
        circles = pack_circles(pwidth, pheight, 1000, 2, 100, strk_col)
        
        pg.beginDraw()
    
        # Set background color
        pg.fill(*bg_col)
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        
        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)
    
        for circle in circles:
            circle.draw(pg)
            
            
        # End drawing on PGraphics    
        pg.popMatrix()
        pg.endDraw()
        
        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        pg.save("template.png")
