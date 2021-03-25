void setup() {
  size(400, 400);
}

void draw() {
  background(130);
  
  pushMatrix();
  translate(width*0.5, height*0.5);
  rotate(frameCount / 100.0);
  star(0, 0, 30, 80, 5); 
  popMatrix();
}

void star(float x, float y, float raio1, float raio2, int pontas) {
  float angulo = TWO_PI / pontas;
  float metAng = angulo/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angulo) {
    float px = x + cos(a) * raio2;
    float py = y + sin(a) * raio2;
    vertex(px, py);
    px = x + cos(a+metAng) * raio1;
    py = y + sin(a+metAng) * raio1;
    vertex(px, py);
  }
  endShape(CLOSE);
}
