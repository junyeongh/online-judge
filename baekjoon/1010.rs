use std::io::{stdin, stdout, Write};

fn main() {
    let mut input = String::new();
    let _ = stdout().flush();
    stdin().read_line(&mut input).unwrap();
    let n = input.trim().parse::<i32>().unwrap();
    for _ in 0..n {
        input.clear();
        stdin().read_line(&mut input).unwrap();
        let mut nums = input.trim().split_whitespace();
        let a = nums.next().unwrap().parse::<i32>().unwrap();
        let b = nums.next().unwrap().parse::<i32>().unwrap();
        solver(a, b);
        println!("{}", solver(a, b));
    }
}

// Input
// 3
// 2 2
// 1 5
// 13 29

// Output
// 1
// 5
// 67863915
fn solver(a: i32, b: i32) -> i32 {
    if a == b {
        return 1;
    }

    let (n, k) = if a > b {
        (a, std::cmp::min(b, a - b))
    } else {
        (b, std::cmp::min(a, b - a))
    };

    (0..k).fold(1, |acc, i| acc * (n - i) / (i + 1))
    // https://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula
}
