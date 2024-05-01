#![allow(unused)]

use require_lifetimes::require_lifetimes;

/// This function prints the given input.
/// You will need to annotate its lifetimes.
/// (2 marks)
#[require_lifetimes]
pub fn print<'a>(a: &'a i32) {
    println!("{a}");
}

/// This function returns the first parameter it is given.
/// You will need to annotate its lifetimes.
/// (3 marks)
#[require_lifetimes]
pub fn first<'a, 'b>(a: &'a i32, b: &'b i32) -> &'a i32 {
    a
}

/// A struct to hold the data of a string being split.
/// You will need to annotate its lifetimes.
/// (2 marks)
pub struct StringSplitter<'a, 'b> {
    pub text: &'a str,
    pub pattern: &'b str,
}

/// This function creates a string splitter with given data.
/// You will need to annotate its lifetimes.
/// (3 marks)
#[require_lifetimes]
pub fn split<'a, 'b>(text: &'a str, pattern: &'b str) -> StringSplitter<'a, 'b> {
    StringSplitter {
        text,
        pattern,
    }
}
