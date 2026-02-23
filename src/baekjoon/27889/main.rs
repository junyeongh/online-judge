use std::io::{stdin, Read};

fn main() {
    let NLCS = "North London Collegiate School";
    let BHA = "Branksome Hall Asia";
    let KIS = "Korea International School";
    let SJA = "St. Johnsbury Academy";

    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();

    // `match` syntax is pretty awesome
    match buffer.trim() {
        "NLCS" => println!("{}", NLCS),
        "BHA" => println!("{}", BHA),
        "KIS" => println!("{}", KIS),
        "SJA" => println!("{}", SJA),
        _ => unreachable!(),
    }
}
