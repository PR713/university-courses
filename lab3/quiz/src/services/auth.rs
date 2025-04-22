use crate::models;
use crate::models::user::participant::Participant;

pub fn login(participant: Participant) {
    println!("Logging in participant: {}", participant.name);
}