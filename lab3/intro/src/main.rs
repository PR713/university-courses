use std::fmt::{Display, Formatter};

struct EmptyStructure;
struct Color(i32, i32, i32); // fields are without names (are access as in tuple)
struct PointTuple(i32, i32, i32); // a different structure with the same types
struct Point{
    x: f32,
    y: f32
}

#[derive(Debug)] // allows to print the structure in debug mode (ie. to use {:?})
struct Rectangle {
    x : f32,
    y : f32
}

impl Rectangle {
    fn area(&self) -> f32 { //musimy przekazać pożyczkę do self
        self.x * self.y// + 100f32
    }

    fn scale(&mut self, factor: f32) { //&mut self modyfikacja instancji
        self.x *= factor;
        self.y *= factor;
    }

    fn into_tuple(self) -> (f32, f32) { //consumer
        (self.x, self.y)
    }

    fn new_square(x: f32) -> Self {
        Self { x, y : x }
    }
}


trait Shape {
    fn area(&self) -> f32;
    fn perimeter(&self) -> f32;

    fn describe(&self) {
        println!("I'm a general shape.");
    }
}

impl Shape for Rectangle {
    fn area(&self) -> f32 {
        self.x * self.y
    }

    fn perimeter(&self) -> f32 {
        2f32 * (self.x + self.y)
    }

    fn describe(&self) {
        println!("I'm a rectangle.");
    }
}


impl Display for Rectangle {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "Rectangle[x={},y={}]", self.x, self.y)?;
        Ok(())
    }
}

fn main() {
    // let es = EmptyStructure;
    // let black = Color(0, 0, 0);
    // let origin = PointTuple(0, 0, 0);
    // let point = Point{x: 1.0, y: 2.0};
    let r = Rectangle{x: 1.0, y: 1.0};

    println!("{:?}", r);
    println!("x: {}, y: {}", r.x, r.y);

    let r1 = Rectangle{x: 10.0, ..r};
    println!("{:?}", r1); //as spread operator JS


    let mut r3 = Rectangle{x : 5.0, y : 9.0};
    println!("[{}, {}]", r3.x, r3.y);
    r3.x = 10.0; //without mut there will occur an error

    println!("Area of {:?} is {}", r, r.area());
    r3.scale(0.5);

    let (x, y) = r3.into_tuple();
    //println!("{:?}", r3); //r3 moved ^^ into_tuple(self) neither &self nor &mut self

    let square = Rectangle::new_square(3.0);
    println!("{:?}", square);

    println!("\n*** traits ***\n"); //jak interfejs
    let area = r1.area(); //by default uses method implemented in Rectangle
    // not in impl Shape for Rectangle
    println!("area {}", area);
    println!("{}", r1.perimeter());

    r1.describe(); //I am a Rectangle

    println!("{}", r1);
}