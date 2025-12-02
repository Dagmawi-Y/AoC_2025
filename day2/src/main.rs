use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").expect("failed to read input");

    let mut sum: u64 = 0;

    for range in input.trim().split(',') {
        let (start_s, end_s) = range.split_once('-').unwrap();
        let start: u64 = start_s.parse().unwrap();
        let end: u64 = end_s.parse().unwrap();

        for id in start..=end {
            if is_double_pattern(id) {
                sum += id;
            }
        }
    }

    println!("{}", sum);
}

fn is_double_pattern(n: u64) -> bool {
    let s = n.to_string();
    let len = s.len();

    // must be even len to split into two equal halves
    if len % 2 != 0 {
        return false;
    }

    let mid = len / 2;
    let (a, b) = s.split_at(mid);

    a == b
}
