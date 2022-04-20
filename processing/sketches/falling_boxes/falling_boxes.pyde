from __future__ import division

def setup():
    size(800, 800)
    
    #### COLOR DEFINITIONS
    bg_col = 0xFFFFFFFF
    strk_col = 0xFF000000
    
    #### LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 1
    
    # PGraphics drawing size
    pwidth, pheight = width*scale_, height*scale_
    
    # Margins around the drawing
    margin = 50 * scale_
    
    # Margins between each grid cell
    grid_margin = 5 * scale_
    
    # Outer size of grid cell
    tw = 100 * scale_
    th = 5 * scale_
    
    # Inner size of grid cell
    dw = tw - grid_margin
    dh = th - grid_margin
    
    # Number of rows and columns in grid
    rows = int(pheight // th)
    cols = int(pwidth // tw)
    
    # STYLE PARAMETERS
    stroke_cap = ROUND
    stroke_weight = 1
    n_loop = 1
    
    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pg.beginDraw()
    pg.smooth(8)
    pg.strokeCap(stroke_cap)
    
    # Set background color
    pg.fill(bg_col)
    pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
    #pg.rectMode(CENTER)
    
    # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
    pg.pushMatrix()
    pg.translate(margin, margin)
    
    for _ in range(n_loop):
        for r in range(1, rows):
            for c in range(1, cols-1):
                # Coordinates, heights, and widths for the drawn grid:
                # (x                 , y                 , w , h )
                # (c * tw + (tw-dw)/2, r * th + (th-dh)/2, dw, dh)
                pg.strokeWeight(stroke_weight)
                if c > 1 and False:
                    pg.line(c*tw + grid_margin/2, 0, c*tw + grid_margin/2, height)
                    pg.line(c*tw - grid_margin/2, 0, c*tw - grid_margin/2, height)
                pg.pushMatrix()
               
                pg.translate(c*tw + grid_margin/2 + dw/2, r * th + grid_margin/2 + dh/2)
                pg.rotate(random(-map(r, 0, rows, 0, QUARTER_PI), map(r, 0, rows, 0, QUARTER_PI)))
                pg.rect(-dw/2, -dh/2, dw, dh)
                pg.popMatrix()
                
    # End drawing on PGraphics    
    pg.popMatrix()
    pg.endDraw()
    
    print('done')
    # Display final drawing and save to .png in same folder
    image(pg, 0, 0, width, height)
    pg.save("falling_boxes.png")
