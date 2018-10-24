int colrd;

void setup()
{
size(480,480);
frameRate(3);
smooth();
background(255,199,127);
}

void draw()
{
float diameter = random(100);
noStroke();
colorRandom();
ellipse(random(width),random(height),diameter,diameter);
}
void colorRandom() 
{
    color[] c = new color[4];
    c[0] = color(240,104,145);
  c[1] = color(255,164,102);
   c[2] = color(255,228,102);
  c[3] = color(255,255,255);
  
   colrd = int(random(0, 3));    
    switch(colrd) {
  case 0: 
   fill(c[0]);
    break;
  case 1: 
      fill(c[1]);
    break;
     case 2: 
      fill(c[2]);
    break;
        case 3: 
      fill(c[3]);
    break;
}
}