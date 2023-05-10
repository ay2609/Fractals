// noprotect

var a = -0.192;
var b = 0.982;
var z = 3;

function f(x) {
  return a*x + 2*(1 - a)*x*x*pow(1 + x*x, -2);
}

function gumowskimira(x0, y0, iters) {
  var x = x0;
  var y = y0;
  
  for (i = 0; i < iters; i++) {
    var xt = x;
    
    x = b*y + f(x);
    y = f(x) - xt;
    
    point(map(x, -z, z, 0, width), map(y, -z, z, height, 0));
  }
}

function setup() {
  createCanvas(800, 800);
  background(255);
  
  noLoop();
}

function draw() {
  stroke(0, 20);
  
  for (j = 0; j < 10000; j++) {
  	gumowskimira(random(-z, z), random(-z, z), 1000);
  }
}

