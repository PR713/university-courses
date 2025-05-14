struct Pair<T> {
    x: T,
    y: T
}

struct MyPair<T,V> {
    x: T,
    y: V
}

fn extract_x<T>(p : Pair<T>) -> T {
    p.x
}

impl <T> Pair<T> {
    fn extract_x(self) -> T {
        self.x
    }
}

// impl Pair<i32> {
//     fn bigger(&self) -> i32 {
//         if self.x > self.y {
//             self.x
//         } else {
//             self.y
//         }
//     }


impl <T: PartialOrd + Copy> Pair<T> {
    fn bigger(&self) -> T {
        if self.x > self.y {
            self.x
        } else {
            self.y
        }
    }
}
//fn some_function<T: Display + Clone, U : Debug + Clone>(t: T, u: U) -> i32 {
//     ...
// }
// or
//fn some_function<T, U>(t: T, u: U) -> i32
//     where T : Display + Clone,
//           U : Debug + Clone
// {
//     ...
// }




//Napisz funkcję max, która zwróci największą wartość tablicy zawierającej dowolne typy liczbowe.
//Funkcja powinna zwracać Some(max) lub None w przypadku pustej tablicy.

fn max<T: PartialOrd + Copy> (arr: &[T]) -> T {
    if arr.is_empty() {
        return None;
    }

    let mut max_val = arr[0];

    for &item in arr.iter().skip(1) {
        if item > max_val {
            max_val = item;
        }
    }

    Some(max_val)
}

//(*) Napisz funkcję mean, która wyznaczy średnią arytmentyczną elementów tablicy zawierającej
//dowolne typy liczbowe.

fn mean(){

}

//Napisz funkcję dodawanie par liczbowych (struktur typu Pair).

fn add_pairs<T>(p1 : Pair<T>, p2 : Pair<T>) {

}

fn main() {
    let pi = Pair{x : 5, y : 3};

    let pf = Pair {x: 15f64, y : 12.0f64};

    //let pw = Pair {x: 15f64, y : 12}; //must be the same type

    let pw = MyPair{x : 15f64, y : 12};

    pi.bigger();
    pf.bigger();
}
