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


    // anonymous functions / function objects

    println!("\n\nLITERAŁY");

    let increment_v1 = |x: u32| -> u32 { x + 1 };
    let increment_v2 = |x| { x + 1 };
    let increment_v3 = |x| x + 1; // only if there is only one expression

    assert_eq!(increment_v1(4), 5); // calling functional object
    assert_eq!(increment_v2(4), 5);
    assert_eq!(increment_v3(4), 5);


    let mut x = 5;
    let mul_5 = |a| a * x;

    assert_eq!(mul_5(4), 20);

    let mut x = 5;
    let mut add_to_x = |a| x += a;

    add_to_x(5);
    add_to_x(1);
    assert_eq!(x, 11);

    x += 1;
    assert_eq!(x, 12);


    let mut x = vec![1, 2, 3];
    let equal_to_x = move |y| y == x;  // equal_to_x becomes the owner of x

    // println!("can't use x here: {:?}", x); // ^ keyword 'move'

    let y = vec![1, 2, 3];
    assert!(equal_to_x(y));
    //println!("{:?}", y); //cant use too

    let v = vec![1, 2, 3];
    let mut iter = v.iter(); // must be mutable

    assert_eq!(Some(&1), iter.next());
    assert_eq!(Some(&2), iter.next());
    assert_eq!(Some(&3), iter.next());
    assert_eq!(None, iter.next());


    let v = vec![1, 2, 3];
    let iter = v.iter();
    assert_eq!(6, iter.sum()); // consumes the iterator

    let v = vec![1, 2, 3];
    assert_eq!(3, v.iter().count()); // consumes the iterator

    let a = [1, 2, 3];
    let v = a.iter().collect::<Vec<_>>(); // turbofish syntax
    assert_eq!(&1, *v.get(0).unwrap()); // :>


    let v = vec![1, 2, 3];
    // transforming each element
    let res = v.iter().map(|x| x * 2).collect::<Vec<i32>>();
    assert_eq!(vec![2, 4, 6], res);

    // filter elements
    let res = v.iter().filter(|&x| *x % 2 == 0).map(|x| *x).collect::<Vec<i32>>();
    assert_eq!(vec![2], res);

    /////////

    let mut v = vec![1, 2, 3];

    v.iter_mut().map(|x| *x +=1).collect::<Vec<_>>();
    assert_eq!(vec![2, 3, 4], v);


    let v = vec![1, 2, 3];
    let v2 = v.into_iter().map(|x | x * 2).collect::<Vec<_>>();

    // v.get(0); // cannot use v anymore - it's moved

    assert_eq!(vec![2, 4, 6], v2);


    //todo
}
