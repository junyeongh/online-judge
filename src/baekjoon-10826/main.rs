use std::io::stdin;

/*
입력: 첫째 줄에 n이 주어진다. n은 10,000보다 작거나 같은 자연수 또는 0이다.

큰 수를 다루기 위한 add_large_number를 구해야 하는 문제
 */
fn add_large_numbers(a: &Vec<u8>, b: &Vec<u8>) -> Vec<u8> {
    let mut result = Vec::new();
    let mut carry = 0;
    let mut i = 0;

    while i < a.len() || i < b.len() || carry > 0 {
        let mut sum = carry;
        if i < a.len() {
            sum += a[i];
        }
        if i < b.len() {
            sum += b[i];
        }
        result.push(sum % 10);
        carry = sum / 10;
        i += 1;
    }

    result
}

fn main() {
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();

    let input = buffer.trim().parse::<usize>().unwrap();

    match input {
        0 => println!("0"),
        1 => println!("1"),
        _ => {
            let mut a = vec![1];
            let mut b = vec![1];
            for _ in 2..input {
                let temp = add_large_numbers(&a, &b);
                a = b;
                b = temp;
            }
            b.reverse();
            let result: String = b.iter().map(|&digit| (digit + b'0') as char).collect();
            println!("{}", result);
        }
    }
}
