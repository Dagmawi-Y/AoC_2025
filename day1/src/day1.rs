use std::fs;

pub fn part1() {
    let input = fs::read_to_string("input.txt")
        .expect("failed to read input file");

    let mut pos: i32 = 50;
    let mut count_zero = 0;

    for line in input.lines() {
        if line.trim().is_empty() {
            continue;
        }

        let dir = line.chars().next().unwrap();

        let dist: i32 = line[1..].parse().expect("dist parse err");

        match dir {
            'L' => {
                pos = pos - dist;
            }
            'R' => {
                pos = pos + dist;
            }
            _ => panic!("invalid direction"),
        }

        // wrap for negatives
        pos = ((pos % 100) + 100) % 100;

        if pos == 0 {
            count_zero += 1;
        }
    }

    println!("result: {}", count_zero);
}

pub fn part2() {
    let input = fs::read_to_string("input.txt").expect("failed to read input file");
    let mut pos = 50;
    let mut count_zero = 0;

    for line in input.lines() {
        if line.trim().is_empty() { continue; }

        let dir = line.chars().next().unwrap();
        let dist: i32 = line[1..].parse().expect("dist parse err");

        for _ in 0..dist {
            if dir == 'R' {
                pos += 1;
            } else {
                pos -= 1;
            }

            if pos > 99 {
                pos = 0;
            } else if pos < 0 {
                pos = 99;
            }

            if pos == 0 {
                count_zero += 1;
            }
        }
    }

    println!("Part 2 result: {}", count_zero);
}