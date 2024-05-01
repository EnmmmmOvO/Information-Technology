### (optional) exercise: Q1

# Question 1

## Q1.1 (2 marks)

A C programmer who is starting to learn Rust has asked: "Aren't match statements just complicated if statements?". Give a specific example of a situation where you believe a match statement would significantly improve code quality, instead of a series of if/else statements.

## Q1.2 (2 marks)

The following Rust code fails to compile, but equivalent code in other popular programming languages (e.g. C, Java, Python) compiles and/or works correctly. Explain what issue(s) prevent the Rust compiler from building this code, and the philosophy behind this language decision.

```rust
struct Coordinate {
    x: i32,
    y: i32,
};

let coord1 = Coordinate {x: 1, y: 2};
let coord2 = coord1;
let coord_sum = Coordinate { x: coord1.x + coord2.x, y: coord1.y + coord2.y };
```

## Q1.3 (3 marks)

In other languages, the operation: `"first_string" + "second_string"` produces a new string, `"first_stringsecond_string"`. This particular operation **does not** work in Rust.

1. Why does Rust not implement this operation on the `&str` type?
2. Would it be possible for the Rust language developers to implement this? What rust feature would they use to implement it?
3. Do you think the Rust language developers should implement this operation? Give one reason to justify your answer.



## Q1.4 (3 marks)

Rust beginners have posted some questions on a programming forum:

1. How can I turn an owned value into a shared borrow?
2. How can I turn a shared borrow into an exclusive borrow!
3. Why am I allowed to turn an exclusive borrow into a shared borrow?

Provide a short answer to each question. Importantly, note that some questions might ask for something that is not possible (in which case, you should say so and explain why).

### (optional) exercise: Q2

In this activity, you will be building a small text searching system. It should search a large string for sentences that contain a particular search term. Another function will then look through all the search results to determine how often each sentence was found.

You have been given starter code which does not yet compile. Your task is to fill in both `todo!()` statements, as well as to add lifetimes where required in order to build your code.

You are not permitted to change the return type of functions, the names of structs, or the types of structs. You may also not change the main function, and you should expect that the main function could be changed during testing. You will, however, have to add lifetimes to existing types in order to successfully compile your code.

This is an example of the expected behaviour:

```sh
 6991 cargo run test_data/test_data.txt 
    Finished dev [unoptimized + debuginfo] target(s) in 0.36s
    Running `target/debug/prac_q2`
there
very
prove
the universe
  
Found 1 results for 'there'.
Found 9 results for 'very'.
Found 1 results for 'prove'.
Found 11 results for 'the universe'.
'8 billion years ago, space expanded very quickly (thus the name "Big Bang")' occured 1 times.
'According to the theory the universe began as a very hot, small, and dense superforce (the mix of the four fundamental forces), with no stars, atoms, form, or structure (called a "singularity")' occured 2 times.
'Amounts of very light elements, such as hydrogen, helium, and lithium seem to agree with the theory of the Big Bang' occured 1 times.
'As a whole, the universe is growing and the temperature is falling as time passes' occured 1 times.
'Because most things become colder as they expand, scientists assume that the universe was very small and very hot when it started' occured 2 times.
'By measuring the redshift, scientists proved that the universe is expanding, and they can work out how fast the object is moving away from the Earth' occured 2 times.
'Cosmology is the study of how the universe began and its development' occured 1 times.
'Other observations that support the Big Bang theory are the amounts of chemical elements in the universe' occured 1 times.
'The Big Bang is a scientific theory about how the universe started, and then made the stars and galaxies we see today' occured 1 times.
'The Big Bang is the name that scientists use for the most common theory of the universe, from the very early stages to the present day' occured 2 times.
'The more redshift there is, the faster the object is moving away' occured 1 times.
'The most commonly considered alternatives are called the Steady State theory and Plasma cosmology, according to both of which the universe has no beginning or end' occured 1 times.
'The most important is the redshift of very far away galaxies' occured 1 times.
'These electromagnetic waves are everywhere in the universe' occured 2 times.
'This radiation is now very weak and cold, but is thought to have been very strong and very hot a long time ago' occured 1 times.
'With very exact observation and measurements, scientists believe that the universe was a singularity approximately 13' occured 2 times.
```

### (optional) exercise: Q3

In this question, your task is to complete two functions, and make them generic: `zip_tuple` and `unzip_tuple`. Right now, the `zip_tuple` function takes a `Vec<Coordinate>` and returns a tuple: `(Vec<i32>, Vec<i32>)`. The `unzip_tuple` function performs the inverse of this.

This code currently does not compile, because `q3_lib` (i.e. `lib.rs`) does not know what the type of `Coordinate` is. Rather than telling the functions what type `Coordinate` is, in this exercise we will make the functions generic, such that it works for both `q3_a` (i.e. main_1.rs) and `q3_b` (i.e. main_2.rs). This is to say, `tuple_unzip` should work for any `Vec<T>` such that `T` implements `Into` into a 2-tuple of any 2 types, and `tuple_zip` should work for any `Vec<(T, U)>` such that `(T, U)` implements `Into` into any type.

Once you have modified your function signatures for `tuple_unzip` and `tuple_zip`, you should find that the only *concrete* type appearing within the signature is `Vec`. In other words, the functions should work for **any type** which can be created from a 2-tuple and which can be converted into a 2-tuple.

### (optional) exercise: Q4

## Q4.1 (2 marks)

Steve is writing some Rust code for a generic data structure, and creates a (simplified) overall design alike the following:

```rust
struct S {
    // some fields...
}

impl S {
    fn my_func<T>(value: T) {
        todo!()
    }
}
```

He soon finds that this design is not sufficient to model his data structure, and revises the design as such:

```rust
struct S<T> {
    // some fields...
}

impl<T> S<T> {
    fn my_func(value: T) {
        todo!()
    }
}
```

Give an example of a data-structure that Steve could be trying to implement, such that his first design would not be sufficient, and instead his second design would be required for a correct implementation. Furthermore, explain why this is the case.

## Q4.2 (3 marks)

Emily is designing a function that has different possibilities for the value it may return. She is currently deciding what kind of type she should use to represent this property of her function.

She has narrowed down three possible options:

1. An enum
2. A trait object
3. A generic type (as `fn foo(...) -> impl Trait`)

For each of her possible options, explain one possible advantage and one possible disadvantage of that particular choice.

## Q4.3 (5 marks)

Rust's macro system offers an extremely flexible method for code generation and transfiguring syntax, but this language feature comes with certain costs. Identify 3 downsides to the inclusion, design, or implementation of Rust's macro system.

(Note that your downsides may span any amount and combination of the categories above. e.g. you could write all 3 on just one category, or one on each, or anything in-between.)

### (optional) exercise: Q5

## Q5.1 (3 marks)

In many other popular programming languages, mutexes provide `lock()` and `unlock()` methods which generally do not return any value (i.e. `void`).

What issues could this cause?

How does Rust differently implement the interface of a `Mutex`, and what potential problems does that help solve?

## Q5.2 (2 marks)

In Rust, locking a `Mutex` returns a `Result`, instead of simply a `MutexGuard`. Explain what utility this provides, and why a programmer might find this important.

## Q5.3 (3 marks)

While reviewing someone's code, you find the following type: `Box<dyn Fn() -> i32 + Send>`.

Explain what the `+ Send` means in the code above?

Explain one reason you might need to mark a type as `Send`, and what restrictions apply when writing a closure that must be `Send`.

## Q5.4 (2 marks)

Your friend tells you they don't need the standard library's channels, since they've implemented their own alternative with the following code:

```rust
use std::collections::VecDeque;
use std::sync::Mutex;
use std::sync::Arc;
use std::thread;

#[derive(Clone, Debug)]
struct MyChannel<T> {
    internals: Arc<Mutex<VecDeque<T>>>
}

impl<T> MyChannel<T> {
    fn new() -> MyChannel<T> {
        MyChannel {
            internals: Arc::new(Mutex::new(VecDeque::new()))
        }
    }
    fn send(&mut self, value: T) {
        let mut internals = self.internals.lock().unwrap();
        internals.push_front(value);
    }

    fn try_recv(&mut self) -> Option<T> {
        let mut internals = self.internals.lock().unwrap();
        internals.pop_back()
    }
}

fn main() {
    let mut sender = MyChannel::<i32>::new();
    let mut receiver = sender.clone();
    sender.send(5);
    thread::spawn(move || {
        println!("{:?}", receiver.try_recv())
    }).join().unwrap();
}
```

Identify a use-case where this implementation would not be sufficient, but the standard library's channel would be.

Furthermore, explain why this is the case.

### (optional) exercise: Q6

The "[Read Copy Update](https://en.wikipedia.org/wiki/Read-copy-update)" pattern is a common way of working with data when many sources need to be able to access data, but also to update it. It allows a user to access a value whenever it's needed, achieving this by never guaranteeing that the data is always the latest copy. In other words, there will always be something, but it might be slightly old. In some cases, this trade-off is one that's worth making.

In this task, you will be implementing a small RCU data-structure. You should ensure that:

- Multiple threads are able to access a given piece of data.
- Threads can pass a closure to the type which updates the data.
- When created, the RCU type starts at generation 0. Every time it is updated, that counter is increased by one.

You have been given some starter code for the type `RcuType<T>`, including some suggested fields, and the required interface. Ensure you first understand the requirements of this task, and then implement the methods described in the starter code.

### (optional) exercise: Q7

## Q7.1 (5 marks)

Gavin writes a blog post critical of Rust, especially with respect to `unsafe`. In his blog post, he claims that it's not possible to have any confidence in the overall safety of a Rust program since "even if you only write safe Rust, most standard functions you call will have unsafe code inside them".

1. State to what extent you agree with Gavin's claim.
2. Give at least three arguments that support your conclusion.

## Q7.2 (5 marks)

Hannah writes a Rust program that intends to call some C code directly through FFI. Her C function has the following prototype:

```rust
int array_sum(int *array, int array_size);
```

and the following implementation:

```rust
int array_sum(int *array, int array_size) {
	int sum = 0;
	for (int i = 0; i < array_size; i++) { sum += array[i]; }
	return sum;
}
```

Note that you can assume that this C code is written entirely correctly, and the below `extern "C"` block is an accurate translation of the C interface.

Her Rust code is currently written as follows:

```rust
use std::ffi::c_int;

#[link(name = "c_array")]
extern "C" {
    fn array_sum(array: *mut c_int, array_size: c_int) -> c_int;
}

fn test_data() -> (*mut c_int, c_int) {
    let size = 10;
    let array = vec![6991; size].as_mut_ptr();
    (array, size as c_int)
}

fn main() {
    let sum = {
        let (array, size) = test_data();

        // Debug print:
        let message = format!("Calling C function with array of size: {size}");
        println!("{message}");

        unsafe { array_sum(array, size) }
    };

    println!("C says the sum was: {sum}");
}
```

She expects that if she runs her code, it should print that the C code summed to `69910`. To her surprise, she runs the program and finds the following:

```sh
6991 cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/ffi`
Calling C function with array of size: 10
C says the sum was: -2039199222
```

Hannah correctly concludes that there must be a problem with her Rust code.

1. Identify the issue that is causing the program to misbehave.
2. Describe a practical solution Hannah could use to fix the bug.
3. Explain why Rust wasn't able to catch this issue at compile-time.

### (optional) exercise: Q8

The final question of the exam will be a more open-ended question which will ask you to perform some analysis or make an argument. Your argument will be judged alike an essay (are your claims substantiated by compelling arguments). Remember that you **will not** get any marks for blindly supporting Rust.

A friend of yours has just read [this article](https://matklad.github.io/2020/09/20/why-not-rust.html), and thinks that it means they shouldn't learn Rust.

Read through the article, and **discuss** the following prompt:

##### Rust is not worth learning, as explained by this article.

The overall structure of your answer is **not** marked. For example, your answer may include small paragraphs of prose accompanied by dot-points, or could instead be posed as a verbal discussion with your friend. Regardless of the structure / formatting you choose, the **substance** of what you write is the most important factor, and is what will determine your overall mark for this question.

From [UNSW's Glossary of Task Words](https://www.student.unsw.edu.au/glossary-task-words):

| **Discuss** | Investigate or examine by argument. Examine key points and possible interpretations, sift and debate, giving reasons for and against. Draw a conclusion. |
| ----------- | ------------------------------------------------------------ |
|             |                                                              |