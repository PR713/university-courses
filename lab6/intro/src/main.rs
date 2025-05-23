use std::collections::HashMap;

fn words_stats(words: &Vec<String>) -> HashMap<String, i32> {
    let mut stats: HashMap<String, i32> = HashMap::new();

    for word in words { //bez & bo już mamy pożyczkę w sygnaturze
        // if let Some(cnt) = stats.get_mut(word) {
        //     *cnt += 1;
        // } else {
        //     stats.insert(word.to_string(), 1);
        // }
        //lub:

        let cnt = stats.get_mut(word);

        match cnt {
            Some(cnt) => *cnt += 1,
            None => {
                stats.insert(word.to_string(), 1);
            }
        }
        //lub map.entry(word.to_owned()).or_insert(0) += 1; po prostu xd
    }

    stats
}


fn hash_map_words_stats_poem() {
    let response = reqwest::blocking::get("https://wolnelektury.pl/media/book/txt/pan-tadeusz.txt").expect("Cannot get poem from a given URL");
    let poem = response.text().unwrap();

    let stats = words_stats(&split_to_words(&poem));
    let sorted_stats = sort_stats(&stats);
    println!("{:?}", &sorted_stats[..20]);
}


fn split_to_words(s: &str) -> Vec<String> {
    let mut words = Vec::new();
    for word in s.split_whitespace() {
        let unified_word = word.trim_matches(|c| char::is_ascii_punctuation(&c)).to_lowercase();
        words.push(unified_word);
    }
    words
}

fn sort_stats(stats : &HashMap<String, i32>) -> Vec<(&str, i32)> {
    let mut sorted_stats : Vec<(&str, i32)> = Vec::new();
    for (word, count) in stats.iter() {
        sorted_stats.push((word, *count));
    }

    sorted_stats.sort_by(|(_, c1), (_, c2)| c2.partial_cmp(c1).expect("FAILED"));

    sorted_stats
}


fn main() {
    // new empty vector
    let v: Vec<i32> = Vec::new();

    // new vector with values
    let mut v = vec![1, 2, 3];


    let e1 : &i32 = &v[1];

    let e2 = v.get(2);

    // adding values to vector
    v.push(4);
    v.push(5);

    // removing values
    let e = v.pop();


    let first = &v[0];

    v.push(4); //mutowalna pożyczka &mut self

    //println!("{}", *first); // uncomment to see the compile error
    //używamy niemutowalnej


    for e in v {
        println!("{} .", e);
    }

    // cannot use v here
    //let eo = &v[0]; // will cause an error

    let v = vec![1, 2, 3];

    for e in &v { // need to use reference (otherwise the v value is moved)
        println!("{}", *e); // need to explicitly derefer the value
    };


    let mut v = vec![1, 2, 3];

    for e in &mut v { // mutable borrow
        *e *= 2; // remember to use dereference operator
    }


    //map

    let mut map = HashMap::new();

    map.insert(String::from("world"), 1);
    map.insert(String::from("rust"), 2);

    map.remove("world");
    let cnt : Option<&i32> = map.get("rust"); // returns an optional reference to a value in the map

    for (text, number) in &map { // immutable borrow
        println!("{} has {} occurrences", text, number);
    }


    //
    //hash_map_words_stats_poem();

    let entry = map.entry("rust".to_string());
    let word = "python".to_string();
    let cnt : &mut i32 = map.entry(word.to_owned()).or_insert(0);
    *cnt += 1; //lub od razu map.entry... += 1
    println!("\n {}", cnt);

    println!("{:?}", map);
    println!("{}", word); //to_owned method cloned that variable :)

    map.entry(word.to_owned()).and_modify(|counter| *counter += 1).or_insert(1);

    
}
