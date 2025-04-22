
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

mod m1 {
    pub fn m1_function() {
        println!("Hello from m1_function!");
        m2::m2_function();
    }

    mod m2 {
        pub fn m2_function() {
            println!("Hello from m2_function!");
            crate::m0_function();
        }
    }
}

fn m0_function() {
    println!("Hello from m0_function!");
}


mod outermost {
    pub fn middle_function() {}

    fn middle_secret_function() {}

    mod inside {
        pub fn inner_function() {}
        fn inner_secret_function() {}
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
    m1::m1_function();
    //m1::m2::m2_function(); //inaccessible


    outermost::middle_function();
    // outermost::middle_secret_function();//inaccessible
    // outermost::inside::inner_function();//inaccessible
    // outermost::inside::inner_secret_function();//inaccessible
}