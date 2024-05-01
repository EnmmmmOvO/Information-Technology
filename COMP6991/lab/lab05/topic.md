## Week 05 Weekly Exercises

### exercise: Pointy

> #### Note
>
> **Objectives**
>
> - Understand how and why Rust uses generics
> - Write a generic DataType, Function, and understand the problems which they solve
> - Implement a method on a generic DataType
>
> Basically, get you to write some very basic generic code in Rust!

So far in our Rust journey, we've always had to write our types, functions, and methods for a specific type.

For example, we would write a struct that would store two i32�32 values, and then we would write a function that would take two i32�32 values and return an i32�32 value (maybe doing some sort of addition).

This is fine for simple programs, but what if we wanted to write a function that would take two f32f32 values, perform some operation, and then return an f32�32 value? We would have to write a new function for that. What if we wanted to write a function that would take two StringString values, perform the same operation, and then return a StringString value? We would have to write a new function for that, even though the only thing that changed were the types inputted and outputted to the function!

Suddenly, we have multiple functions that all do the same thing - resulting in a lot of duplicated code, more code to maintain, test and write! There are many ways we could make writing this code easier; we can use generics to solve this problem!

> #### Hint
>
> If you've never encountered "generic programming" or "generics" before, you may find the following resources useful:
>
> - [What is Generic Programming?](https://oswalt.dev/2020/08/what-is-generic-programming/)
> - [Rust Book - Generics](https://doc.rust-lang.org/book/ch10-01-syntax.html)

**In this exercise** you will be writing a generic function, a generic type, and a method on a generic type. You should complete the below tasks in `src/lib.rs`

- **First** - implement a generic function called `first` that takes a [slice](https://doc.rust-lang.org/book/ch04-03-slices.html) of some type T�, and returns a shared borrow of first value in the slice. Be sure to use the provided doctests to help you write your function.

- **Second** - modify the given `Point` struct to be generic. It should be able to store two values of one type `T`. Be sure to use the provided doctests to help you write your struct.

- **Third** - modify the existing method on the `Point` struct called `distance` that takes a second `Point` and returns the distance between the two points. Modify this method to be only be implemented for `Point` instances where the type of the `x` and `y` values are `f32`

- **Finally** - create a generic method on the `Point` struct called `new` that creates a new  `Point`. This method should take two values of type $T$  and return a new `Point` instance with the given values.

  Ideally, your method should return `Self`, and construct a `Self`.

> #### Hint
>
> The documentation for the `traits` chapter of the book may be useful.
>
> The documentation for the `generics` chapter of the book may be useful.
>
> The documentation for the `methods` chapter of the book may be useful.
>
> The documentation for the `slices` chapter of the book may be useful.
>
> The documentation for the `self` keyword may be useful.

When you think your program is working, you can use `autotest` to run some simple automated tests:

```
6991 autotest
```

When you are finished working on this exercise, you must submit your work by running `give`:

```
6991 give-crate
```

The due date for this exercise is **Week 7 Wednesday 21:00:00**.

Note that this is an individual exercise; the work you submit with `give` must be entirely your own.

### exercise: Dungeons and Dragons!

> #### Note
>
> **Objectives** Understanding, practice and reasoning about:
>
> - Traits
> - Trait bounds
>
> Additionally, exposure to the rustyline crate.
>
> This exercise should provide you with the when and why behind writing your first trait in Rust.
>
> It should be an opportunity for you to create, reason about and apply simple traits - useful for your assignment!

In this exercise, you will be harnessing the power of traits, in order to emulate a subset of a role playing game (RPG) inspired by dungeons and dragons - dice rolling!

The provided code will handle all of the input parsing using the awesome [rustyline](https://docs.rs/rustyline/latest/rustyline/) crate. You will be modifying the code in `die.rs`

> #### Warning
>
> If you have not watched the week 5 lectures, the following short talk should give enough context to start.
>
> It's also in theme!
>
> [Traits and You: A Deep Dive — Nell Shamrell-Harrington](https://www.youtube.com/watch?v=grU-4u0Okto)

In this exercise, you will need to complete the following tasks, by modifying the code in `die.rs` ONLY.

1. Create a Trait with a single function , that describes the behaviour of getting the value of a roll of a dice/coin.
2. Implement the trait for `Coin` (a coin "roll" will either be $1$ or $2$).
3. Implement the trait for `Dice` (each dice will be a number between 1 and the number of sides on the dice (inclusive) - a D4 for example, has 4 sides).
4. Add a generic trait bound for the roll function - such that your function accepts any type $T$ - where $T$ implements your trait!

> #### Note
>
> In order to pass the autotests, you **must** use the given `get_random_value` function to generate random values (why might this be?).
>
> You should not touch the code inside `main.rs`

```
6991 cargo run
  Finished dev [unoptimized + debuginfo] target(s) in 0.02s
    Running `target/debug/dungeons_and_dragons`
>> d20
You rolled a d20: 7
>> d2
You rolled a d2: 1
>> d10
You rolled a d10: 4
>> d8
You rolled a d8: 3
>> 
Goodbye!
```

When you think your program is working, you can use `autotest` to run some simple automated tests:

```
6991 autotest
```

When you are finished working on this exercise, you must submit your work by running `give`:

```
6991 give-crate
```

The due date for this exercise is **Week 7 Wednesday 21:00:00**.

Note that this is an individual exercise; the work you submit with `give` must be entirely your own.

### exercise: Languages!

> #### NOte
>
> **Objectives**
>
> - Trait objects
> - The From trait
> - Interaction with associate trait types `impl Add<Foo> for Bar`
>
> Understanding of the above is super useful for the assignment! For example, you might want something like `impl Add<Direction> for Player`

In this exercise, you will be finishing a quick implementation of a program that uses some basic operations using trait objects.

You've been given a starter crate languages, which consists of the `Greeting` trait, and three implementations of it for the `English`, `French` and `Spanish` structs.

Your task is to complete the following tasks in `main.rs` such that it compiles and prints some basic output.

1. **First**, implement the `From` trait, such that you can convert a `&str` into a `Box<dyn Greeting>`. You can assume that only valid strings will be given. In a real codebase, you would want to handle errors (maybe by using the `TryFrom` trait), but for this exercise, you can assume that the input is valid.
2. **Second**, finish the implementation of the `speak_all_greetings `function, such that it prints out the greetings.

> #### Hint
>
> The video linked in the exercise above should explain the concept of trait objects, alongside the week05 lectures.

```
    6991 cargo run
    Compiling languages v0.1.0
    Finished dev [unoptimized + debuginfo] target(s) in 0.21s
     Running `target/debug/languages`
John says:
Hello!
Hola!
Jane says:
Bonjour!
```

You may find the following videos useful, although some may go into advanced trait usages.[Jon Gjengset - Dispatch and Fat Pointers](https://youtu.be/xcygqF5LVmM)[Tim Clicks - Generics and trait objects explained](https://www.youtube.com/watch?v=ywskA8CoulM)

When you think your program is working, you can use `autotest` to run some simple automated tests:

```
6991 autotest
```

When you are finished working on this exercise, you must submit your work by running `give`:

```
6991 give-crate
```

The due date for this exercise is **Week 7 Wednesday 21:00:00**.

Note that this is an individual exercise; the work you submit with `give` must be entirely your own.

### (optional) challenge exercise: Mitochondria (Investigating the Cell smart pointer)

> #### Danger
>
> This exercise is optional, and will not be marked. This will allow you to focus on your assignment1!
>
> If you're getting here and have time, you can still complete it, and discuss your solutions on the forum/with your tutor.
>
> However, we would recommend you instead spend your time watching some of the linked videos to get a better understanding of trait objects, if you have the time.
>
> If you've finished this and still want something to procrastinate your assignment on - I'd love to see an investigation of the thiserror and anyhow crates for error handling as blog post :D

> #### Note
>
> In the field of biology, the mitochondria is often labelled as the "powerhouse of the cell", that is, it is the organelle that is responsible for how/why the Cell is able to work!
>
> This exercise name hence is `mitochondria`, as we investigate how rust's [std::cell::Cell](https://doc.rust-lang.org/stable/std/cell/struct.Cell.html) smart pointer (and it's close relatives) work, and what powers them!

This exercise is a theory exercise, aimed to explore the smart pointers `Cell` and `RefCell`. The exercise consists of 10 prompts/questions, in order for you to investigate `Cell`. Your task is to answer each question!

If you wish to discuss your solution/ask questions - do so on the course forum!

> #### Hint
>
> Most of the questions in this exercise can be answered by watching the first 20 or 30 minutes of this video:
>
> [Crust of Rust: Smart Pointers and Interior Mutability](https://youtu.be/8O0Nt9qY_vo?t=151)

