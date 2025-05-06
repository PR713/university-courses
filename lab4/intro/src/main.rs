use UIEvent::*;
use Direction::*;

#[derive(Debug)]
enum UIEvent {
    ButtonClicked,
    Scroll(Direction),
    KeyPressed(char),
    MouseClicked { x: i32, y: i32 }
}

#[derive(Debug)]
enum Direction {
    Up,
    Down,
}



impl UIEvent {
    fn describe(&self) {
        println!("UIEvent: {:?}", self);
    }
}

fn describe(event : UIEvent) {
    println!("UIEvent: {:?}", event);
}

#[derive(Debug)]
enum Message {
    Quit,
    Move{x: i32, y: i32},
    Echo(String),
    ChangeColor(i32, i32, i32)
}

impl Message {
    fn call(&self) {
        println!("{:?}", self);
    }
}


fn call(event : UIEvent) {
    //use UIEvent::*; //already is on the top
    match event {
        ButtonClicked => println!("Button clicked"), // simple match
        Scroll(x) => println!("Scroll {:?}", x), // attribute extraction
        KeyPressed(ch) => { // whole block
            let up_ch = ch.to_uppercase();
            println!("Key pressed: {}", up_ch);
        },
        MouseClicked { x, y } => println!("Mouse clicked at ({}, {})", x, y), // attribute extraction
    }
}


struct Point {
    x : i32,
    y : i32
}

fn main() {
    let clicked = ButtonClicked;
    let scroll = Scroll(Up);
    let b_key_pressed = KeyPressed('b');
    let mouse_clicked = MouseClicked{ x: 0, y: 123 };

    scroll.describe();
    describe(scroll);


    let messages = [
        Message::Move { x: 10, y: 30 },
        Message::Echo(String::from("hello world")),
        Message::ChangeColor(200, 255, 255),
        Message::Quit,
    ];

    for message in &messages {
        message.call();
    }


    ////


    let clicked = ButtonClicked;
    let scroll = Scroll(Down);
    let key_pressed = KeyPressed('b');
    call(clicked);
    call(scroll);
    call(key_pressed);



    let x = 2u16;

    match x {
        1 | 2 => println!("one or two"),
        3 | 4 => println!("three or four"),
        _ => println!("anything else"),
    }

    match x {
        1..=9 => println!("easy"),
        10..=99 => println!("medium"),
        100..=999 => println!("large"),
        _ => println!("anything else"),
    }


    let p = Point { x: 0, y: 7 };

    match p {
        Point { x, y: 0 } => println!("On the x axis at {x}"),
        Point { x: 0, y } => println!("On the y axis at {y}"),
        Point { x, y } => {
            println!("On neither axis: ({x}, {y})");
        }
    }

    match p {
        Point { x, .. } => println!("x is {}", x),
        _ => ()
    }


    let num = Some(4);

    match num {
        Some(x) if x % 2 == 0 => println!("The number {} is even", x),
        Some(x) => println!("The number {} is odd", x),
        None => (),
    }

    let x = 4;
    let y = false;

    match x {
        4 | 5 | 6 if y => println!("yes"),
        _ => println!("no"),
    }


    let x = Some(2);

    if let Some(x) = x {
        println!("{}", x); // 2
    } // można some(y) = x


    ////option

    let some_number = Some(5);
    let some_text = Some(String::from("Some value in Option type"));

    //let no_value : Option<i32> = None;


    let x = Some(5);
    let y = 10;

    //let sum = x + y; //Option<i32> + i32 Błąd
}

enum Option<T> { // T depicts generic type
    Some(T),
    None
}
