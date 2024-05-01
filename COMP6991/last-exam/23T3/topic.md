### (optional) exercise: 23T3 Q1: Theory (10 marks)

## Q1.1 (3 marks)

This question will ask you to comment on the following Rust snippet, which compiles correctly.

**Question:**

```rust
fn main() {
	let name = Some("Tom".to_string());

	print_name(name);
}

fn print_name(name: Option<String>) {
	match name {
		Some(n) => println!("Name is {}", n),
		None => println!("No name"),
	}
}
```

1. On the first line of the main function, we call the `to_string` method. Explain what this function does. *(1 mark)*
2. On the first line of the main function, we use the expression `Some(...)`. Explain the purpose of this code. *(1 mark)*
3. On the second line of the print_name function, we write `Some(n)`. Explain what this does in the context of a match block. *(1 mark)*

------

Write your answer in `exam_q1/q1_1.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q1_1 q1_1.txt
```

## Q1.2 (3 marks)

Julian has just learned how to use command line arguments in Rust. The `std::env::args().nth(1)` expression returns an `Option` containing the first command line argument (or `None` if there isn't an argument).

This code is his first attempt at using this function.

**Question:**

```rust
fn main() {
	let Some(name) = std::env::args().nth(1);

	println!("First argument was: {}", name);
}
```

**Question:**

1. Explain in principle (i.e. from a high level) why this code does not work. *(2 marks)*
2. Rewrite Julian's code to use a `let ... else` or `match` expression to assign the variable `name` to the command line argument if present or an empty string otherwise. Do not modify the `println!` code. *(1 mark)*

------

Write your answer in `exam_q1/q1_2.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q1_2 q1_2.txt
```

## Q1.3 (4 marks)

Your friend Imran sends you the following message:

Honestly Rust is so annoying. C and C++ let me just pass pointers or references around without having to worry about this `&mut` and `&` stuff, and none of those confusing lifetime annotations. My code would compile and work just fine in any other language!

**Question:**

Discuss Rust's ownership and borrowing model with reference to Imran's comment.

In your response, highlight two advantages *(2 marks)* and two disadvantages *(2 marks)* of the ownership and borrowing model.

------

Write your answer in `exam_q1/q1_3.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q1_3 q1_3.txt
```

### (optional) exercise: 23T3 Q2: Practical (10 marks)

In this question, we have written 3 functions which are implemented correctly. These functions are missing lifetime annotations. Your task is to add the correct lifetime annoations to these functions.

```rust
use require_lifetimes::require_lifetimes;
/// This function returns the input it is given.
/// You will need to annotate its lifetimes
/// (2 marks)
#[require_lifetimes]
pub fn identity(a: &i32) -> &i32 {
    a
}

/// This function swaps the two references it is given.
/// You will need to annotate its lifetimes
/// (4 marks)
#[require_lifetimes]
pub fn swap(a: &i32, b: &i32) -> (&i32, &i32) {
    (b, a)
}

//// This function returns the two references it is given in sorted order,
//// with the smallest one first.
//// (4 marks)
#[require_lifetimes]
pub fn sort_references(a: &i32, b: &i32) -> (&i32, &i32) {
    if *a > *b {
        (b, a)
    } else {
        (a, b)
    }
}
```

The code will run some assertions to check correctness, so the expected behaviour is empty output:

```sh
6991 cargo run --bin exam_q2
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q2`
6991 cargo run --bin exam_q2_alt
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q2_alt`
```

------

Write your answer in `exam_q2/src/lib.rs`.

When you think your program is working, you can use `autotest` to run some simple automated tests:

```
6991 autotest
```

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q2 lib.rs
```

### (optional) exercise: 23T3 Q3: Theory (10 marks)

## Q3.1 (5 marks)

The following code reads all digit characters from a given file and parses it into a single `i32`. For example, given a file with the contents `1, 2, 3-4-5, once I caught a fish alive!` it would output the single number `12345`.

```rust
use std::{error::Error, fs::File, path::Path, io::Read};

fn read_num_from_file(file_path: &Path) -> Result<i32, Box<dyn Error>> {
    let mut file = File::open(file_path)?;

    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    contents.retain(|ch| ('0'..='9').contains(&ch));
    let num = contents.parse()?;

    Ok(num)
}
```

This code in particular makes use of `Box<dyn Error>` and the `?` (`Try`) operator.

**Question:**

1. Explain what `Box<dyn Error>` represents. *(1 mark)*
2. Explain how the `?` (`Try`) operator works, with reference to the example code. *(1 mark)*
3. Discuss how this function's approach differs from using a concrete error `enum`, for both the function's author and its users. Provide a judgement. *(3 marks)*

------

Write your answer in `exam_q3/q3_1.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q3_1 q3_1.txt
```

## Q3.2 (2 marks)

Hannah is trying to design a function that sums up a sequence of `i32`s. She starts with the first design...

```rust
fn sum_sequence(sequence: &[i32]) -> i32 {
    let mut sum = 0;
    for num in sequence {
        sum += num;
    }
    sum
}
```

... and submits this for code review. Another software engineer on her team suggests the following change...

```rust
fn sum_sequence(sequence: impl Iterator<Item = i32>) -> i32 {
    let mut sum = 0;
    for num in sequence {
        sum += num;
    }
    sum
}
```

... which Hannah accepts and resubmits. Finally, a senior engineer suggests a further change:

```rust
fn sum_sequence(sequence: impl IntoIterator<Item = i32>) -> i32 {
    let mut sum = 0;
    for num in sequence {
        sum += num;
    }
    sum
}
```

**Question:**

1. Why is the first suggested change an improvement on Hannah's original design? *(1 mark)*
2. Why is the second suggested change an improvement on the second design? *(1 mark)*

------

Write your answer in `exam_q3/q3_2.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q3_2 q3_2.txt
```

## Q3.3 (3 marks)

Olivia is trying to create a `collect_sorted_vec` helper function that permits the shorthand of collecting an `Iterator` into a `Vec`, and then sorting that resulting `Vec`.

In short, she is trying to create a function working in the following way:

```rust
fn main() {
    let vec = [3, 1, 2].into_iter()
        .map(|x| x * 2)
        .collect_sorted_vec();

    assert_eq!(vec, vec![2, 4, 6]);
}
```

She elects to achieve this through an extension trait that should be implemented on all candidate iterators. She defines the trait as follows:

```rust
trait CollectSortedVec<T> {
    fn collect_sorted_vec(self) -> Vec<T>;
}
```

**Question:**

Write the code to implement this trait for all candidate `Iterators`. A candidate `Iterator` is any `Iterator` whose `Item` implements `Ord`. *(3 marks)*

------

Write your answer in `exam_q3/q3_3.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q3_3 q3_3.txt
```

### (optional) exercise: 23T3 Q4: Theory (10 marks)

## Q4.1 (3 marks)

While wandering the halls of UNSW's K17 building, you overhear some young and excited undergraduates discussing their favourite programming languages.

"Rust has solved concurrency! I haven't run into a single concurrent issue since I started with it!"

**Question:**

1. Explain how Rust's aliased XOR mutable borrowing model helps to prevent programming concurrency issues. *(2 marks)*
2. Does Rust prevent all concurrency issues? If so, explain how. If not, provide and explain a counter-example. *(1 mark)*

------

Write your answer in `exam_q4/q4_1.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q4_1 q4_1.txt
```

## Q4.2 (3 marks)

Lachlan is attempting to use `channel`s in a concurrent context. He writes some short example code that spawns a thread using `thread::scope`, and communicates between the main thread and spawned thread through a `channel`.

```rust
use std::{sync::mpsc::channel, thread};

fn main() {
    let (send, recv) = channel();

    thread::scope(|scope| {
        scope.spawn(move || {
            let item = recv.recv().unwrap();

            println!("Received {item} on thread!");
        });
    });

    send.send("hello").unwrap();
}
```

He expects that when run, the thread should print `"Received hello on thread!"`, but instead the program simply hangs endlessly, and has to be terminated manually with `^C`:

```sh
6991 cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/channel_test`
[...]
^C
```

**Question:**

1. Explain in detail why the program hangs forever. *(2 marks)*
2. Suggest a fix for this issue. *(1 mark)*

------

Write your answer in `exam_q4/q4_2.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q4_2 q4_2.txt
```

## Q4.3 (4 marks)

Annie often writes concurrent code making use of `Arc<Mutex<...>>`s. She values this particular abstraction, but dislikes the syntactic overhead of writing code this way.

In particular, she dislikes writing `Arc::new(Mutex::new(...))`, and having to use a new scope along with cloning her required `Arc`s each time she needs to spawn a thread. Her current sample code looks like the following:

```rust
use std::{thread, sync::{Arc, Mutex}};

fn main() {
    let a = Arc::new(Mutex::new(42));
    let b = Arc::new(Mutex::new("hello"));
    let c = Arc::new(Mutex::new(3.14));
    
    {
        let a = a.clone();
        let b = b.clone();

        thread::spawn(move || {
            println!("{} {}", a.lock().unwrap(), b.lock().unwrap());
        }).join().unwrap();
    }
    
    {
        let b = b.clone();
        let c = c.clone();

        thread::spawn(move || {
            println!("{} {}", b.lock().unwrap(), c.lock().unwrap());
        }).join().unwrap();
    }
}
```

She would like to make use of two macros, `arc_mutex!` and `use_arc_mutex!` in order to cut out some of the boilerplate. Her resulting equivalent code should be written as the following:

```
use std::{thread, sync::{Arc, Mutex}};

fn main() {
    arc_mutex!(
        a = 42;
        b = "hello";
        c = 3.14;
    );

    use_arc_mutex!(
        a;
        b;
        {
            thread::spawn(move || {
                println!("{} {}", a.lock().unwrap(), b.lock().unwrap());
            }).join().unwrap();
        }
    );

    use_arc_mutex!(
        b;
        c;
        {
            thread::spawn(move || {
                println!("{} {}", b.lock().unwrap(), c.lock().unwrap());
            }).join().unwrap();
        }
    );
}
```

When the macros are expanded, they should produce the original sample code.

Note that `arc_mutex!` should work for any number of declared variables, and `use_arc_mutex!` should work for any number of cloned `Arc`s.

Your task is to implement these two macros for Annie.

**Question:**

1. Implement the `arc_mutex!` macro. Provide the full `macro_rules!` declaration. *(2 marks)*
2. Implement the `use_arc_mutex!` macro. Provide the full `macro_rules!` declaration. *(2 marks)*

------

Write your answer in `exam_q4/q4_3.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q4_3 q4_3.txt
```

### (optional) exercise: 23T3 Q5: Practical (10 marks)

In this question, you will implement a generic "group-add" function.

Group-add is a fictional operation that takes a sequence of elements, and a grouping function which classifies each element into some particular group. It then produces a `HashMap` of groups to items, where items of the same group are summed up.

For example, the sequence `[1, 2, 3, 4, 5, 6, 7]` with the grouping function `|x| x % 3` should produce a `HashMap` with the key-value pairs:

```
0 => 9,
1 => 12,
2 => 7,
```

because the sequence is grouped into `[1, 2, 0, 1, 2, 0, 1]` based on their remainders. Note that it is the **items** that are then summed up:

```
0 => 3 + 6,
1 => 1 + 4 + 7,
2 => 2 + 5,
```

You have been given the following starter code in `src/lib.rs`:

```rust
use std::collections::HashMap;

pub fn group_add_items(items: Vec<i32>, grouper: fn(&i32) -> i32) -> HashMap<i32, i32> {
    let mut groupings = HashMap::new();

    for item in items {
        let group = grouper(&item);
        let current_group = groupings.entry(group)
            .or_default();
        *current_group += item;
    }

    groupings
}
```

This code correctly implements `group_add_items` for `Vec` collections of `i32`s, and a grouper using a function pointer from `i32` borrows to `i32`s.

Your task is to make this function far more generic.

Instead of the item list being concretely a `Vec` of `i32`s, it should be a generic sequence of any applicable type.

You must modify the type of the `grouper` from a function pointer of `&i32 -> i32` into a closure of `&Item -> Group` for any possible types `Item` and `Group`. As part of this, you must also decide which type of closure is the most generic choice out of `FnOnce`, `FnMut` and `Fn`.

The returned types within the `HashMap` should similarly be modified to suit.

You will be required to constrain some generic type parameters as you solve the exercise. You must ensure that you do not overly constrain the types, only requiring what is minimally needed.

You must not modify the body of the `group_add_items` function at all.

That is, the actual running code is already entirely correct. You must **only** modify the signature of the function (optionally adding a `where` section) to make this function more generic.

You are also permitted to import standard library types.

The code already runs correctly on the basic test case outlined above:

```sh
6991 cargo run --bin exam_q5
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q5`
```

However does not yet typecheck on the other test cases provided. Once you have modified the types to make the function as generic as possible, you should find these other test cases now compile and run:

```sh
6991 cargo run --bin exam_q5_odd_even
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q5_odd_even`
6991 cargo run --bin exam_q5_duration
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q5_duration`
6991 cargo run --bin exam_q5_naughty_nice
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q5_naughty_nice`
```

Partial marks will be awarded for solutions which pass a subset of the test cases.

------

Write your answer in `exam_q5/src/lib.rs`.

When you think your program is working, you can use `autotest` to run some simple automated tests:

```
6991 autotest
```

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q5 lib.rs
```

### (optional) exercise: 23T3 Q6: Theory (10 marks)

## Q6.1 (4 marks)

The following code demonstrates two possible appearances of so-called "safety comments" in Rust, with the details redacted.

```rust
/// # Safety
/// ...
///
pub unsafe fn my_unsafe_fn(x: *const char) -> *const i32 {
    // Safety: ...
    unsafe {
        // ...
    }
}
```

**Question:**

1. Explain the purpose of the first safety comment. *(1 mark)*
2. Explain the purpose of the second safety comment. *(1 mark)*
3. Explain how safety comments are validated in Rust. Make reference to at least 1 specific technique. *(2 marks)*

------

Write your answer in `exam_q6/q6_1.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q6_1 q6_1.txt
```

## Q6.2 (6 marks)

The following code attempts to write an implementation of a linked list, making use of `unsafe` code.

```rust
use std::ptr::{self, null_mut};

struct LinkedList<T> {
    head: *mut Node<T>,
    tail: *mut Node<T>,
}

struct Node<T> {
    data: T,
    next: *mut Node<T>,
}

impl<T> LinkedList<T> {
    fn new() -> Self {
        Self {
            head: ptr::null_mut(),
            tail: ptr::null_mut(),
        }
    }

    fn push(&mut self, data: T) {
        let node = &mut Node {
            data,
            next: null_mut(),
        } as *mut Node<T>;

        if self.head.is_null() {
            self.head = node;
            self.tail = node;
        } else {
            let curr_tail = unsafe { &mut *self.tail };
            curr_tail.next = node;

            self.tail = node;
        }
    }

    fn pop(&mut self) -> Option<T> {
        unsafe {
            if self.tail.is_null() {
                None
            } else if self.head == self.tail {
                let data = ptr::read(self.head).data;

                self.head = null_mut();
                self.tail = null_mut();

                Some(data)
            } else {
                let mut curr = self.head;
                
                while ptr::read(curr).next != self.tail {
                    curr = ptr::read(curr).next;
                }

                let data = ptr::read(self.tail).data;
                ptr::read(curr).next = null_mut();

                Some(data)
            }
        }
    }
}
```

**Question:**

1. Perform a code review on the linked list implementation carefully examining the usage of `unsafe`. *(5 marks)*
2. Make a judgement on the overall soundness of the code. *(1 mark)*

------

Write your answer in `exam_q6/q6_2.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q6_2 q6_2.txt
```

### (optional) exercise: 23T3 Q7: Theory (10 marks)

The final question of the exam will be a more open-ended question which will ask you to perform some analysis or make an argument. Your argument will be judged alike an essay (i.e. are your claims substantiated by compelling arguments). Remember that you **will not** get any marks for blindly supporting / opposing Rust.

In early October 2023, Bjarne Stroustrup (creator of the C++ language) gave a keynote speech at the 2023 C++ conference. This talk outlined important concerns he had about C++, and about how they would be addressed. The New Stack, a tech-focused news site, published an article that summarised his talk, which we have excerpted below. You are **not** expected to read the full article, though you can [find it here ](https://thenewstack.io/bjarne-stroustrups-plan-for-bringing-safety-to-c/)The excerpt is copied below (which you **are** expected to read, and is also available in the `exam_q7` directory as `bjarne.txt`):

```
# Bjarne Stroustrup's plan for bringing safety to C++

Published by The New Stack, by David Cassel

The 72-year-old creator of C++, [Bjarne Stroustrup,] gave a forward-looking
keynote address last month as the programming language’s annual convention.

...

Early in the presentation, Stroustrup shared a slide titled “Safety is not just
type safety,” highlighting everything from resource leaks and overflows to
memory corruption and timing errors. There’s concurrency errors, termination
errors — and of course, type errors. “Often the safety mentioned is just memory
safety — that’s not enough… And the need to interoperate with other languages,
including C++ and C, tend not to be mentioned. And the cost of conversion can be
ferocious. That’s rarely mentioned…”

“And anyway — which other language? The way I have seen it argued, we are going
to have C++ replaced by about seven different languages, as of suggestions of
about now. By the time it happens — 40 years from now — we’ll probably have 20
different ones, and they have to interoperate. This is going to be difficult.”

Elsewhere in the talk Stroustrup also points out that “A lot of the so-called
‘safe’ languages outsource all the low-level stuff to C or C++,” temporarily
escaping the original language to access hardware resources or even the
operating system (which is often written in C) — or even “trusted code” which
may actually be very old, tucked away in an external library… or written in an
entirely different programming language.

As Stroustrup sees it, “This idea of just building a new system over on the
side, without any of the problems of the old one, is a fantasy. But it’s a very
popular fantasy.”

...

So about 54 minutes into the talk, Stroustrup told his audience, “Now I want to
get to future stuff: where do we go from here…? ”

...

Stroustrup has arrived at his solution: profiles. (That is, a set of rules
which, when followed, achieve specific safety guarantees.)
...
Stroustrup lays out the general strategy: using static analysis to eliminate
potential errors. But “Global static analysis is just unaffordable,” Stroustrup
adds. “So basically we need rules to simplify what we are writing to something
that can be analyzed efficiently and cheaply — local static analysis… And then
provide libraries to make relying on these rules feasible.”

One slide also noted another advantage: that “Gradual conversion from older code
to modern code offering guarantees is supported. The slide emphasized that
there’ll be a standard “fundamental” set of guarantees, with a larger, open
universe of available guarantees. Stroustrup says “I’m imagining type- and
resource-safety, memory safety, range safety. Arithmetic safety, things like
that, could be standardized.” And there will also be rules for applying
different guarantees to different fragments of code.

Code could even gets explicit expressions of which guarantees were applied (thus
reassuring future readers). Stroustrup again put up his slide listing the “many
notions of safety” — a slide titled “Safety is not just type safety,”
highlighting resource leaks, overflows, memory corruption, timing errors,
concurrency errors, termination errors — and of course, type errors.

One slide succinctly makes the case: “Being careful” doesn’t scale. So while the
core guidelines may suggest safe coding practices, “We need enforced rules.” As
Stroustrup puts it, “We have to formulate the rules for safe use. We have to
provide ways of verifying that people actually do what they’re trying to do.”
Stroustrup points out that much of what he’s describing has already been tried,
even at scale. “But nowhere has it all been integrated into a consistent,
coherent whole. And that’s what I’m arguing we should do.”

One slide lays out the formula in six words: hygiene rules + static analysis +
run-time checks. Stroustrup put up a slide saying C++ can eliminate many common
errors — including uninitialized variables, range errors, null pointer
dereferencing, resource leaks, and dangling references.

[End of excerpt]
```

------

Read through the excerpt above, and **discuss** the following prompt:

##### Gradual conversion of existing code to a new "profiles" system is a compelling alternative to widespread adoption of Rust.

The overall *structure* of your answer is **not** marked. For example, your answer may include small paragraphs of prose accompanied by dot-points, or could instead be posed as a verbal discussion with your friend. Regardless of the structure / formatting you choose, the **substance** of what you write is the most important factor, and is what will determine your overall mark for this question.

Only responses less than 1000 words will be marked for this question. There will be many good answers that are significantly shorter (see above), this limit is a cap to save our marking time, and your sanity.

From [UNSW's Glossary of Task Words](https://www.student.unsw.edu.au/glossary-task-words):

| **Discuss** | Investigate or examine by argument. Examine key points and possible interpretations, sift and debate, giving reasons for and against. Draw a conclusion. |
| ----------- | ------------------------------------------------------------ |
|             |                                                              |

------

Write your answer in `exam_q7/q7.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q7 q7.txt
```