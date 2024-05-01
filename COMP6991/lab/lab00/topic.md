## COMP6991 Week 00 Weekly Exercises

### exercise: Our first rust program

If you're starting this activity, it is assumed that you have followed the [home computing ](https://cgi.cse.unsw.edu.au/~cs6991/24T1/resources/rust-toolchain)documentation to install the rust toolchain, and have (optionally) setup your editor to use rust-analyzer.

Now that you've installed a rust toolchain, it's time to write your first rust program!

Your task is to create a rust program that acts just like the following example.

```
6991 rustc blazingly_fast.rs
./blazingly_fast
Hello world!
I am a bit rusty with this new language!
This program is 🚀 blazingly fast 🚀
```

The book subchapter on `Hello, World!` may be useful.

The documentation for the `println!` macro may be useful.

### exercise: Some basic input

Your task is to write a program, `repeat.rs` that reads a single line of input and then prints the line back out.

For example,

```
cd repeat
6991 cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/repeat`
hello there
hello there
6991 cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/repeat`
echo!
echo!
6991 cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/repeat`
it seems that our program has stumbled across what appears to be a rather lengthy line
it seems that our program has stumbled across what appears to be a rather lengthy line
```

The documentation for the `print!` macro may be useful.

The documentation for the `read_line` function may be useful.

### exercise: FizzBuzz

You have been given a program, `fizzbuzz.rs`, that prints the numbers from 1 to 5.

Your task is to modify the program such that that prints all numbers from 1 to 100 inclusive, but for multiples of three prints `Fizz` instead of the number and for multiples of five prints `Buzz`. For numbers which are multiples of both three and five, the program should print `FizzBuzz`.

For example,

```
cd fizzbuzz
6991 cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/fizzbuzz`
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
<...>
97
98
Fizz
Buzz
```

You can calculate the remainder of a number in Rust using the modulo operator:

```
// The remainder of 5 when divided by 3
let remainder = 5 % 3;
```

If you're done these exercises, and want to keep reading (you are not required to!) then you should start with [The Rust Programming Language Book](https://doc.rust-lang.org/book/).

Note that the topic ordering in the book is different to the ordering of the topics in this course!