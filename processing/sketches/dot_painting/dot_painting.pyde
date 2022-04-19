from __future__ import division
import random as rrandom

def dist_noise(x,y, strength=0.9, size_=5):
    return noise(x,y,strength*size_*noise(x,y))

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# Fire like drawing
def setup1():
    size(600, 750)
    
    #### COLOR DEFINITIONS
    colors = ['#824b22','#7f1613','#da2d1d','#f68b17','#fee936']
    bg_col = '#faba27'
    filler_col = '#e8a60e'
    colors = [hex_to_rgb(c) for c in colors]
    #rrandom.shuffle(colors)
    bg_col = hex_to_rgb(bg_col)
    filler_col = hex_to_rgb(filler_col)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 5
    
    # Margins around the drawing
    margin = 50 * scale_
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Distance between dots
    d = 2
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    radius = 1
    n_loop = 1
    sc_x = 0.01
    sc_y = 0.0005
    jitter_pos = 1
    jitter_radius = 0
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pg.beginDraw()
    pg.noSmooth()
    pg.strokeCap(stroke_cap)
    
    # Set background color
    pg.fill(*bg_col)
    pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
    
    # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
    pg.pushMatrix()
    pg.translate(margin, margin)
    
    offset_x = 0
    offset_y = 0
    for seed in range(len(colors)):
        noiseSeed(1)
        for x in range(0, pwidth, d):
            for y in range(0, pheight, d):
                n = noise((x+offset_x) * sc_x, (y+offset_y) * sc_y) + random(-0.15, 0.15)
                clr = None
                if n < 0.2:
                    clr = colors[0]
                elif 0.2 <= n < 0.4:
                    clr = colors[1]
                elif 0.4 <= n < 0.6:
                    clr = colors[2]
                elif 0.6 <= n < 0.8:
                    clr = colors[3]
                elif 0.8 <= n:
                    clr = colors[4]
                
                pg.stroke(*clr)
                pg.fill(*clr)
                pg.circle(x + random(-jitter_pos, jitter_pos), y + random(-jitter_pos, jitter_pos), radius + random(-jitter_radius, jitter_radius))
                    
            
        offset_x += 100 * scale_
        offset_y += 100 * scale_
        
    # End drawing on PGraphics    
    pg.popMatrix()
    pg.endDraw()
    
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    pg.save("dot_painting.png")
    
    
# Idea for this setup:
# Separate noise into 'blobs'
# in each blob, use different color and/or different density of dots
def setup():
    size(600, 750)
    init_seed = int(random(100000))
    noiseSeed(init_seed)
    print('Initial seed: ' + str(init_seed))


    
    #### COLOR DEFINITIONS
    colors = ['5d2904','#82440b','#b7751f','#8b6e28','#d4ba66']
    bg_col = '#ab7f39'
    filler_col = '#e8a60e'
    colors = [hex_to_rgb(c) for c in colors]
    #rrandom.shuffle(colors)
    bg_col = hex_to_rgb(bg_col)
    #filler_col = hex_to_rgb(filler_col)
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 1
    
    # Margins around the drawing
    margin = 50 * scale_
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Distance between dots
    d = 1
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    radius = 2
    n_loop = 1
    sc_x = 0.01
    sc_y = 0.003
    jitter_pos = 2
    jitter_radius = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pg.beginDraw()
    pg.noSmooth()
    pg.strokeCap(stroke_cap)
    
    # Set background color
    pg.fill(*bg_col)
    pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
    
    # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
    pg.pushMatrix()
    pg.translate(margin, margin)
    
    offset_x = 0
    offset_y = 0
    for seed in range(min(1, len(colors))):
        for x in range(0, pwidth, d):
            for y in range(0, pheight, d):
                n = dist_noise((x+offset_x) * sc_x, (y+offset_y) * sc_y) + random(-0.15, 0.15)
                clr = None
                draw_ = False
                if n < 0.2:
                    clr = colors[0]
                    draw_ = random(1) < 0.15
                elif 0.2 <= n < 0.4:
                    clr = colors[1]
                    draw_ = random(1) < 0.15
                elif 0.4 <= n < 0.6:
                    clr = colors[2]
                    draw_ = random(1) < 0.25
                elif 0.6 <= n < 0.8:
                    clr = colors[3]
                    draw_ = random(1) < 0.31
                elif 0.8 <= n:
                    clr = colors[4]
                    draw_ = random(1) < 0.55
                
                if draw_ or True:
                    pg.stroke(*clr)
                    pg.fill(*clr)
                    pg.circle(x + random(-jitter_pos, jitter_pos), y + random(-jitter_pos, jitter_pos), radius + random(-jitter_radius, jitter_radius))
                    
            
        offset_x += 100 * scale_
        offset_y += 100 * scale_
        
    # End drawing on PGraphics    
    pg.popMatrix()
    pg.endDraw()
    
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    pg.save('dot_painting_2' + str(init_seed) + '.png')
