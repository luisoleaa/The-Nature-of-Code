// Recreates the Koch Curve when a button is pressed
// Built using "The Nature of Code" free textbook Chapter 8


let segments = [];

class KochLine {
  //{!2} A line between two points: a and b
  constructor(a, b) {
    // a and b are p5.Vector objects.
    this.start = a.copy();
    this.end = b.copy();
  }
  kochPoints(){
    let a = this.start.copy();

    let v = p5.Vector.sub(this.end, this.start);
    v.div(3);

    let b = p5.Vector.add(a,v);
    let d = p5.Vector.add(b,v);

    // finding c using equilateral triangles (pi/3)
    v.rotate(-PI/3);
    let c = p5.Vector.add(b,v);
    
    let e = this.end.copy();
    return [a,b,c,d,e];
  }
  kochPointsOpposite(){
    let a = this.end.copy();
    
    let v = p5.Vector.sub(this.end, this.start);
    v.div(3);

    let b = p5.Vector.add(e,v);
    let d = p5.Vector.add(b,v);

    v.rotate(PI/3);
    let c = p5.Vector.add(b,v);


    let e = this.start.copy();
    return [a,b,c,d,e];
  }

  show() {
    stroke(0);
    //{!1} Draw the line from a to b.
    line(this.start.x, this.start.y, this.end.x, this.end.y);
    
  }
}

function generate(){
  let next = [];
  for(let segment of segments){
    let [a,b,c,d,e] = segment.kochPoints();
    next.push(new KochLine(a,b));
    next.push(new KochLine(b,c));
    next.push(new KochLine(c,d));
    next.push(new KochLine(d,e));
  }
  segments = next;
}

function opposite(){
  let next = [];
  for(let segment of segments){
    let[a,b,c,d,e] = segment.kochPointsOpposite();
    next.push(new KochLine(a,b));
    next.push(new KochLine(b,c));
    next.push(new KochLine(c,d));
    next.push(new KochLine(d,e));
  }
  segments = next;
}




function setup() {
  createCanvas(1340,1040);

  let start = createVector(0,500);
  let end = createVector(width,500);

  segments.push(new KochLine(start,end))
  segments.push(new KochLine(end,start))
}

function draw() {
  background(255);
  for (let segment of segments){
    segment.show();
  }
}

function keyPressed() {
  generate();
  opposite();
}



