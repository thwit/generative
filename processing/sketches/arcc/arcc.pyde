import random

# a, b = center of arcc
# c, d =  width, height of arcc (if == then it is a circle arc)
# start, stop = angle to start and stop arcc at. Radians
# mode = https://py.processing.org/reference/arc.html
# stroke_weight = width of the arcc curve
def arcc(a, b, c, d, start, stop, mode=OPEN, stroke_weight=5, strk=(0,0,0)):
    #noFill()
    strokeWeight(stroke_weight)
    if isinstance(strk, str):
        stroke(strk)
    else:
        stroke(*strk)
    arc(a, b, c, d, start, stop, mode)
    
# draws multiple arccs
# only supports circle arccs
# n = number of arccs
# s = spacing between arccs (independent of stroke weight)
def n_arcc(a, b, n, s, start, stop, mode=OPEN, stroke_weight=5, strk=(0,0,0), bg=(255,255,255), margin=0):
    for n_ in range(n, 0, -1):
        c = d = n_ * s
        if isinstance(bg, str):
            fill(bg)
        else:
            fill(*bg)
        arcc(a, b, c-margin, d-margin, start, stop, mode, stroke_weight, strk)
        

def ccurve(a, b, c, d, start, stop, mode=OPEN, stroke_weight=5, strk=(0,0,0)):
    #noFill()
    strokeWeight(stroke_weight)
    if isinstance(strk, str):
        stroke(strk)
    else:
        stroke(*strk)
    arc(a, b, c, d, start, stop, mode)
    
# draws multiple arccs
# only supports circle arccs
# n = number of arccs
# s = spacing between arccs (independent of stroke weight)
def n_ccurve(a, b, n, s, start, stop, mode=OPEN, stroke_weight=5, strk=(0,0,0), bg=(255,255,255), margin=0):
    for n_ in range(n, 0, -1):
        c = d = n_ * s
        if isinstance(bg, str):
            fill(bg)
        else:
            fill(*bg)
        arcc(a, b, c-margin, d-margin, start, stop, mode, stroke_weight, strk)
        
   
    

    
def setup():
    size(720,720)
    smooth(8)

    bg = '#F6E6E4'
    strk = '#BB6464'
    
    # 1=full circle, 2=half, 4=quarter
    type = 4
    stop = HALF_PI
    
    n = 20
    stroke_weight = 1
    s = stroke_weight * 2 + 5
    step = n*s // type * 2 + stroke_weight/2 + 1

    fill(bg)
    rect(0,0,width,height)
    pis = [k * HALF_PI for k in range(4)]
    i = 0
    for _ in range(10):
        for r in range(step, width+step*2, step*2):
            for c in range(step, height+step*2, step*2):
                print(i)
                i+=1
                rotation = random.choice(pis)
                pushMatrix()
                translate(r,c)
                rotate(rotation)
                #rotate(HALF_PI)
                if i== 30:
                    n_arcc(-step, -step, n, s, 0, stop, stroke_weight=stroke_weight, mode=OPEN, bg=bg, strk=(0,255,0))    
                else:
                    n_arcc(-step, -step, n, s, 0, stop, stroke_weight=stroke_weight, mode=OPEN, bg=bg, strk=strk)
                popMatrix()
                
    
        
    for r in range(step, width+step*2, step*2):
        for c in range(step, height+step*2, step*2):
            rotation = random.choice(pis)
            pushMatrix()
            translate(r,c)            
            stroke(255, 0, 0)
            noFill()
            strokeWeight(2)
            #circle(-step, -step, step*2)
            popMatrix()
