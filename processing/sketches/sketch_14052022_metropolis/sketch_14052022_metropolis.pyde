from __future__ import division

import pens
import tools
import fills


def setup():
    global pg, colors, strk_col, fill_col, bg_col, pwidth, pheight, flag, margin, pen, stroke_weight, scale_, seed
    size(500, 700)

    # SEEDS
    seed = int(random(1000000))
    randomSeed(seed)
    noiseSeed(seed)

    # COLOR DEFINITIONS
    colors = ['#8fa57f', '#FA8246', '#FEB139', '#F6F54D']
    bg_col = '#fffffa'
    strk_col = '#000000'

    bg_col = tools.hex_to_hsb(bg_col)
    strk_col = tools.hex_to_hsb(strk_col)
    colors = tools.hex_to_hsb(colors)

    # LAYOUT PARAMETERS
    # Scale applied to width and height to get PGraphics drawing size
    scale_ = 1
    print('heyy ' + ())

    # PGraphics drawing size
    pwidth, pheight = width * scale_, height * scale_

    # Margins around the drawing
    margin = 30 * scale_

    # STYLE PARAMETERS
    stroke_weight = 1

    # Create and setup PGraphics
    pg = createGraphics(pwidth + margin * 2, pheight + margin * 2)
    pen = pens.PenBasic(pg, fills.CurveFill(pg))
    pen = pens.PenBasic(pg, fills.BasicFill(pg))

    pg.beginDraw()
    pg.colorMode(HSB, 360, 100, 100)
    # pg.colorMode(RGB, 255, 255, 255)
    pen.strokeWeight(stroke_weight)

    pg.endDraw()
    # pen.set_clean(True)
    # pen.prob = 0

    flag = True


def keyReleased():
    global flag

    if key == ENTER:
        flag = True


def draw2():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, scale_, seed

    s = pwidth // 2

    pen.noStroke()
    pen.fill(colors[0])
    pen.rect(PVector(0, 0), pwidth, pheight)

    pen.fill(colors[1])

    r = None

    while r is None or pwidth % (r * 2) != 0 or pheight % (r * 2) != 0:
        r = int(random(10, 100))

    r = 10 * scale_
    s = 2 * (r - 3)
    n = pwidth / (r * 2)

    y_starts = []

    # Sky
    pen.fill(colors[1])
    pen.fill((0, 0, 85))
    for x in range(r, pwidth, r * 2):
        color_changed = False
        for y in range(r, pheight, r * 2):
            if random(1) < y / (pheight * 4):
                y_starts.append(y)
                color_changed = True
                break

            pen.fill((210, 15, map(y, 0, pheight, 80, 100)))
            pen.fill((0, 0, 85))

            pen.circle(PVector(x, y), r - 3)

        if not color_changed:
            y_starts.append(pheight)

    # Sun
    sun_radius = 85
    pg.fill(*bg_col)
    pg.circle(pwidth - 110, 150, sun_radius * 2 + 3)
    pen.fill(colors[0])
    pen.circle(PVector(pwidth - 110, 150), sun_radius + 2)
    pen.fill(colors[1])
    pen.circle(PVector(pwidth - 110, 150), sun_radius)

    print(2 * n / 3 * (r - 5))

    # Buildings
    # pen.fill(colors[1])
    pen.fill((0, 0, 0))
    for y_start, x in zip(y_starts, range(r, pwidth, r * 2)):
        for y in range(y_start, pheight, r * 2):
            if random(1) < 0.03:
                col = colors[3]
                pen.fill((col[0], col[1] - 15, col[2] - 5))
            else:
                pen.fill((0, 0, 0))
            pen.circle(PVector(x, y), r - 3)

    points = []

    tools.to_panto_a4(points, pwidth, pheight)


def draw():
    global flag, bg_col, strk_col, fill_col, pwidth, margin, pheight, colors, pen, stroke_weight, seed
    if flag:
        flag = False
        pg.beginDraw()

        # Set background color
        pg.fill(*bg_col)
        pg.noStroke()
        pg.rect(-1, -1, pwidth + margin * 2 + 1, pheight + margin * 2 + 1)
        pg.noFill()
        print('ye')

        pen.fill(colors[1])
        pen.noStroke()
        # pen.rect(PVector(-1, -1), pwidth + margin * 2 + 1, pheight + margin * 2 + 1)

        pen.stroke(strk_col)

        # Push matrix and translate coordinate system so (0,0) is at (margin, margin)
        pg.pushMatrix()
        pg.translate(margin, margin)

        draw2()

        pg.loadPixels()
        # tools.noisify_brightness(pg.pixels, pg)
        pg.updatePixels()

        # End drawing on PGraphics
        pg.popMatrix()
        pg.endDraw()

        # Display final drawing and save to .png in same folder
        image(pg, 0, 0, width, height)
        tools.save_image(pg, seed)
