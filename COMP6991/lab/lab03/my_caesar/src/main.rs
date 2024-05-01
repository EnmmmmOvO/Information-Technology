use std::io::{stdin, BufRead};
use std::env;

const DEFAULT_SHIFT: i32 = 5;

fn main() {
    let shift_by: i32 = env::args()
        .nth(1)
        .and_then(|arg| arg.parse().ok())
        .unwrap_or(DEFAULT_SHIFT);

    for line in stdin().lock().lines() {
        let shifted = shift(shift_by, &line.expect("no input line"));

        println!("Shifted ascii by {shift_by} is: {shifted}");
    }
}


fn shift(shift: i32, line: &str) -> String {
    let mut result = String::new();
    line.chars().for_each(|c| result.push(decode(shift, c)));
    result
}

fn decode(shift: i32, c: char) -> char {
    match c as u32 {
        65..=90 => char::from_u32((65 + (((c as i32) - 65 + shift) % 26 + 26) % 26) as u32).unwrap(),
        97..=122 => char::from_u32((97 + (((c as i32) - 97 + shift) % 26 + 26) % 26) as u32).unwrap(),
        _ => c
    }
}