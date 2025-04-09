
mod my_module {
    pub fn my_function() {
        println!("Hello from my_module!");
    }

    pub mod my_submodule {
        pub fn my_subfunction() {
            println!("Hello from my_submodule!");
        }
    }
}

fn main() {
    my_module::my_function();
    my_module::my_submodule::my_subfunction();
    //lub

    crate::my_module::my_function();
    crate::my_module::my_submodule::my_subfunction();

    // my_function(); //<- ale z użyciem use my_module::my_function;
    // my_subfunction();


    //rules of privacy
}