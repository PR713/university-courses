use crate::models::user::participant;

mod models;
mod services;

fn main() {
    let name = String::from("Rust");
    let password = String::from("123456");
    let age = 30;
    let score = 0;
    let experience = 1;
    let has_premium_membership = true;

    let participant = participant::create_participant(name, password, age, score, experience, has_premium_membership);
    services::auth::login(participant);
}
