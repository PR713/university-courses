use rand::Rng;
//&str static reference to a non-modifiable string in program static memory
//String modifiable string, on heap
fn main() {


    let password = generate_password(12);
}


fn generate_password(length: u32) -> String {
    let chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    String::from("siema")
}