void setup() {
  size(500, 500);
}

void draw() {
  float s = 15;
  
  fill(255);
  stroke(255);
  rect(0, 0, 500, 500);
  for (int x = 0; x < width; x += s) {
    for (int y = 0; y < height; y += s) {
      
      stroke(200);
      //rect(x, y, s, s);
      
      float val = randomGaussian();
      float sd = 0.2;                  // Define a standard deviation
      float mean = map(x, 0, width, x, x-s);           // Define a mean value (middle of the screen along the x-axis)
      
      float x1 = ( val * sd ) + mean;
      float y1 = y;
      
      val = randomGaussian();
      sd = 0.2;                  // Define a standard deviation
      mean = map(y, 0, height, x, x+s);           // Define a mean value (middle of the screen along the x-axis)
      float x2 = ( val * sd ) + mean;  // Scale the gaussian random number by standard deviation and mean
      
      float y2 = y + s;
      
      stroke(150);
      line(x1, y1, x2, y2);
    }
  }
  noLoop();
}
