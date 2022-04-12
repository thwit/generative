PImage img;
int c = 0;

void setup() {
  img = loadImage("DSC_7980.jpg");
  img.resize(750,0);
  size(750, 750);
  frameRate(1000);
  tint(255, 255);
  //image(img, 0, 0);
  

}

color extractColorFromImage(final PImage img, int alpha) {
  img.loadPixels();
  color r = 0, g = 0, b = 0;
 
  for (final color c : img.pixels) {
    r += c >> 020 & 0xFF;
    g += c >> 010 & 0xFF;
    b += c        & 0xFF;
  }
 
  r /= img.pixels.length;
  g /= img.pixels.length;
  b /= img.pixels.length;
 
  return color(r, g, b, alpha);
}


void draw() {
  int w = int(random(2, 20));
  int h = int(random(2, 20));
  int x = int(random(img.width - w));
  int y = int(random(img.height - h));
  int alpha = 255;
  int colorOffset = 255;
  int rr = int(random(-colorOffset, colorOffset)), rg = int(random(-colorOffset, colorOffset)), rb = int(random(-colorOffset, colorOffset)); 
  
  Rectangle rect = new Rectangle(x, y, w, h);
  PImage ROI = img.get(rect.x, rect.y, rect.w, rect.h);
  rect.display(extractColorFromImage(ROI, alpha));
  
  float angle = random(-PI, PI);
  angle = 0;
  //rect.display(color(red(get(x + rect.w / 2, y + rect.h / 2)) + rr, green(get(x + rect.w / 2, y + rect.h / 2)) + rg, blue(get(x + rect.w / 2, y + rect.h / 2)) + rb, alpha), angle);
  
}


final class Rectangle {
  final short x, y, w, h;
  boolean state;

  final static color c = 50;

  Rectangle(float xx, float yy, float ww, float hh) {
    x = (short) xx;
    y = (short) yy;
    w = (short) ww;
    h = (short) hh;
  }

  boolean toggle() {
    return state = !state;
  }

  boolean click() {
    return mouseX > x & mouseX < x+w & mouseY > y & mouseY < y+h;
  }

  boolean collision(Rectangle other) {
    return (this.x + this.w >= other.x &&
            this.x <= other.x + other.w &&
            this.y + this.h >= other.y &&
            this.y <= other.y + other.h);
  }

  void display() {
    stroke(c);
    fill(c);
    rect(x, y, w, h);
  }
  
  void display(color cc) {
    noStroke();
    fill(cc);
    rect(x, y, w, h);
  }
  
  void display(color cc, float angle) {
    noStroke();
    fill(cc);
    
    pushMatrix();
    //translate(x, y);
    //rotate(random(angle));
    rect(x, y, w, h);
    popMatrix();
  }
}
