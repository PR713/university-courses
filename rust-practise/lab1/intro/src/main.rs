
fn main() {

    let phone_entry = ("John Kirby", "+48 600 500 400", 1u8, true);

    println!("Phone number {} belongs to {}", phone_entry.1, phone_entry.0);
    println!("coś {:?}", phone_entry);

    println!("One element tuple: {:?}", (5u32,));

    let (name, number, sex, is_primary) = phone_entry;
    println!("{:?}, {:?}, {:?}, {:?}", name, number, sex, is_primary);

    //Arrays


    let primes = [2, 3, 5, 7, 11, 13, 17, 19]; // type: [i32, 8]
    println!("\n{:?}", primes);

    println!("First prime number is {}", primes[0]);
    println!("Second prime number is {}", primes[1]);


    let zeros = [0; 100];
    println!("{:?}\nlen of 'zeros array': {}", zeros, zeros.len());


    println!("Number of prime numbers in the array: {}", primes.len());
    println!("Number of prime numbers in the array: {}", primes.len());

    println!("The last prime numbers in the array: {}\n", primes[primes.len() - 1]);

    //println!("{}", primes[primes.len()]);


    //multi dimensions arrays

    let mut board = [[' '; 3]; 3];

    board[0][0] = 'x';
    board[0][1] = 'o';
    println!("{:?}", board);

    let board = [['x', 'o', 'x'], ['x', 'o', 'o'], ['x', 'o', 'x']];

    println!("{:?}\n\n", board);


    //functions

    say_hello(5);

    println!("{}", get_one());

    let x = get_one();
    println!("{}", x);

    println!("{}\n\n", increment_by_2(10));


    //flow control


    let y = {
        let x = 3;
        x + 1
    };

    println!("The value of y is {}\n", y);


    let i = 1;
    if i >= 0 {
        println!("Non negative number")
    } else {
        println!("Negative number")
    }

    let abs_i = if i >= 0 { i } else { -1 };
    println!("{}\n", abs_i);



    let i = -1;
    let res = if i >= 0 || i % 2 == 0 { println!("Nonnegative or even") };
    println!("res: {:?}\n", res); //typ jednostkowy ()


    let mut x = 1;

    loop {
        println!("{}", x);
        x = x + 1;

        if x > 10 {
            break;
        }
    }


    let mut x = 1;

    let y = loop {
        println!("{}", x);
        x = x + 1;

        if x > 10 {
            break x; //<- sth like return
        }
    };

    println!("Value of y: {}\n", y);



    let mut i = 0;
    while i < 5 {
        println!("{}", i);
        i += 1;
    }


    let primes: [i32; 8] = [2,3,5,7,11,13,17,19];

    println!("Primes:");

    let mut i = 0;
    while i < primes.len() {
        println!("{}", primes[i]);
        i += 1;
    }

    println!("\n");

    for n in 0..primes.len() {
        println!("{}", n);
    }

    for i in 0..10 {
        println!("{}", i);
    }

    //cargo w RustRover
}





fn say_hello(x : i32) {
    println!("Hello guys! I am a fn with an integer parameter {}", x);
}


fn get_one() -> i32 {
    1
}


fn increment_by_2(n : i32) -> i32 {
    n + 2
}
