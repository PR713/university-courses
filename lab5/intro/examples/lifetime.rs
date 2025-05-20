
fn len_longer_array(a : &[i32], b : &[i32]) -> usize {
    if a.len() > b.len() {
        a.len()
    } else {
        b.len()
    }
}

fn longer_array<'a>(a : &'a[i32], b : &'a[i32]) -> &'a[i32] {
    if a.len() > b.len() {
        a
    } else {
        b
    }
}



#[derive(Debug)]
struct Introduction<'a> {
    intro : &'a str
}

impl<'a> Introduction<'a> {
    fn print(&self) {
        println!("{}", self.intro);
    }

    fn get_intro(&self) -> &str { //lifetime elision rules
        self.intro
    }
}


//

fn get_sample_text() -> &'static str {
    "Just a sample text" //&str, rust nie ma samodzielnego str - dynamically sized type
}

// fn get_sample_text2() -> &'static str {
//     String::from("Just a sample text").as_str() //źle bo zwracamy &str czyli tylko
//podgląd do tego co ma w sobie String
// }


fn main() {
    let ref_x;
    {
        let x = 5;
        ref_x = &x;
    }
    //println!("{:?}", ref_x); //actually borrowed



    ////////////////LIFETIME

    let arr1 = [1, 2, 3];
    let arr2 = [4, 5, 6, 7];
    println!("{}", len_longer_array(&arr1, &arr2));
    println!("{:?}", longer_array(&arr2, &arr1));


    // structures instances attributes lifetime

    let text = String::from("Introduction to a long text. The rest of long text with many sentences.");

    let intro = text.split('.').next().expect("Introduction needs a '.'");

    let i = Introduction { intro };

    println!("{:?}", i);
    i.print();
    let x = i.get_intro();
    println!("{:?}", x);



    // static lifetime specifiers

}