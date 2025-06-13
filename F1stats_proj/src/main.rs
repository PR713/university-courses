use std::fs::File;
use std::io::{BufReader, BufWriter};
use std::path::Path;
use chrono::{DateTime, Duration, Utc};
use serde::{Deserialize, Serialize};
use anyhow::Result;

const DATA_FILE : &str = "data.json";

const API_QUERY : &str = "https://api.openf1.org/v1/car_data?driver_number=55&session_key=9159";

#[derive(Serialize, Deserialize)]
struct CarData {
    brake : u32,
    date: DateTime<Utc>,
    driver_number: u32,
    drs: u8,
    meeting_key: u32,
    n_gear: u8,
    rpm: u32,
    session_key: u32,
    speed: u32,
    throttle: u8
}


fn fetch_car_data(url: &str, data_file : &str) -> Result<()> {
    let data = reqwest::blocking::get(url)?.text()?;
    let car_data : Vec<CarData> = serde_json::from_str(&data)?;
    let writer = BufWriter::new(File::create(data_file)?);
    serde_json::to_writer(writer, &car_data)?;
    Ok(())
}

fn load_car_data_from_file(data_file : &str) -> Result<Vec<CarData>> {
    let car_data : Vec<CarData> = serde_json::from_reader(BufReader::new(File::open(data_file)?))?;
    Ok(car_data)
}

fn check_if_data_exists(data_file : &str) -> bool {
    Path::new(data_file).exists()
}

fn average(car_data : &Vec<CarData>) -> f64 {
    let sum: f64 = car_data.iter().map(|data| data.speed as f64).sum();
    sum / car_data.len() as f64
}

fn high_speed(car_data : &Vec<CarData>, speed_threshold : f64) -> Duration {
    let mut total_duraion = Duration::zero();
    let mut last_time: Option<DateTime<Utc>> = None;

    for data in car_data.iter().filter(|data| data.speed as f64 > speed_threshold) {
        if let Some(prev) = last_time {
            let duration = data.date - prev;
            if duration.num_seconds() < 5 {
                total_duraion += duration;
            }
        }
        last_time = Some(data.date);
    }

    total_duraion
}


fn max_rpm(car_data : &Vec<CarData>) -> Option<(u32, u8)> {
    car_data.iter().max_by_key(|data| data.rpm)
        .map(|data| (data.rpm, data.n_gear))
}


fn main() -> Result<()> {

    if !check_if_data_exists(DATA_FILE) {
        fetch_car_data(API_QUERY, DATA_FILE)?;
    }

    let car_data = load_car_data_from_file(DATA_FILE).unwrap();

    let average_speed = average(&car_data);
    println!("Average Speed: {}", average_speed);

    let threshold = 300; // Przykład: 300 km/h
    let fast_time = high_speed(&car_data, threshold as f64);
    println!("Czas jazdy > {} km/h: {} sekund", threshold, fast_time.num_seconds());

    if let Some((rpm, gear)) = max_rpm(&car_data) {
        println!("Maksymalne RPM: {} na biegu: {}", rpm, gear);
    } else {
        println!("Brak danych RPM.");
    }

    Ok(())
}
