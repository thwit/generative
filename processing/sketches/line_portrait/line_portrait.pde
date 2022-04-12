PImage img;

void setup() {
  img = loadImage("test.png");
  //img.filter(BLUR, 20);
  //img.filter(GRAY);
  //img.filter(THRESHOLD, 0.9999);
  
  img.loadPixels();
  size(300, 300);
}

float gray(int c) {
  float r = red(c); // red part
  float g = green(c); // green part
  float b = blue(c); // blue part
  return (r+b+g)/3; 
}

void draw() {
  int w = img.width;
  int h = img.height;
  int stepSize = 5;
  
  background(255);
  stroke(255,0,0);
  
  image(img,0,0);
  println("start");
  
  int count = 0;
  
  for (int y = 0, yy = 0; y < h; y += stepSize, yy += stepSize) {
    
    int x1 = -1;
    int y1 = -1;
    for (int x = 0; x < w; x++) {
      if (200 < green(img.pixels[x + y  * w]) && 200 < red(img.pixels[x + y  * w]) && 200 < blue(img.pixels[x + y  * w])) {
        count++;
      }
      
      if (gray(img.pixels[x + y * img.width]) < 1 && x1 == -1) {
        
        //stroke(255,0,0);
        //line(0, y, x, y);
        x1 = x;
        y1 = y;
        yy += random(-10, 10);
        if (yy < 0) {
          yy = 0;
        } else if (yy >= height) {
          yy = height - 1;
        }
        
      } else if (gray(img.pixels[x + yy * img.width]) > 250 && x1 != -1) {
        //stroke(0, 255, 0);
        fill(50,50,50);
        rect(x1, y1, 5, 5);
        line(x1, y1, x, yy);
        //line(x, yy, width, yy);
        
        break;
      } else if ((x + stepSize) >= w) {
        //stroke(0, 0, 255);
        //line(0, y, width, y);
        break;
      }
    }
  }
  println(count);
  noLoop();
}
