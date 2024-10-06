use std::io::stdin;
// use std::io::{stdin, Read};

// [Introduction - Rust Snippets for Competitive Programming](https://bamgoesn.github.io/rust-ps-md/intro.html)
// [러스트 입출력 방법 총정리 - Rust로 알고리즘 풀기](https://velog.io/@unhappydogchew/러스트-입출력-방법-총정리-Rust로-알고리즘-풀기)
fn main() {
    println!("Different ways to input/output for competitive programming in Rust");
}

fn input_single_line() {
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();

    println!("{}", buffer);

    let input = buffer.trim().parse::<i32>().unwrap();
    println("{}", input);
}

fn input_multi_line() {
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();

    let n = buffer.trim().parse::<usize>().unwrap();

    for _ in 0..n {
        buffer.clear();
        stdin().read_line(&mut buffer).unwrap();
    }
}

fn input_multiple_numbers() {
    // Multiple numbers as input
    let mut buffer = String::new();

    // 1. parse all together
    stdin().read_line(&mut buffer).unwrap();
    let mut input = buffer.split_ascii_whitespace().flat_map(str::parse::<i32>);
    let n = input.next().unwrap();

    // 2. parse one by one
    stdin().read_line(&mut buffer).unwrap();
    let mut input = buffer.trim().split_ascii_whitespace();
    let a = input.next().unwrap().parse::<i32>().unwrap();
    let b = input.next().unwrap().parse::<i32>().unwrap();

    // 3. parse numbers in a line as a vector
    stdin().read_line(&mut buffer).unwrap();
    let v = buffer
        .split_ascii_whitespace()
        .flat_map(str::parse::<i32>)
        .collect::<Vec<i32>>();

    // Clear buffer before reusing
    buffer.clear();
}

fn output_multi_line() {
    // Multi-line output using BufWriter
    // use std::io::{stdout, Write, BufWriter}
    let stdout = stdout();
    let mut writer = BufWriter::new(stdout);

    for i in 0..100_000 {
        writeln!(writer, "{i}").unwrap();
    }
}

fn output_string_instance_as_buffer() {
    // String instance as buffer for output
    // use std::fmt::Write
    let mut output = String::new();

    for i in 0..100_000 {
        writeln!(output, "{i}").unwrap();
    }

    println!("{}", output);
}
