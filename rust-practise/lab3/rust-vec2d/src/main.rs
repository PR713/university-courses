use std::ops::Add;
use crate::vec2d::{Vec2D, Product};

mod vec2d;

fn main() {
    let vec = Vec2D{x:1.0,y:2.0};
    vec.print();
    let unit_vec = vec.to_unit();
    unit_vec.print();

    vec.equals(&unit_vec);

    //let new_vec = &vec + &unit_vec; // lub równoważnie bez syntax sugar
    let new_vec = vec.add(&unit_vec);
    new_vec.print();

    let new_vec2 = vec - new_vec;//tracimy oba
    new_vec2.print();

    let product_vec = unit_vec.product(Vec2D{x: 1.0, y: 1.0});
    product_vec.print();

    let product_vec_scalar = product_vec.product_by_scalar(10.0);
    product_vec_scalar.print();
}



//TESTY

#[cfg(test)]
mod tests {
    use super::*;
    use crate::vec2d::Vec2D;

    #[test]
    fn test_vec2d_creation() {
        let vec = Vec2D { x: 1.0, y: 2.0 };
        assert_eq!(vec.x, 1.0);
        assert_eq!(vec.y, 2.0);
    }

    #[test]
    fn test_to_unit() {
        let vec = Vec2D { x: 3.0, y: 4.0 };
        let unit_vec = vec.to_unit();
        let expected_length = 1.0;
        let actual_length = (unit_vec.x.powi(2) + unit_vec.y.powi(2)).sqrt();
        assert!((actual_length - expected_length).abs() < f32::EPSILON);
    }

    #[test]
    fn test_equals() {
        let vec1 = Vec2D { x: 1.0, y: 2.0 };
        let vec2 = Vec2D { x: 1.0, y: 2.0 };
        let vec3 = Vec2D { x: 1.1, y: 2.0 };

        assert!(vec1.equals(&vec2));
        assert!(!vec1.equals(&vec3));
    }

    #[test]
    fn test_addition() {
        let vec1 = Vec2D { x: 1.0, y: 2.0 };
        let vec2 = Vec2D { x: 3.0, y: 4.0 };
        let result = &vec1 + &vec2;

        assert_eq!(result.x, 4.0);
        assert_eq!(result.y, 6.0);
    }

    #[test]
    fn test_subtraction() {
        let vec1 = Vec2D { x: 1.0, y: 2.0 };
        let vec2 = Vec2D { x: 3.0, y: 4.0 };
        let result = vec1 - vec2;

        assert_eq!(result.x, -2.0);
        assert_eq!(result.y, -2.0);
    }

    #[test]
    fn test_product() {
        let vec1 = Vec2D { x: 1.0, y: 2.0 };
        let vec2 = Vec2D { x: 3.0, y: 4.0 };
        let result = vec1.product(vec2);

        assert_eq!(result.x, 3.0);
        assert_eq!(result.y, 8.0);
    }

    #[test]
    fn test_product_by_scalar() {
        let vec = Vec2D { x: 1.0, y: 2.0 };
        let result = vec.product_by_scalar(3.0);

        assert_eq!(result.x, 3.0);
        assert_eq!(result.y, 6.0);
    }

    #[test]
    fn test_print() {
        let vec = Vec2D { x: 1.0, y: 2.0 };
        vec.print();
    }
}