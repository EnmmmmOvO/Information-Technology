use std::num::ParseIntError;

use my_new_lib_crate::utils::first_argument;
use my_new_lib_crate::errors::TribonacciError;
use my_new_lib_crate::constants::ERROR_MESSAGE;

fn main() {
    let shift_size = first_argument();

    if let Err(e) = compute_tribonacci(shift_size) {
        println!("Error: {}", e.0)
    }
}

/// Computes the tribonacci sequence of a given size
/// Prints the sequence, and its sum
fn compute_tribonacci(size: Result<usize, ParseIntError>) -> Result<(), TribonacciError> {

    let mut tribonacci = vec![1_u128; 3];
    let size = size.map_err(|_| TribonacciError(ERROR_MESSAGE.to_string()))?;

    for i in 3..size {
        tribonacci.push(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3]);
    }

    println!("Values: {:?}", tribonacci);

    let value: u128 = tribonacci.into_iter().sum();
    println!("\nSum: {}", value);

    Ok(())
}
