use std::io::{stdin, Read};

fn main() {
    // [러스트 입출력 방법 총정리 - Rust로 알고리즘 풀기](https://velog.io/@unhappydogchew/러스트-입출력-방법-총정리-Rust로-알고리즘-풀기)
    // Single-line input
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();

    println!("{}", buffer);

    // Multi-line input
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();

    let n = buffer.trim().parse::<usize>().unwrap();

    for _ in 0..n {
        buffer.clear();
        stdin().read_line(&mut buffer).unwrap();
    }

    // Multiple numbers as input
    let mut buffer = String::new();
    //     parse all together
    stdin().read_line(&mut buffer).unwrap();
    let mut input = buffer.split_ascii_whitespace().flat_map(str::parse::<i32>);
    let n = input.next().unwrap();
    //     parse one by one
    stdin().read_line(&mut buffer).unwrap();
    let mut input = buffer.trim().split_ascii_whitespace();
    let a = input.next().unwrap().parse::<i32>().unwrap();
    let b = input.next().unwrap().parse::<i32>().unwrap();
    //     parse numbers in a line as a vector
    stdin().read_line(&mut buffer).unwrap();
    let v = buffer
        .split_ascii_whitespace()
        .flat_map(str::parse::<i32>)
        .collect::<Vec<i32>>();
    // Clear buffer before reusing
    buffer.clear();

    // Output
    println!("{}", n);
    println!("{n}");

    // Multi-line output using BufWriter
    // use std::io::{stdout, Write, BufWriter}
    let stdout = stdout();
    let mut writer = BufWriter::new(stdout);

    for i in 0..100_000 {
        writeln!(writer, "{i}").unwrap();
    }

    // String instance as buffer for outbut
    // use std::fmt::Write
    let mut output = String::new();

    for i in 0..100_000 {
        writeln!(output, "{i}").unwrap();
    }

    println!("{output}");
}

// [Introduction - Rust Snippets for Competitive Programming](https://bamgoesn.github.io/rust-ps-md/intro.html)