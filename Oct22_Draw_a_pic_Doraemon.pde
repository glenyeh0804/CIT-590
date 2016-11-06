void setup() {
 // This is the main program
 size(280, 280);
 background(220, 200, 170);
 head();
 face();
 eyes(0, 0);
 eyes(45, 20);
 nose();
 hair(0);
 hair(55);
 mouth();
 tongue();
 bell();
 name();
}

void head() {
  // This is for head
  fill(20, 170, 220);
  stroke(0);
  strokeWeight(1.5);
  ellipse(150, 150, 230, 210);
}

void eyes(float shift, float shift2) {
  // This is for eyes
  fill(255, 255, 255);
  stroke(0);
  strokeWeight(1.5);
  ellipse(130 + shift, 75, 45, 50);
  fill(0);
  ellipse(142 + shift2, 78, 10, 17);
  stroke(255, 255, 255);
  fill(255, 255, 255);
  ellipse(142 + shift2, 76, 2, 5);
}

void nose() {
  // This is for nose
  fill(220, 0, 0);
  stroke(0);
  strokeWeight(1.5);
  ellipse(152, 103, 28, 28);
  stroke(255, 255, 255);
  fill(255, 255, 255);
  ellipse(150, 98, 10, 10);
}

void face() {
  // This is for face
  fill(255, 255, 255);
  stroke(0);
  strokeWeight(1.5);
  beginShape();
    curveVertex(109, 85);
    curveVertex(109, 85);
    curveVertex(75, 100);
    curveVertex(50, 140);
    curveVertex(60, 200);
    curveVertex(90, 240);
    curveVertex(150, 250);
    curveVertex(210, 240);
    curveVertex(240, 200);
    curveVertex(250, 140);   
    curveVertex(225, 100);
    curveVertex(191, 85);
    curveVertex(191, 85);
  endShape();
}

void hair(float shift) {
  // This is for hair
  stroke(0);
  strokeWeight(1.5);
  line(152, 118, 152, 220);
  line(125 + shift, 120, 70 + (2.9 * shift), 110);
  line(123 + shift, 135, 65 + (3.1 * shift), 135);
  line(125 + shift, 150, 70 + (3 * shift), 160);
}

void mouth() {
  // This is for mouth
  stroke(0);
  strokeWeight(1.5);
  noFill();
  beginShape();
    curveVertex(70, 180);
    curveVertex(70, 180);
    curveVertex(152, 220);
    curveVertex(230, 180);
    curveVertex(230, 180);
  endShape();
  
}

void tongue() {
 // This is for tongue
 stroke(0);
 strokeWeight(1.5);
 fill(220, 0, 0);
 arc(95, 195, 40, 80, 3.4, 6.6, PIE);
 fill(0);
 line(95, 195, 95, 180);
}

void bell() {
 // This is for bell
 stroke(0);
 strokeWeight(1.5);
 fill(220, 0, 0);
 beginShape();
   curveVertex(70, 230);
   curveVertex(70, 230);
   curveVertex(70, 240);
   curveVertex(80, 245);
   curveVertex(110, 250);
   curveVertex(150, 255);
   curveVertex(180, 253);   
   curveVertex(223, 245);
   curveVertex(223, 230);
   curveVertex(150, 240);
   curveVertex(70, 230);
   curveVertex(70, 230);
 endShape();
 fill(255, 230, 120);
 ellipse(150, 260, 35, 35);
 beginShape();
   curveVertex(132, 252);
   curveVertex(132, 252);
   curveVertex(150, 251);
   curveVertex(165, 252);
   curveVertex(165, 252);
 endShape();
  beginShape();
   curveVertex(132, 255);
   curveVertex(132, 255);
   curveVertex(150, 254);
   curveVertex(165, 255);
   curveVertex(165, 255);
 endShape();
 fill(150, 150, 150);
 ellipse(150, 263, 7, 7);
 fill(0);
 line(150, 266, 150, 277);
}

void name() {
 // This is for name
 PFont myFont;
 stroke(0);
 strokeWeight(1.5);
 myFont = createFont("Arial", 12);
 textFont(myFont);
 fill(0);
 text("Ting-Chun Yeh", 190, 275);
}
