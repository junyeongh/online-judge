// https://www.acmicpc.net/problem/2475
use std::io::{stdin, stdout, Write};

fn main() {
    let mut input = String::new();
    let _ = stdout().flush();
    stdin().read_line(&mut input).unwrap();
    let n = input
        .trim()
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<i32>>()
        .iter()
        .fold(0, |acc, x| acc + x * x);
    println!("{}", n % 10);
}
