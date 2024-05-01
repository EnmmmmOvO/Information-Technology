## Week 02 Weekly Exercises

### exercise: Tribonacci

> #### Note
>
> Note, that in the wikipedia link the numbers start with 0, 0, 1. In this exercise we'll be starting with 1, 1, 1.
>
> See hint 2 for more.

In this task, you will write a function that computes a variable number of [Tribonacci numbers ](https://en.wikipedia.org/wiki/Tribonacci_number), and also their sum.

Your program should read a single **positive** integer, `n`, from the command-line arguments, and subsequently compute the first `n` Tribonacci numbers, along with their sum.

If no command-line arguments are given, assume the value of `n` is assumed to be **10**.

Invalid input (i.e. negative enumbers, or non-valid numbers) should be handled by returning a custom error message `"Please enter a valid size!"` (this is in the `error_msg` parameter of the `compute_tribonacci` function), through the `struct TribonacciError`, and then subsequently exiting the program.

> #### Hint
>
> - The [? operator ](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#a-shortcut-for-propagating-errors-the--operator)can be used to handle errors, and exit the program if an error occurs.
>
> - Try (😉) using it to handle the error case of invalid input.
>
> - The `map_err` method can be used to convert the error type of a `Result` type to a custom error type.
>
>   For example
>
>   ```rust
>   let size: Result<i32, ParseIntError> = "42".parse(); ``let result: Result<i32, MyCustomError> = size.map_err(|_| MyCustomError);
>   ```
>
>   If we then add a `?` operator to the end of the `map_err` above, the program will exit if the `result` is an error.

Your program need only be able to calculate from `n = 3` to `n = 145` inclusive. We will not use positive integers outside of this range. Note that `n = 145` produces very large numbers that increase far past the width of a `i64` type. You may want to (strongly) consider using one of `i128` or `u128` instead, both of which can fit the largest number in that sequence.

You need only change the `compute_tribonacci` function.

```
6991 cargo run -- 4
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/tribonacci 4`
Values: [1, 1, 1, 3]

Sum: 6
6991 cargo run -- 10
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/tribonacci 10`
Values: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

Sum: 230
6991 cargo run -- -1
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/tribonacci -1`
Error: Please enter a valid size
```

[Click to reveal further hint](https://cgi.cse.unsw.edu.au/~cs6991/24T1/lab/02/questions#tribonacci_hint1)

> #### Hint
>
> - You can approach this by storing all intermediate values into a vector, where all values should be of type `i128` or `u128`. The vector's initial values should be `[1, 1, 1]`.
>
>   i.e. z
>
>   ```rust
>   let mut values: Vec<u128> = vec![1, 1, 1]
>   ```
>
> - You may find the below documentation, especially the examples, particularly helpful:
>
> - The documentation for the `args` function may be useful.
>
> - The documentation for the `vec` type may be useful.
>
> - The documentation for the `result` type may be useful.
>
> - The documentation for the `parse` method may be useful.
>
> - The documentation for the `map` method may be useful.
>
> - The documentation for the `map_err` method may be useful.
>
> - The documentation for the `sum` method may be useful.



When you think your program is working, you can use `autotest` to run some simple automated tests:

```
6991 autotest
```

When you are finished working on this exercise, you must submit your work by running `give`:

```
6991 give-crate
```

The due date for this exercise is **Week 3 Wednesday 21:00:00**.

Note that this is an individual exercise; the work you submit with `give` must be entirely your own.

### exercise: To Upper (Investigating strings!)

This activity is an investigation of Rust's strings!

You have been provided a simple crate, to_upper, which does not compile! Your task is to modify `to_upper/src/main.rs` so that it takes in a single command-line argument and converts the appropriate characters to uppercase. It may help to [RTFC](https://twitter.com/ekuber/status/1229609001660252160)!

> #### Note
>
> This exercise is based on [fasterthanlime](https://fasterthanli.me/)'s excellent article: [Working with Strings in Rust](https://fasterthanli.me/articles/working-with-strings-in-rust), which we certainly recommend reading.
>
> Although quite long, reading it will leave you with a much deeper understanding of Rust's string types, their interactions with UTF-8, and how and why they actually work!

You will always be given valid input (e.g. no empty arguments).

```
6991 cargo run -- 'hello world!!!'
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/to_upper 'hello world'\!''\!''\!''`
arg = hello world!!!
upp = HELLO WORLD!!!
6991 cargo run -- "uwu🥺👉👈"
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/to_upper 'uwu🥺👉👈'`
arg = uwu🥺👉👈
upp = UWU🥺👉👈
```

When you think your program is working, you can use `autotest` to run some simple automated tests:

```
6991 autotest
```

When you are finished working on this exercise, you must submit your work by running `give`:

```
6991 give-crate
```

The due date for this exercise is **Week 3 Wednesday 21:00:00**.

Note that this is an individual exercise; the work you submit with `give` must be entirely your own.

### exercise: Collections

Rust's collection types could be generally categorised into four groups:

- Sequences
  - `Vec`
  - `VecDeque`
  - `LinkedList`
- Maps
  - `HashMap`
  - `BTreeMap`
- Sets
  - `HashSet`
  - `BTreeSet`
- Misc.
  - `BinaryHeap`

In this activity, we'll be exploring the performance of first three (`Vec`, `VecDeque`, and `LinkedList`), and `HashMap` collections.

For each of the four collections above, your code should:

- Create a new instance of the collection.
- Add some `MAX_ITER` elements to it.
- Remove `MAX_ITER` elements from it.
- Time each of the above operations.

> #### Note
>
> For `LinkedList` insertion, you should insert at the end of the list. You should remove from the start of the list.
>
> For `HashMap` you only need to insert at key `i` where `i` is the current iteration. Similarly, you should remove from key `i`.

Before you start, please write down some of your expectations about what you think will be the most performant collection for these operations.

The analysis of `Vec` and `VecDeque` has already been completed for you in the provided code.

**This exercise also contains a theory section.** At the end of your main function, you should write a comment that answers the following questions:

- Which collection type was the fastest for adding and removing elements?
  - Why do you think this was the case?
- Is there any significant difference between `Vec` and `VecDeque` deletion?
  - If so, why? If not, why not?
- When would you consider using `VecDeque` over `Vec`?
- When would you consider using `LinkedList` over `Vec`?
- Did the results suprise you? Why or why not?.

The above will be manually marked. There will be an opportunity to discuss this with a tutor and get marked during your week 4 workshop. If you cannot attend, your work will instead be manually marked (offline) during week 5.

> #### Hint
>
> - The docs are extremely helpful here! Reading (not just copying) the std::collections module docs will help greatly with **understanding** of this exercise.
> - The documentation for the `std::collections` module may be useful.
> - The documentation for the `std::collections::VecDeque::remove` method may be useful.

When you are finished working on this exercise, you must submit your work by running `give`:

```
6991 give-crate
```

The due date for this exercise is **Week 3 Wednesday 21:00:00**.

Note that this is an individual exercise; the work you submit with `give` must be entirely your own.

### exercise: Data analysis

In this exercise, you are taking on the role of a prospective data analyst and have gotten your hands on a dataset of (**fictional!**) CSE enrolments.

The dataset is in the file `enrolments.psv` and each row contains the following columns (in order):

- UNSW Course Code
- UNSW Student Number
- Name
- UNSW Program
- UNSW Plan
- WAM
- UNSW Session
- Birthdate
- Sex

Each row of data represents one enrolment. One student may have multiple rows, as they may be enrolled in multiple courses.

You've been asked to process the data, and output answers to the following questions:

1. How many unique students are there?
2. What is the most common course (with how many students)?
3. What is the least common course (with how many students)?
4. What is the average WAM of all students in the file(to 2 decimal places)?

Note that you can assume that there will be no two equally most-common or equally least-common courses in the dataset -- i.e. there will always be exactly one answer.

You can also assume there will always be a term provided, but think about how you would model it if not!

> #### Warning
>
> The contents of the `enrollments.psv` used for your program will change in marking

```
 6991 cargo run 
    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/data_analysis`
Number of students: 8065
Most common course: COMP1511 with 953 students
Least common course: BIOM9002 with 1 students
Average WAM: 61.94
```

> #### Note
>
> This exercise may take a while to complete. If you get stuck, ask on the course forum!
>
> But, this exercise was designed to mimic a real-world data analysis task.
>
> Attempting the task will enable you to try:
>
> - How to read and process data from a file,
> - How to use serde, a library for serializing and deserializing data,
> - How to use HashMaps to count things,
> - How to use iterators to perform aggregations, filtering and transformations,
>
> But more importantly, it's one of the first larger exercises that you'll complete in Rust, and gives you a good taste for the scope of tasks that you can accomplish with only two weeks of Rust experience.
>
> There's no starter code for this, that is intentional! You have full control over how you want to structure, and design your program.
>
> If you get stuck, please ask and discuss with your peers/staff on the course forum - we are happy for collaboration on weekly exercises!!
>
> This is quite a lot for one exercise - but just do your best! You'll get there!

> #### Hint
>
> - This is a substantial exercise, break it down into steps! Try and avoid for-loops, and practice using iterator functions.
>
> - It is expected that you use serde for this exercise to deserialize into structs.
>   The documentation for the `serde` crate may be useful.
>
> - Remember, when you are iterating over something (e.g `x`) that `x.into_iter()` can sometimes **move** `x` (or in other words, "consume" `x` such that it cannot be used again later). You may need to either clone the data, or preferably use `x.iter()` instead. If you get stuck, ask on the course forum!
>
> - The documentation for the `csv` crate may be useful.
> - Particularly, the [`ReaderBuilder`](https://docs.rs/csv/latest/csv/struct.ReaderBuilder.html) struct, which will allow you to:
>   - Specify the delimiter (pipe symbol),
>   - Specify the headers (or alternatively that there are no headers),
>   - Specify the path of the file.
> - You may also find the following posts useful for reading PSV files into structs:
>   - [This Stack Overflow post](https://stackoverflow.com/a/71624183),
>   - [Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/encoding/csv.html).
> - The [`seek` method](https://docs.rs/csv/latest/csv/struct.Reader.html#method.seek) may be useful to reset the reader to the start.
> - You will need to enable the derive feature for the serde crate in your Cargo.toml such that your dependency looks like:
>   `serde = { version = "1.0", features = ["derive"] }`
>   This will allow you to use a derive macro for the `csv` crate to automatically generate the code to deserialize the CSV file into a struct.
> - The documentation for the `HashMap` type may be useful.
> - The documentation for the `entry` method may be useful. The example is of particular note.
> - The documentation for the `max_by_key` method may be useful. Similarly, min_by_key is also useful.
> - The documentation for the `sum` method may be useful. This is useful for calculating the average.

When you think your program is working, you can use `autotest` to run some simple automated tests:

```
6991 autotest
```

When you are finished working on this exercise, you must submit your work by running `give`:

```
6991 give-crate
```

The due date for this exercise is **Week 3 Wednesday 21:00:00**.

Note that this is an individual exercise; the work you submit with `give` must be entirely your own.