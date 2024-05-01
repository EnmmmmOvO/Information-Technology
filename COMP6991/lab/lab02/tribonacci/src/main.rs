use std::env;
use std::num::ParseIntError;

struct TribonacciError(String);

fn main() {
    let args: Vec<String> = env::args().collect();
    let error_message = String::from("Please enter a valid size");

    let size = match args.get(1) {
        Some(s) => s.parse::<usize>(),
        None => Ok(10),
    };

    if let Err(e) = compute_tribonacci(size, error_message) {
        println!("Error: {}", e.0)
    }
}

/// Computes the tribonacci sequence of a given size
/// Prints the sequence, and its sum
fn compute_tribonacci(
    size: Result<usize, ParseIntError>,
    // The error message your function should return
    // inside the `TribonacciError` struct
    error_msg: String,
) -> Result<(), TribonacciError> {
    if let Err(_) = size {
        return Err(TribonacciError(error_msg));
    }

    match size.unwrap() {
        0..=2 | 146.. => return Err(TribonacciError(error_msg)),
        3 => println!("Values: [1, 1, 1]\n\nSum: 3"),
        s => {
            let mut sum: i128 = 3;
            let mut temp: [i128; 3] = [1, 1, 1];
            let mut record = 0;
            print!("Values: [1, 1, 1, ");
            for i in 3..s {
                temp[record] = temp.iter().sum();
                print!("{}", temp[record]);
                if i < s - 1 {
                    print!(", ");
                }

                sum = sum + temp[record];
                record = (record + 1) % 3;
            }
            print!("]\n\nSum: {sum}\n");
        }
    }


    Ok(())
}
