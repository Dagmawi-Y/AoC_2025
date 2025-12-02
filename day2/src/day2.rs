use std::fs;

pub fn part1() {
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

    println!("Day 2 - Part 1 result: {}", sum);
}

pub fn part2() {
    let input = fs::read_to_string("input.txt").expect("failed to read input");

    let mut sum: u64 = 0;

    for range in input.trim().split(',') {
        let (start_s, end_s) = range.split_once('-').unwrap();
        let start: u64 = start_s.parse().unwrap();
        let end: u64 = end_s.parse().unwrap();

        for id in start..=end {
            if is_repeated_pattern(id) {
                sum += id;
            }
        }
    }

    println!("Day 2 - Part 2 result: {}", sum);
}

fn is_double_pattern(n: u64) -> bool {
    let s = n.to_string();
    let len = s.len();

    if len % 2 != 0 {
        return false;
    }

    let mid = len / 2;
    let (a, b) = s.split_at(mid);

    a == b
}

fn is_repeated_pattern(n: u64) -> bool {
    let s = n.to_string();
    let len = s.len();

    for block_size in 1..=len / 2 {
        if len % block_size != 0 {
            continue;
        }

        let block = &s[..block_size];

        if s.chars()
            .collect::<Vec<_>>()
            .chunks(block_size)
            .all(|chunk| chunk.iter().collect::<String>() == block)
        {
            return true;
        }
    }

    false
}
