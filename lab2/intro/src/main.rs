
fn main() {
    let mut s = String::from("sample text"); // memory alocation 

    s.push_str(" with some additional text");

    println!("{}", s);


    let s1 = String::from("sample");
    let s2 = s1;

    println!("\n\n{}", s2);
    //println!("{}", s1); // error, the value is invalid



    let a = 6;
    let b = a;

    println!("\n\n{}", a);
    println!("{}", b); //copyable



    let s1 = String::from("sample");
    let s2 = s1.clone();

    println!("\n\n{}", s2);
    println!("{}", s1); // we have two copies of "sample" text at a heap



    //////////////


    let n = 5;

    process_number(n);
    process_number(n+1);

    let text = String::from("sample");

    process_text(text);
    //process_text(text); //the owner is that function -> ...

    //borrowing &text is the same as pointer in C/C++, but let s1 = &s (s = string)
    // s1 is a type of &String, the println!("{s1}"); will print s not address of s,
    //it is dereferenced automatically 


    ///////////////////////////



    let s1 = create_text();
    println!("\n\n{}", s1);




    let s1 = String::from("sample text");
    let s2 = process_text1(s1);
    println!("\n\n{}", s2);





    let s1 = String::from("sample");
    let s2 = process_text2(&s1);  // lends the s1 value through a reference
    println!("\n\n{} -> {}", s1, s2); // both s1 and s2 are valid



    /////////////


    let mut s1 = String::from("sample text");
    process_text3(&mut s1, 4);
    println!("linia 80\n\n{}", s1);


    ////



    let mut s = String::from("sample");
    let s1 = &mut s;
    //let s2 = &mut s; //cant borrow 2nd time

    //println!("{}, {}", s1, s2);


    ///

    let mut s = String::from("sample");
    let s1 = &mut s;
    //let s2 = s; //cant move the s because it is borrowed

    //println!("{}, {}", s1, s2);



    //let s = generate_ref_to_string();
    // when functions ends the reference to string created in the body 
    // of that function is deallocated




    //////////////////////Correct code exercise


    let mut x = 100;
    let y = &mut x;
    *y += 100;
    let z = &mut x; // y is no more used, so we can do that
    *z += 1000;
    assert_eq!(x, 1200);
    println!("x value {}", x);



    let data = "Rust is great!".to_string();

    let x = get_char(&data);
    println!("x: {}", x);

    string_uppercase(data);




    //////slicing:


    let s = String::from("string slice demonstration");

    let s1 = &s[7..12];

    println!("{}", s1);


    ///


    let s = String::from("string slice demonstration");

    let s1 = &s[..12];
    let s2 = &s[6..];
    let s3 = &s[..];

    println!("{} {} {}", s1, s2, s3);


    let mut s = String::from("text that illustrates slices");
    let first = first_word(&s[..]).to_string(); // inaczej mamy
    // błąd bez .to_string() bo tutam mamy pożyczkę na część danych i nie możemy orignału modyfikować

    s.clear(); //tries to modify text

    println!("{first}\n");


    ///
    assert_eq!(trim_me("Hello!     "), "Hello!");
    assert_eq!(trim_me("  What's up!"), "What's up!");
    assert_eq!(trim_me("   Hola!  "), "Hola!");


    assert_eq!(compose_me("Hello"), "Hello world!");
    assert_eq!(compose_me("Goodbye"), "Goodbye world!");


    assert_eq!(replace_me("I think cars are cool"), "I think balloons are cool");
    assert_eq!(replace_me("I love to look at cars"), "I love to look at balloons");
    println!("{}", trim_me(" I think cars...  "));
    println!("{}", trim_me(""));

    //Table slicing TODO

} // s is going out of scope, the memory is automatically freed
// no garbage collector or manual free needed



fn process_text(s : String) {
    println!("Processing text: {}", s); //if &String ten s or *s
}

fn process_number(n : i32) {
    println!("Processing number: {}", n)
}

fn create_text() -> String {
    String::from("text created inside a function")
}

fn process_text1(s: String) -> String {
    s.to_uppercase()
}

fn process_text2(s: &String) -> String { // borrow s value and return new string
    s.to_uppercase()
}

fn process_text3(s: &mut String, len : usize ) {
    s.truncate(len)
}

//fn generate_ref_to_string() -> &String {
//    &String::from("dangling text")
//}


fn get_char(data: &String) -> char {
    data.chars().last().unwrap()
}

// Should take ownership
fn string_uppercase(mut data: String) {
    data = data.to_uppercase();

    println!("{}", data);
}


fn first_word(s : &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[..i]
        }
    }
    s
}

fn trim_me(s: &str) -> &str {
    let bytes = s.as_bytes();
    let n = bytes.len();
    let mut start = 0;
    let mut end = s.len();

    if end == 0 {
        return ""
    }

    if end == 1 {
        if bytes[0] == b' ' {
            return ""
        }
        return &s[start..end]
    }

    while start < end - 1 && bytes[start] == b' '{ //if only " " then at the end we return "" empty string
        start += 1;
    }

    while end - 1 > start && bytes[end - 1] == b' ' {
        end -= 1;
    } //even >= but equality would never cause the end - 1 < start due to first while
    //always start is the boundary, so end - 1 will max be possibly equal to start and won't go below start

    if start == end {
        return ""
    }

    &s[start..end]
}

fn compose_me(input: &str) -> String {
    // TODO: Add " world!" to the string! There's multiple ways to do this!
    //format!("{} world!", input)
    //lub
    let mut result = String::from(input);
    result.push_str(" world!"); //dla input no method push_str found in &str
    result
}

fn replace_me(input: &str) -> String {
    // TODO: Replace "cars" in the string with "balloons"!
    input.replace("cars", "balloons")
}