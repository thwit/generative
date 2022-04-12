float cx, cy, cr, padding, c;
import java.util.Map;
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

void setup() {
  size(500, 500);
  
  cx = width / 2;
  cy = height / 2;
  
  cr = 200;
  
  padding = 1;
  
  frameRate(1000);
  
  
  map.put(-90, 0);
  map.put(-89, 0);
  map.put(-88, 0);
  map.put(-87, 0);
  map.put(-86, 0);
  map.put(-85, 0);
  map.put(-84, 0);
  map.put(-83, 0);
  map.put(-82, 0);
  map.put(-81, 0);
  map.put(-80, 0);
  map.put(-79, 0);
  map.put(-78, 2);
  map.put(-77, 8);
  map.put(-76, 8);
  map.put(-75, 9);
  map.put(-74, 19);
  map.put(-73, 15);
  map.put(-72, 21);
  map.put(-71, 11);
  map.put(-70, 13);
  map.put(-69, 25);
  map.put(-68, 23);
  map.put(-67, 28);
  map.put(-66, 56);
  map.put(-65, 66);
  map.put(-64, 34);
  map.put(-63, 14);
  map.put(-62, 13);
  map.put(-61, 15);
  map.put(-60, 23);
  map.put(-59, 16);
  map.put(-58, 12);
  map.put(-57, 10);
  map.put(-56, 11);
  map.put(-55, 14);
  map.put(-54, 24);
  map.put(-53, 13);
  map.put(-52, 19);
  map.put(-51, 15);
  map.put(-50, 9);
  map.put(-49, 9);
  map.put(-48, 3);
  map.put(-47, 3);
  map.put(-46, 3);
  map.put(-45, 0);
  map.put(-44, 1);
  map.put(-43, 0);
  map.put(-42, 0);
  map.put(-41, 0);
  map.put(-40, 0);
  map.put(-39, 0);
  map.put(-38, 0);
  map.put(-37, 0);
  map.put(-36, 0);
  map.put(-35, 0);
  map.put(-34, 0);
  map.put(-33, 0);
  map.put(-32, 0);
  map.put(-31, 0);
  map.put(-30, 0);
  map.put(-29, 0);
  map.put(-28, 0);
  map.put(-27, 0);
  map.put(-26, 0);
  map.put(-25, 0);
  map.put(-24, 0);
  map.put(-23, 0);
  map.put(-22, 0);
  map.put(-21, 0);
  map.put(-20, 0);
  map.put(-19, 0);
  map.put(-18, 0);
  map.put(-17, 0);
  map.put(-16, 0);
  map.put(-15, 0);
  map.put(-14, 0);
  map.put(-13, 0);
  map.put(-12, 0);
  map.put(-11, 0);
  map.put(-10, 0);
  map.put(-9, 0);
  map.put(-8, 0);
  map.put(-7, 0);
  map.put(-6, 0);
  map.put(-5, 0);
  map.put(-4, 0);
  map.put(-3, 0);
  map.put(-2, 0);
  map.put(-1, 0);
  map.put(0, 0);
}

void draw() {
  int sum = 0;
  for (int f : map.values()) {
    sum += f;
  }
  float start1 = 0;
  float start2 = 0;
  float stop1 = sum;
  float stop2 = 255;
  
  for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
    float f = entry.getValue();
    
    float fintensity = map(f, start1, stop1, start2, stop2);
    int intensity = int(fintensity)* 25;
    color ringColor = color(intensity, 1, 1);
    int weight = 2;
    stroke(ringColor);
    strokeWeight(weight);
    noFill(); //This line is the one you need!
    
    ellipse(width / 2, height / 2, (90 - entry.getKey()) * weight, (90 - entry.getKey()) * weight);
  }
  noLoop();
}
