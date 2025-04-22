use std::ops::{Add, Sub};
use std::ptr::addr_of;

pub struct Vec2D{
    pub x:f32,
    pub y:f32,
}

impl Vec2D{
    pub fn print(&self){
        println!("[{}, {}]",self.x, self.y);
    }

    pub fn to_unit(&self) -> Vec2D{
        let length = (self.x.powi(2) + self.y.powi(2)).sqrt();
        Vec2D{x: self.x/length, y: self.y/length}
    }

    pub fn equals(&self, other: &Vec2D)->bool{
        self.x == other.x && self.y == other.y
    }
}


impl<'a, 'b> Add<&'b Vec2D> for &'a Vec2D {
    type Output = Vec2D;

    fn add(self, other: &'b Vec2D) -> Vec2D {
        // self jest już typu &'a Vec2D, bo for &'a Vec2D
        // other jest typu &'b Vec2D
        //Add domyślnie dla for Vec2D przejmuje ownership więc musimy zrobić
        //for &'a Vec2D, tak jest zdefiniowany w bibliotece:
        //pub trait Add<Rhs = Self> {
        //     type Output;
        //     fn add(self, rhs: Rhs) -> Self::Output;
        // }
        Vec2D {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}


impl Sub for Vec2D{
    type Output = Self;

    fn sub(self, other: Self) -> Self{
        Vec2D{x: self.x - other.x, y: self.y - other.y}
    }
}

pub(crate) trait Product {
    fn product(self, other: Vec2D) ->Vec2D;
    fn product_by_scalar(&self, scalar: f32) -> Vec2D;
}

impl Product for Vec2D {
    fn product(self, other: Vec2D) -> Vec2D{
        Vec2D{x: self.x * other.x, y: self.y * other.y}
    }

    fn product_by_scalar(&self, scalar: f32) -> Vec2D{
        Vec2D{x: self.x * scalar, y: self.y * scalar}
    }
}