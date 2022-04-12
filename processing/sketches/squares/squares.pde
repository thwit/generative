void setup() {
  size(505, 505);
  frameRate(5);
}

void draw() {
  float s = 25;
  int padding = 5;
  int margin = 25;
  
  fill(255);
  stroke(255);
  rect(0, 0, width, height);
  for (int i = 0; i < 1; i++) {
    for (int x = margin; x < (width - margin); x += s) {
      for (int y = margin; y < (height - margin); y += s) {
        
        noStroke();
        fill(random(map(height-y, 0, height, 0, 255)), random(map(height-y, 0, height, 0, 255)), random(map(height-y, 0, height, 0, 255)), 100);
        
        
        pushMatrix();
        translate(x, y);
        rotate(random(map(height-y, 0, height, 0 , PI / 2)));
        rect(-(s - padding) / 2, -(s - padding) / 2, s - padding, s - padding);
        popMatrix();
        
      }
    }
  }
      
}
