class Circle {
  float x, y, dx, dy, randno;
  
  Circle() {
    // Initialize a new moving circle's location and avoid the central area
    do {
    x = random(width);
    y = random(height);
    } while ((x < 230 && x > 70) && (y < 230 && y > 70));
    
    // Decide the moving speed and direct it toward the center
    randno = random(20, 35);
    dx = (x - 150) / randno;
    dy = (y - 150) / randno;
  }
  
  void drawCircle() {
    // Draw the moving circle
    fill(255, 50, 50);
    ellipse(x, y, 20, 20);
  }
  
  void moveCircle() {
    // Move the circle
     x -= dx;
     y -= dy;   
  }
}