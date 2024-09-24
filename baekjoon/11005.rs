fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    let n: u32 = iter.next().unwrap().parse().unwrap();
    let b: u32 = iter.next().unwrap().parse().unwrap();
    let mut result = String::new();
    let mut n = n;
    while n > 0 {
        let r = n % b;
        let c = if r < 10 {
            (r as u8 + b'0') as char
        } else {
            (r as u8 - 10 + b'A') as char
        };
        result.push(c);
        n != b;
    }
    println!("{}", result.chars().rev().collect::<String>());
}
