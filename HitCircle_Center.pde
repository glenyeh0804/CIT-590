import java.awt.Point;
import java.util.ArrayList;
boolean pass, inzone = false;
ArrayList<Circle> list = new ArrayList();
boolean gameover = false;
int time, level, score, misses = 0;

void setup() {
  // Initialize the game board
  size(300, 300);
  frameRate(60);
}

void draw() {
  // Show the gameover and result page
  if (gameover){
    drawEnding();
    return;
  }
  
  background(255);
  
  // Set the level of difficulty (frequency of moving circles)
  time += 1;
  if (time < 1500) {
    level = 100;
  }
  else if (time < 2500) {
    level = 70;
  }
  else
  {
    level = 50;
  }
  
  // Produce new circles
  if (time % level == 0) {
    list.add(new Circle());
  }
  
  // Draw the center fixed circle
  fill(255);
  stroke(0);
  strokeWeight(5);
  ellipse(150, 150, 40, 40);
  
  // Control and draw the moving circles
  moveCircles();
  drawCircles();
  
  // Check whether the user hits circle or miss it
  inCircle();
  score();
  
  // If misses > 3, gameover
  if (misses == 3){
  gameover = true;
  }
}

void moveCircles(){
  // Call the circle in the list and "move" it
  for (Circle circle : list){
    circle.moveCircle();
  }
}

void drawCircles(){
  // Call the circle in the list and draw it
  for (Circle circle : list) {
    circle.drawCircle();
  }
}

void inCircle(){
  for (Circle circle : list){
    if (dist(150, 150, circle.x, circle.y) < 30) {
      // Check whether the user hits the circle. If hits, show green sign.
      inzone = true;
      if ((keyPressed && key == ENTER) && !pass){
        score += 1;
        pass = true;
        fill(0, 255, 0);
        stroke(0);
        strokeWeight(5);
        ellipse(150, 150, 40, 40);  
      }
      else if (pass) {
        fill(0, 255, 0);
        stroke(0);
        strokeWeight(5);
        ellipse(150, 150, 40, 40);  
      }
    }
    else if (dist(150, 150, circle.x, circle.y) < 50) {
      // Check whether the user misses the circle. If misses, show red sign.
      if (inzone){
        if (!pass){
          misses += 1;
          fill(255, 0, 0);
          stroke(0);
          strokeWeight(5);
          ellipse(150, 150, 40, 40);
        }
        inzone = false;
        pass = false;
      }
    }
  }
}

void score(){
  // Show the current scores / misses
  PFont myFont;
  stroke(0);
  strokeWeight(1.5);
  myFont = createFont("Arial", 18);
  textFont(myFont);
  fill(0);
  text("Scores: " + score, 190, 260);  
  text("Misses: " + misses, 190, 285);
}

void drawEnding() {
  // Show the result page
  background(200, 20, 20);
  PFont myFont;
  stroke(0);
  strokeWeight(1.5);
  myFont = createFont("Arial", 25);
  textFont(myFont);
  fill(0);
  text("Game Over :'(", 75, 120);
  text("Your final score is: " + score, 40, 180);  
}