fn sum(x : Option<i32>, y : Option<i32>) -> Option<i32> {
    match (x, y) {
        (Some(x), Some(y)) => Some(x + y),
        _ => None
    }
}

fn sum1(x : Option<i32>, y : Option<i32>) -> Option<i32> {
    Some(x? + y?)
}


fn maybe_icecream(time_of_day: u16) -> Option<u16> {
    // We use the 24-hour system here, so 10PM is a value of 22 and 12AM is a
    // value of 0. The Option output should gracefully handle cases where
    // time_of_day > 23.

    match time_of_day {
        0..=21 => Some(5),
        22 | 23 => Some(0),
        _ => None
    }
}


struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let a = sum(Some(10), Some(20));
    let b = sum(Some(10), None);
    println!("{:?}", a);
    println!("{:?}", b);

    let c = sum1(Some(20), None);
    println!("{:?}", c);

    //////////////////


    let y: Option<Point> = Some(Point { x: 100, y: 200 });

    match &y {
        Some(p) => println!("Co-ordinates are {},{} ", p.x, p.y),
        _ => panic!("no match!"),
    }
    y; // Fix without deleting this line.
}





#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn check_icecream() {
        assert_eq!(maybe_icecream(0), Some(5));
        assert_eq!(maybe_icecream(9), Some(5));
        assert_eq!(maybe_icecream(18), Some(5));
        assert_eq!(maybe_icecream(22), Some(0));
        assert_eq!(maybe_icecream(23), Some(0));
        assert_eq!(maybe_icecream(25), None);
    }

    #[test]
    fn raw_value() {
        // TODO: Fix this test. How do you get at the value contained in the
        // Option?
        let icecreams = maybe_icecream(12);
        assert_eq!(icecreams.unwrap(), 5);
    }
}