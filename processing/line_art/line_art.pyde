import random

# draws straight lines pencil-like
def draw_line(x1, y1, x2, y2):
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    x_length = abs(x1-x2)
    y_length = abs(y1-y2)
    div_num = max(x_length, y_length)
    if div_num == 0:
        return
    div_x = x_length/div_num
    div_y = y_length/div_num
    
    div_num = int(div_num)
    for i in range(div_num+1):
        if(x1<x2):
            new_x = x1 + div_x * i
        else:
            new_x = x1 - div_x * i
        if y1 < y2:
            new_y = y1 + div_y * i
        else:
            new_y = y1 - div_y * i
            
        random_dots(new_x, new_y);

def random_dots(dot_x, dot_y):
    dmi = 10
    rand = 0.5
    for _ in range(dmi):
        dir_x = random.uniform(-rand, rand)
        dir_y = random.uniform(-rand, rand)
        new_x = dot_x+dir_x
        new_y = dot_y+dir_y
        circle(new_x, new_y, 0.075)
        
        
def setup():
    size(600, 750)
    fill('#FAF9F5')
    noStroke()
    rect(0,0,width,height)
    stroke('#B21504')

    margin_top = 100
    margin_side = 70
    
    for i in range(90):
        ox = cos(radians(i)) * (width - margin_side * 2)
        oy = cos(radians(i)) * (height - margin_top * 2)
        x = margin_side + ox
        
        if x < width // 2:
            break
        
        draw_line(x, margin_top, x, margin_top + oy)
        
    for i in range(90):
        ox = cos(radians(i)) * (width - margin_side * 2)
        oy = cos(radians(i)) * (height - margin_top * 2)
        x = (width - margin_side) - ox
        
        if x > width // 2:
            break
        
        draw_line(x, margin_top, x, height - margin_top - oy)
        
    for i in range(90):
        ox = cos(radians(i)) * (width - margin_side * 2)
        oy = cos(radians(i)) * (height - margin_top * 2)
        x = margin_side + ox
        y_start = margin_top + oy + 20
        
        if x < width // 2:
            break
        elif y_start > (height - margin_top):
            continue
        
        draw_line(x, y_start, x, height - margin_top)
        
    for i in range(90):
        ox = cos(radians(i)) * (width - margin_side * 2)
        oy = cos(radians(i)) * (height - margin_top * 2)
        x = (width - margin_side) - ox
        y_start = height - margin_top - oy + 20
        
        if x > width // 2:
            break
        elif y_start > (height - margin_top):
            continue
        
        draw_line(x, y_start, x, height - margin_top)
        
        
def setup2():
    size(600, 750)
    fill('#FAF9F5')
    noStroke()
    rect(0,0,width,height)
    stroke('#B21504')

    margin_top = 100
    margin_side = 70
    v_center = PVector(width / 2, height / 2)
    
    v2s = []
    
    for x in [0, width]:
        for y in range(0, height+1, 25):
            v1 = PVector(x, y)
            v2 = v1 + (v_center - v1).normalize().mult(abs(sin(radians(map(y, 0, height, 25, 155)))) * v1.dist(v_center) - 10)
            v2s.append(v2)
            draw_line(v1.x, v1.y, v2.x, v2.y)
            print(v1, v2)
            
    for y in [0, height]:
        for x in range(0, width+1, 25):
            v1 = PVector(x, y)
            v2 = v1 + (v_center - v1).normalize().mult(abs(sin(radians(map(x, 0, width, 25, 155)))) * v1.dist(v_center) - 10)
            v2s.append(v2)
            draw_line(v1.x, v1.y, v2.x, v2.y)
            
    
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def on_segment(self, p, q, r):
        '''Given three colinear points p, q, r, the function checks if 
        point q lies on line segment "pr"
        '''
        if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        return False

    def orientation(self, p, q, r):
        '''Find orientation of ordered triplet (p, q, r).
        The function returns following values
        0 --> p, q and r are colinear
        1 --> Clockwise
        2 --> Counterclockwise
        '''
    
        val = ((q[1] - p[1]) * (r[0] - q[0]) - 
                (q[0] - p[0]) * (r[1] - q[1]))
        if val == 0:
            return 0  # colinear
        elif val > 0:
            return 1   # clockwise
        else:
            return 2  # counter-clockwise
    
    def intersects(self, other):
        '''Main function to check whether the closed line segments p1 - q1 and p2 
        - q2 intersect'''
        p1 = (self.x1, self.y1)
        q1 = (self.x2, self.y2)
        p2 = (other.x1, other.y1)
        q2 = (other.x2, other.y2)
        
        
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)
    
        # General case
        if (o1 != o2 and o3 != o4):
            return True
    
        # Special Cases
        # p1, q1 and p2 are colinear and p2 lies on segment p1q1
        if (o1 == 0 and self.on_segment(p1, p2, q1)):
            return True
    
        # p1, q1 and p2 are colinear and q2 lies on segment p1q1
        if (o2 == 0 and self.on_segment(p1, q2, q1)):
            return True
    
        # p2, q2 and p1 are colinear and p1 lies on segment p2q2
        if (o3 == 0 and self.on_segment(p2, p1, q2)):
            return True
    
        # p2, q2 and q1 are colinear and q1 lies on segment p2q2
        if (o4 == 0 and self.on_segment(p2, q1, q2)):
            return True
    
        return False # Doesn't fall in any of the above cases
    
    def intersects_list(self, other_list):
        for other in other_list:
            if self.intersects(other):
                return True
        return False
    
    def magnitude(self):
        v1 = PVector(self.x1, self.y1)
        v2 = PVector(self.x2, self.y2)
        return (v1 - v2).mag()
    

    def draw(self):
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        draw_line(self.x1, self.y1, self.x2, self.y2)
        
    def draw2(self):
        line(self.x1, self.y1, self.x2, self.y2)


def setup3():
    size(750, 750)
    fill('#FAF9F5')
    noStroke()
    rect(0,0,width,height)
    stroke('#B21504')
    noFill()
    
    lines = []

    for _ in range(100):
        line_ = Line(random.randint(0,width), random.randint(0,height), random.randint(0,width), random.randint(0,height))
        while line_.intersects_list(lines):
            line_ = Line(random.randint(0,width), random.randint(0,height), random.randint(0,width), random.randint(0,height))
        lines.append(line_)

    
    for line_ in lines:
        line_.draw()
        
        
class CCircle:
    def __init__(self, x, y, r, p=None, col='#000000'):
        self.x = x
        self.y = y
        self.r = r
        self.p = p
        self.col = col
    
    def draw(self, child=False):
        if not child:
            noFill()
        else:
            fill(self.col)
        stroke(self.col)
        circle(self.x, self.y, self.r)
        
        if self.p:
            self.p.draw(True)
            
class EEllipse:
    def __init__(self, x, y, w, h, p=None, col='#000000'):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.p = p
        self.col = col
    
    def draw(self, child=False):
        if not child:
            noFill()
        else:
            fill(self.col)
        stroke(self.col)
        ellipse(self.x, self.y, self.w, self.h)
        
        if self.p:
            self.p.draw(True)
        
def setup4():
    size(750, 750)
    clr = '#000000'
    fill('#FAF9F5')
    noStroke()
    rect(0,0,width,height)
    
    step = 50
    r = 40
    r2 = 20
    
    circles = []
    v_center = PVector(width / 2, height / 2)
    
    for x in range(step, width, step):
        for y in range(step, height, step):
            v1 = PVector(x, y)
            v2 = v1 + (v_center - v1).normalize().mult(abs(sin(radians(map(y, 0, height, 25, 155)))) * r2 / 3)
            d = map((v_center - v1).mag(), 0, v_center.mag(), 0, r2)
            p = EEllipse(x, y, r2, d, col=clr)
            circles.append(CCircle(x, y, r, p=p, col=clr))
                           
    for c in circles:
        c.draw()
    
    
    
        
