

pub struct Participant {
    pub name: String,
    pub password: String,
    pub age: i32,
    pub score: i32,
    pub experience: i32,
    pub has_premium_membership: bool,
}
pub fn create_participant(name: String, password: String, age: i32, score: i32, experience: i32, has_premium_membership: bool) -> Participant {
    Participant{name, password, age, score, experience, has_premium_membership}
}