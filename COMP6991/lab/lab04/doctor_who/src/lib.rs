//! # My Caesar
//!
//! This crate provides functionality to encode and decode messages using the Caesar cipher,
//! which shifts each letter in the message by a specified number of places.

/// The default shift amount for the Caesar cipher.
pub const DEFAULT_SHIFT: i32 = 5;
/// ASCII value for uppercase 'A'.
const UPPERCASE_A: i32 = 65;
/// ASCII value for lowercase 'a'.
const LOWERCASE_A: i32 = 97;
/// The size of the alphabet used in the Caesar cipher.
const ALPHABET_SIZE: i32 = 26;

/// Shifts the characters in the given lines by a specified number of places in the alphabet,
/// effectively encoding or decoding a message using the Caesar cipher technique.
///
/// # Arguments
/// * `shift_by` - An `Option<i32>` specifying the number of places to shift each character.
///   If `None`, a default shift (usually 5) is applied.
/// * `lines` - A `Vec<String>` containing the strings to be shifted.
///
/// # Returns
/// A `Vec<String>` where each input string has been shifted accordingly.
///
/// # Examples
///
/// Here is an example where the number of positions to shift the string is set to `3`, which
/// can be any integer (`Some(<i32>)`).
/// ```rust
/// # use doctor_who::caesar_shift;
/// let shifted = caesar_shift(Some(3), vec!["COMP6991".to_string()]);
/// assert_eq!(shifted, vec!["FRPS6991".to_string()]);
/// ```
///
/// Here is an example where the number of positions to shift the string is not set, using
/// `DEFAULT_SHIFT`. The default value of `DEFAULT_SHIFT` is 5.
/// ```rust
/// # use doctor_who::caesar_shift;
/// let shifted = caesar_shift(None, vec!["COMP6991".to_string()]);
/// assert_eq!(shifted, vec!["HTRU6991".to_string()]);
/// ```
pub fn caesar_shift(shift_by: Option<i32>, lines: Vec<String>) -> Vec<String> {
    let shift_number = shift_by.unwrap_or(DEFAULT_SHIFT);

    lines
        .iter()
        .map(|line| shift(shift_number, line.to_string()))
        .collect()
}

fn shift(shift_by: i32, line: String) -> String {
    let mut result: Vec<char> = Vec::new();

    // turn shift_by into a positive number between 0 and 25
    let shift_by = shift_by % ALPHABET_SIZE + ALPHABET_SIZE;

    line.chars().for_each(|c| {
        let ascii = c as i32;

        if ('A'..='Z').contains(&c) {
            result.push(to_ascii(
                abs_modulo((ascii - UPPERCASE_A) + shift_by, ALPHABET_SIZE) + UPPERCASE_A,
            ));
        } else if ('a'..='z').contains(&c) {
            result.push(to_ascii(
                abs_modulo((ascii - LOWERCASE_A) + shift_by, ALPHABET_SIZE) + LOWERCASE_A,
            ));
        } else {
            result.push(c)
        }
    });

    result.iter().collect()
}

/// Computes the absolute value of a modulo b.
fn abs_modulo(a: i32, b: i32) -> i32 {
    (a % b).abs()
}

/// Converts an integer to a character, assuming the integer represents an ASCII value.
fn to_ascii(i: i32) -> char {
    char::from_u32(i as u32).unwrap()
}
