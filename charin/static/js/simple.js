var x = new Array(1000);
var y = new Array(1000);
var c = new Array(1000);

function setup() {
    myCanvas = createCanvas(windowWidth, 400);
    myCanvas.parent("myContainer");
    for( var i = 0 ; i < x.length ; i++ ) {
        x[i] = random(width);
        y[i] = random(height);
        c[i] = color(255, random(255), random(255));
    }
    var title = createDiv("<h1>P5.js Test</h1>");
    title.position(50,10);
}

function draw() {
    background(255,50);
    for( var i = 0 ; i < x.length ; i++ ) {
        noStroke();
        fill(c[i]);
        ellipse(x[i], y[i], 20, 20);
        x[i] += random(-1,1);
        y[i] += random(1);
        if( height < y[i] ) {
            y[i] = -10;
        }
    }
}
