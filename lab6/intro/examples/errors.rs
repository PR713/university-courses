use std::{fs, io};
use reqwest::Error;

struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    fn new1(width: f64, height: f64) -> Rectangle {
        if width <= 0.0 || height <= 0.0 {
            panic!("Invalid width or height");
        }
        Rectangle { width, height }
    }

    fn new2(width: f64, height: f64) -> Option<Rectangle> {
        if width <= 0.0 || height <= 0.0 {
            return None
        }
        Some(Rectangle { width, height })
    }

    fn new(width : f64, height : f64) -> Result<Rectangle, String> {
        if width <= 0.0 || height <= 0.0 {
            return Err("Rectangle cannot have negative width or height".to_string());
        }
        Ok(Rectangle { width, height })
    }

    fn new3(width : f64, height : f64) -> Result<Rectangle, Box<dyn std::error::Error>> {
        if width <= 0.0 || height <= 0.0 {
            return Err("Rectangle cannot have negative width or height".into());
        }
        Ok(Rectangle { width, height })
    }

    fn area(&self) -> f64 {
        self.width * self.height
    }


    fn read_from_file(path : &str) -> Result<Rectangle, Box<dyn std::error::Error> > {
        //nie można po prostu Box<Error> bo Error to trait, Box<T>
        //gdzie T to albo enum albo typ, więc wprowadzono dyn jako dynamiczny dispatch
        //czyli wywowałanie funkcji w czasie działania programu a nie kompilacji
        // -> trait object, czyli jakiś typ implementujący cechę Error
        let s = fs::read_to_string(path)?;
        let mut iter = s.split_whitespace();
        let width : f64 = iter.next().ok_or("Cannot convert string to width".to_string())?.parse()?;
        let height : f64 = iter.next().ok_or("Cannot convert string to height".to_string())?.parse()?;

        Rectangle::new3(width, height)

    }
}



const DEFAULT_WIDTH: f64 = 1.0;
const DEFAULT_HEIGHT: f64 = 1.0;

impl Default for Rectangle {

    fn default() -> Self {
        Rectangle{ width : DEFAULT_WIDTH, height : DEFAULT_HEIGHT }
    }
}



fn bigger(w1: f64, h1: f64, w2 : f64, h2 : f64) -> Result<Rectangle, String> {
    let r1 = Rectangle::new(w1, h1);
    let r2 = Rectangle::new(w2, h2);

    match (r1, r2) {
        (Ok(rec1), Ok(rec2)) => {
            if rec1.area() > rec2.area() {
                Ok(rec1)
            } else {
                Ok(rec2)
            }
        },
        _ => Err("Rectangle cannot have negative width or height".to_string())
    }
}


fn bigger1(w1: f64, h1 : f64, w2 : f64, h2 : f64) -> Result<Rectangle, String> {
    let r1 = Rectangle::new(w1, h1)?;
    let r2 = Rectangle::new(w2, h2)?;

    if r1.area() > r2.area() {
        Ok(r1)
    } else {
        Ok(r2)
    }
}



#[cfg(test)]
mod tests {
    #[test]
    fn test_new_rectangle(){
        let width = 4.1;
        let height = 3.5;

        let r = Rectangle::new1(width, height);
        assert!((r.width-width).abs() < f64::EPSILON && (r.height-height).abs() < f64::EPSILON);
    }


    #[test]
    #[should_panic]
    fn test_new_rectangle_with_negatives(){
        let width = 4.1;
        let height = -3.5;

        let r = Rectangle::new1(width, height);
    }


    #[test]
    fn test_new_rectangle_with_negatives2() {
        let width = 4.1;
        let height = -3.5;
        let r = Rectangle::new2(width, height);
        assert!(r.is_none())
    }
    use super::*;


    #[test]
    fn test_new_rectangle1() {
        // given
        let width = 4.5;
        let height = 5.7;

        // when
        let r = Rectangle::new(width, height).unwrap();

        // then
        assert!((r.width - width).abs() < f64::EPSILON && (r.height - height).abs() < f64::EPSILON);
    }

    #[test]
    fn test_new_rectangle_with_negative1() {
        let r = Rectangle::new(-1.0, 1.0);
        match r {
            Err(s) => assert_eq!("Rectangle cannot have negative width or height", s.as_str()),
            Ok(_) => panic!() // the result shouldn't be Ok
        }
    }


    #[test]
    #[should_panic]
    fn test_unwrap() {
        // that is ok
        let r = Rectangle::new(1.0, 2.0);
        let rec = r.unwrap(); // consumes the value

        // that generates panic
        let r = Rectangle::new(-1.0, 2.0);
        let rec = r.unwrap(); // consumes the value

    }

    #[test]
    #[should_panic]
    fn test_expect() {
        // that is ok
        let r = Rectangle::new(1.0, 2.0);
        let rec = r.expect("This should be always a proper rectangle");

        // that generates panic
        let r = Rectangle::new(1.0, -2.0);
        let rec = r.expect("Don't do that!");
    }


    #[test]
    fn test_is_ok() {
        let r = Rectangle::new(1.0, 2.0);
        assert!(r.is_ok());
        assert!(!r.is_err());
    }


    #[test]
    fn test_unwrap_or_else() {
        let r = Rectangle::new(-1.0, -2.0);
        let rec = r.unwrap_or_else(|_| Rectangle::new(DEFAULT_WIDTH, DEFAULT_HEIGHT).unwrap());

        assert!((rec.width - DEFAULT_WIDTH).abs() < f64::EPSILON && (rec.height - DEFAULT_HEIGHT).abs() < f64::EPSILON);
    }


    #[test]
    fn test_unwrap_or_default() {
        let r = Rectangle::new(-1.0, -2.0);
        let rec = r.unwrap_or_default();

        assert!((rec.width - DEFAULT_WIDTH).abs() < f64::EPSILON && (rec.height - DEFAULT_HEIGHT).abs() < f64::EPSILON);

        let r = Rectangle::new(1.0, 2.0);
        let rec = r.unwrap_or_default();
        assert!((rec.width - 1.0).abs() < f64::EPSILON && (rec.height - 2.0).abs() < f64::EPSILON);
    }


    //propagacja błędów

    #[test]
    fn test_bigger() {
        // given
        let w1 = 1.0;
        let h1 = 2.0;
        let w2 = 3.0;
        let h2 = 4.0;

        // when
        let r = bigger(w1, h1, w2, h2);

        // then
        assert!((r.unwrap().area() - (w2 * h2)).abs() < f64::EPSILON);
    }

    #[test]
    fn test_bigger_err() {
        // given
        let w1 = 1.0;
        let h1 = -2.0; // wrong width
        let w2 = 3.0;
        let h2 = 4.0;

        // when
        let r = bigger(w1, h1, w2, h2);

        // then
        assert!(r.is_err());
    }

    #[test]
    fn test_bigger1() {
        let w1 = 1.0;
        let h1 = 2.0;
        let w2 = 3.0;
        let h2 = 4.0;

        let r = bigger1(w1, h1, w2, h2);

        assert!((r.unwrap().area() - (w2 * h2)).abs() < f64::EPSILON);
    }

    #[test]
    fn test_bigger1_err(){
        let w1 = 1.0;
        let h1 = -2.0;
        let w2 = 3.0;
        let h2 = 4.0;

        let r = bigger1(w1, h1, w2, h2);

        assert!(r.is_err());
    }


    // read_from_file


    #[test]
    fn test_read_from_not_existing_file() {
        // given
        let path = "not-existing-file.txt";

        // when
        let r = Rectangle::read_from_file(path);

        // then
        match r {
            Err(ref e) if e.is::<std::io::Error>() => println!("ok"),
            _ => panic!()
        }
    }
}


fn main() {}