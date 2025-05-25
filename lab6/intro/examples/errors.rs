
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    fn new(width: f64, height: f64) -> Rectangle {
        if width <= 0.0 || height <= 0.0 {
            panic!("Invalid width or height");
        }
        Rectangle { width, height }
    }

    fn area(&self) -> f64 {
        self.width * self.height
    }
}


#[cfg(test)]
mod tests {
    #[test]
    fn test_new_rectangle(){
        let width = 4.1;
        let height = 3.5;

        let r = Rectangle::new(width, height);
        assert!((r.width-width).abs() < f64::EPSILON && (r.height-height).abs() < f64::EPSILON);
    }


    #[test]
    #[should_panic]
    fn test_new_rectangle_with_negatives(){
        let width = 4.1;
        let height = -3.5;

        let r = Rectangle::new(width, height);
    }
    use super::*;
}


fn main() {}