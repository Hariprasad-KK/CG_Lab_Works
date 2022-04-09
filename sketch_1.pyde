def setup():
    size(1000,1000)
def draw():
     line(0,500,1000,500);
     line(500,0,500,1000);
     triangle(50,50,150,100,110,150);
     translate(500,0);
     triangle(50,50,150,100,110,150);
     translate(0,500);
     triangle(50,50,150,100,110,150);
     translate(-500,0);
     triangle(50,50,150,100,110,150);
