
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
}