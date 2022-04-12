float cx, cy, cr, padding, c;
ArrayList<Rectangle> rects = new ArrayList<Rectangle>();


void setup() {
  size(500, 500);
  
  cx = width / 2;
  cy = height / 2;
  
  cr = 200;
  
  padding = 1;
  
  frameRate(1000);
}

void draw() {
  c+=1;
  float x = random(width);
  float y = random(height);
  float w = random(max(padding * 2, 3), 40);
  float h = random(max(padding * 2, 3), 40);
  
  Rectangle rect = new Rectangle(x, y, w, h, padding);
  
  
  if (dist(x + w / 2, y + w / 2, cx, cy) < cr) {
    boolean valid = true;
    for (Rectangle other : rects) {
      if (rect.collision(other)) {
        valid = false;
        break; 
      }
    }
    if (valid) {
      rects.add(rect);
      rect.display();
    }
  }
}



final class Rectangle {
  final short x, y, w, h, p;
  boolean state;

  final static color c = 50;

  Rectangle(float xx, float yy, float ww, float hh, float padding) {
    x = (short) xx;
    y = (short) yy;
    w = (short) ww;
    h = (short) hh;
    p = (short) padding;
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
    rect(x + p, y + p, w - p, h - p);
  }
  
  void display(color cc) {
    stroke(cc);
    rect(x + p, y + p, w - p, h - p);
  }
}
