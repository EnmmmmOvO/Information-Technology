### (optional) exercise: 23T1 Q1: Theory (10 marks)

## Q1.1 (4 marks)

**Question:**

1. Explain the difference between the `&str` and `String` types, with respect to *ownership*. *(1 mark)*
2. Explain how the behaviour regarding *lifetimes* differ between `&str` and `String`. *(1 mark)*
3. Outline an example of when a `&str` might be used instead of a `String`. *(1 mark)*
4. Outline an example of when a `String` might be used instead of a `&str`. *(1 mark)*

------

Write your answer in `exam_q1/q1_1.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q1_1 q1_1.txt
```

## Q1.2 (2 marks)

The following Rust code fails to compile, but equivalent code in other popular programming languages (e.g. C, Java, Python) compiles and/or works correctly.

```rust
fn main() {
	let my_string = String::from("Hello, World!");

	// print the string twice
	print_string(my_string);
	print_string(my_string);
}

fn print_string(string: String) {
	println!("{string}");
}
```

**Question:**

1. Explain what issue(s) prevent the Rust compiler from building this code. *(1 mark)*
2. Explain the philosophy behind this language decision. *(1 mark)*

------

Write your answer in `exam_q1/q1_2.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q1_2 q1_2.txt
```

## Q1.3 (4 marks)

**Question:**

Idiomatic Rust programs often extensively use enums when considering errors or other failure cases. Select another programming language of your choice (e.g. C, Java, Python, Go, etc.), and contrast its equivalent error-handling features with Rust.

Provide at least three individual points of contrast *(3 marks)*, along with an overall judgement as to their merits and disadvantages. *(1 mark)*

Any reasonable programming language is an acceptable choice for this question.

Esoteric languages (e.g., Brainf***, INTERCAL, etc.) are not acceptable, and will not receive marks.

You must select a **programming** language. Languages that do not involve programming (e.g. markup languages (HTML, Markdown), query languages (SQL, jq), etc.) are not acceptable, and will not receive marks.

Programming languages that are slightly more niche (e.g. Haskell, Zig, Swift, Lisp) are perfectly acceptable.

If you are unsure whether your programming language is "reasonable", simply default to C.

------

Write your answer in `exam_q1/q1_3.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q1_3 q1_3.txt
```

### (optional) exercise: 23T1 Q2: Practical (10 marks)

Boris is attempting to write a function `split_once`, which takes two string slices: `string` and `split_on`. If `split_on` occurs within `string`, it will return `Some` tuple of the slice of `string` that exists before the first occurence of `split_on`, and the remainder of `string` after the first occurence.

Boris is certain that he has written the implementation of the function correctly, but is not so confident in Rust when it comes to lifetimes. Sadly, his code does not compile currently.

```rust
pub fn split_once<'a, 'b>(string: &'a str, split_on: &'b str) -> Option<(&'b str, &'a str)> {
    let index = string.find(split_on)?;
    let tuple = (&string[..index], &string[index + split_on.len()..]);

    Some(tuple)
}
```

Your task is to fix the lifetimes issue with Boris' broken code. You only have to modify lifetimes in order to solve the issue, and thus you are not permitted to change any code except that relevant to lifetimes in `src/lib.rs`. You are permitted to add, remove, and modify lifetimes in this exercise.

This is an example of the expected behaviour:

```sh
6991 cargo run --bin exam_q2
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q2`
Some(("hello", "world"))

6991 cargo run --bin exam_q2_alt
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q2_alt`
Some(("hello", "world"))
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

### (optional) exercise: 23T1 Q3: Theory (10 marks)

Luke is trying to define a library of sports cars for use in his Rust programs. He decides that he would like to make use of the trait system to do so, and so defines the following trait:

```rust
pub trait Car {
	fn brand(&self) -> CarBrand;
	fn horsepower(&self) -> u32;
}

pub enum CarBrand {
	Toyota,
	Subaru,
	Nissan,
}
```

Because defining a type and implementing a trait for each individual car requires a substantial amount of boilerplate, he also defines a macro to make the process simpler:

```rust
#[macro_export]
macro_rules! car {
	($name:ident, $brand:expr, $horsepower:literal) => {
		pub struct $name;
		impl Car for $name {
			fn brand(&self) -> CarBrand {
				use CarBrand::*;
				$brand
			}
			fn horsepower(&self) -> u32 {
				$horsepower
			}
		}
	}
}
```

And so defines the individual cars like such:

```rust
car!(Corolla,  Toyota, 100);
car!(Cressida, Toyota, 160);
car!(Chaser,   Toyota, 220);

car!(Liberty,  Subaru, 100);
car!(Impreza,  Subaru, 130);
car!(Wrx,      Subaru, 200);

car!(Pulsar,   Nissan, 90);
car!(Silvia,   Nissan, 200);
car!(Skyline,  Nissan, 220);
```

This all seems to have worked correctly, so he creates his first function, `favourite_car`, which given a particular `CarBrand` will return back his favourite car model from that brand:

```rust
fn favourite_car(brand: CarBrand) -> impl Car {
	use CarBrand::*;

	match brand {
		Toyota => Cressida,
		Subaru => Liberty,
		Nissan => Skyline,		
	}
}
```

However, attempting to build this leads Luke into a problem:

```sh
6991 cargo build
   Compiling cars v0.1.0
error[E0308]: `match` arms have incompatible types
  --> src/favourite.rs:8:13
   |
6  | /     match brand {
7  | |         Toyota => Cressida,
   | |                   -------- this is found to be of type `cars::Cressida`
8  | |         Subaru => Liberty,
   | |                   ^^^^^^^ expected struct `cars::Cressida`, found struct `cars::Liberty`
9  | |         Nissan => Skyline,
10 | |     }
   | |_____- `match` arms have incompatible types
```

## Q3.1 (4 marks)

**Question:**

1. Explain why Luke is receiving this error message, even with an `impl Car` return type. *(1 mark)*
2. Explain two issues Rust (the language) would face if this behaviour were to be allowed. *(2 marks)*
3. Provide an example of a possible fix for Luke's issue. *(1 mark)*

------

Write your answer in `exam_q3/q3_1.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q3_1 q3_1.txt
```

## Q3.2 (3 marks)

Luke decides that his `car!` macro still has a bit too much boilerplate. Instead of defining cars individually, he would like to only perform one macro invocation for a whole brand of cars at a time.

That is, he would like to modify his macro such that the following code works equivalently:



```rust
car! {
	brand  = Toyota;
	models = [
		Corolla  = 100,
		Cressida = 160,
		Chaser   = 220,
	];
}

car! {
	brand  = Subaru;
	models = [
		Liberty = 100,
		Impreza = 130,
		Wrx     = 200,
	];
}

car! {
	brand  = Nissan;
	models = [
		Pulsar  = 90,
		Silvia  = 200,
		Skyline = 220,
	];
}
```

**Question**

Rewrite Luke's macro as described. Provide the full `macro_rules!` definition in your response. *(3 marks)*

------

Write your answer in `exam_q3/q3_2.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q3_2 q3_2.txt
```

## Q3.3 (3 marks)

Luke would finally like to parameterise the `Car` trait to include type-level information about the car's transmission layout. There are three possible transmission layouts in Luke's library: front-wheel drive, rear-wheel drive, and all-wheel drive.

Luke knows that most cars are only sold with one choice of transmission layout. For example, all `Wrx`s are all-wheel drive, and all `Silvia`s are rear-wheel drive.

However, some cars may support different transmission layouts. For example, while `Corolla`s were originally rear-wheel drive, newer `Corolla`s can come in both front-wheel drive *and* all-wheel drive!

With this in mind, Luke settles on two options for his trait design:

```rust
// Layouts
struct RearWheelDrive;
struct FrontWheelDrive;
struct AllWheelDrive;

// Trait definition:

// Option 1
pub trait Car<Layout> {
	fn brand(&self) -> CarBrand;
	fn horsepower(&self) -> u32;
}

// Option 2
pub trait Car {
	type Layout;

	fn brand(&self) -> CarBrand;
	fn horsepower(&self) -> u32;
}
```

**Question**

1. Explain the differences between Luke's two options. *(2 marks)*
2. With the information provided, which option is more suitable for Luke's case? *(1 mark)*

------

Write your answer in `exam_q3/q3_3.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q3_3 q3_3.txt
```

### (optional) exercise: 23T1 Q4: Theory (10 marks)

## Q4.1 (4 marks)

The following program attempts to launch two new threads, which each print a shared string.

```rust
use std::thread;

fn main() {
	let the_string = String::from("Hello, World!");

	let handle_1 = thread::spawn(|| {
		print_string(&the_string);
	});

	let handle_2 = thread::spawn(|| {
		print_string(&the_string);
	});

	handle_1.join().unwrap();
	handle_2.join().unwrap();
}

fn print_string(string: &str) {
	println!("{string}");
}
```

However, the code does not compile.

Note: the signature of `std::thread::spawn` is as follows:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
where
    F: FnOnce() -> T + Send + 'static,
    T: Send + 'static,
{
	...
}
```

**Question:**

1. Explain why the code does not compile. *(1 mark)*
2. Identify the **specific** part of `std::thread::spawn`'s signature that is responsible for this compiler error. *(1 mark)*
3. Explain two possible solutions to fix this issue. *(2 marks)*

------

Write your answer in `exam_q4/q4_1.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q4_1 q4_1.txt
```

## Q4.2 (3 marks)

When `lock()` is called on a `std::sync::Mutex`, a `Result` containing a `MutexGuard` is returned.

**Question:**

1. How does the `Mutex` automatically unlock itself? *(1 mark)*
2. How does Rust statically prevent programmers from extracting the guarded value out of a `MutexGuard`? *(2 marks)*

------

Write your answer in `exam_q4/q4_2.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q4_2 q4_2.txt
```

## Q4.3 (3 marks)

The signature of `std::iter::Iterator::map` looks approximately like the following:

```rust
pub trait Iterator {
	type Item;

	...

	fn map<B, F>(self, f: F) -> Map<Self, F>
	where
	    F: FnMut(Self::Item) -> B,
	{
		...
	}
}
```

However, the `rayon` crate's equivalent function, `rayon::iter::ParallelIterator::map` contains some subtle differences:

```rust
pub trait ParallelIterator: Send {
	type Item: Send;

	...

	fn map<F, R>(self, map_op: F) -> Map<Self, F>
	where
		F: Fn(Self::Item) -> R + Sync + Send,
		R: Send,
	{
		...
	}
}
```

**Question:**

1. Justify the change in type bounds to the `type Item` associated type parameter. *(1 mark)*
2. Justify the change in type bounds involving `Send` and `Sync` within `fn map`. *(1 mark)*
3. Justify the change in function trait (`FnMut` to `Fn`) for the provided closure to `map`. *(1 mark)*

------

Write your answer in `exam_q4/q4_3.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q4_3 q4_3.txt
```

### (optional) exercise: 23T1 Q5: Practical (10 marks)

In this question, you will implement a basic in-memory cache.

A cache is a data-type which when given some input, will perform some calculation and return the result. However, if the calculation for that specific input had already been performed previously, the cache will simply return the result of the previous calculation, instead of doing the hard work again.

You have been given `src/lib.rs`, which describes a very simple cache primitive:

```rust
use std::{collections::HashMap, rc::Rc};

pub struct Cache {
    calculator: fn(&String) -> String,
    cache_map: HashMap<String, Rc<String>>,
}

impl Cache {
    pub fn new(calculator: fn(&String) -> String) -> Self {
        Cache {
            calculator,
            cache_map: HashMap::new(),
        }
    }

    pub fn get(&mut self, key: String) -> Rc<String> {
        if let Some(value) = self.cache_map.get(&key) {
            Rc::clone(value)
        } else {
            let value = Rc::new((self.calculator)(&key));
            self.cache_map.insert(key, Rc::clone(&value));

            value
        }
    }
}
```

This code correctly implements an in-memory cache that works only for key-value pairs of type `String`. That is, the cache will work for a `calculator` of type `fn(&String) -> String`, and allow you to query/fill the cache with the `get` function turning a `String` key into an `Rc<String>` value.

Your task is to make this cache more generic. You must modify the type of the calculator from a function pointer of `&String -> String` into a closure of `&Key -> Value` for any possible types `Key` and `Value`. As part of this, you must also decide which type of closure is the most generic choice out of `FnOnce`, `FnMut` and `Fn`.

This will also require you to change the generic parameters within the `HashMap` from `<String, Rc<String>>` into `<Key, Rc<Value>>`, and similarly within the `get` function, as previously described in the calculator closure.

You will be required to constrain some generic type parameters as you solve the exercise. You must ensure that you do not overly constrain the types, only requiring what is minimally needed.

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

### (optional) exercise: 23T1 Q6: Theory (10 marks)

## Q6.1 (4 marks)

**Question:**

1. Is it possible to invoke undefined behaviour in Rust? If so, how? If not, why? *(1 mark)*
2. Explain the difference between an unsafe block and an unsafe function in Rust. *(1 mark)*
3. Describe the technique of unsafe implementations behind safe abstractions, and explain how it reduces Rust's scope for unsoundness. *(2 marks)*

------

Write your answer in `exam_q6/q6_1.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q6_1 q6_1.txt
```

## Q6.2 (6 marks)

The following code attempts to write an (inefficient, but simple) implementation of a `channel` using `unsafe`. In particular, it implements a bounded-buffer single-producer single-consumer channel where the bound is always 1.

```rust
pub fn channel() -> (Sender<i32>, Receiver<i32>) {
	let buffer  = Box::into_raw(Box::new(None::<i32>));
	let hung_up = Box::into_raw(Box::new(false));

	let sender   = Sender   { buffer, hung_up };
	let receiver = Receiver { buffer, hung_up };

	(sender, receiver)
}

pub struct Sender<T> {
	buffer:  *mut Option<T>,
	hung_up: *mut bool,
}

pub struct Receiver<T> {
	buffer:  *mut Option<T>,
	hung_up: *mut bool,
}

impl<T> Sender<T> {
	pub fn send(&mut self, value: T) -> Option<()> {
		if unsafe { *self.hung_up } {
			return None;
		}

		// wait until the channel is empty...
		loop {
			let value = unsafe { std::ptr::read(self.buffer) };
			if value.is_none() { break; }
			std::mem::forget(value);
		}

		// send the value into the shared buffer
		unsafe { std::ptr::write(self.buffer, Some(value)); }

		Some(())
	}
}

impl<T> Receiver<T> {
	pub fn recv(&mut self) -> Option<T> {
		loop {
			if unsafe { *self.hung_up } {
				return None;
			}

			// wait until the value exists...
			if let Some(value) = unsafe { std::ptr::read(self.buffer) } {
				// clear the channel for the next message
				unsafe { std::ptr::write(self.buffer, None); }

				return Some(value);
			}
		}
	}
}

unsafe impl<T: Send> Send for Sender<T> {}
unsafe impl<T> Send for Receiver<T> {}

impl<T> Drop for Sender<T> {
	fn drop(&mut self) {
		unsafe { *self.hung_up = true; }
	}
}

impl<T> Drop for Receiver<T> {
	fn drop(&mut self) {
		unsafe { *self.hung_up = true; }
	}
}
```

It can be used like this:

```rust
use exam_q6_lib::channel;

fn main() {
	std::thread::scope(|scope| {
		let (mut send, mut recv) = channel();

		scope.spawn(move || {
			while let Some(num) = recv.recv() {
				println!("Thread got {num}!");
			}

			println!("Thread finished!");
		});

		for i in 1..=5 {
			println!("Sending {i}...");
			send.send(i);
		}

		println!("Sending finished!");
		drop(send);
	});
}

```

```sh
6991 cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q6`
Sending 1...
Sending 2...
Sending 3...
Thread got 1!
Sending 4...
Thread got 2!
Thread got 3!
Thread got 4!
Sending 5...
Thread got 5!
Sending finished!
Thread finished
```

However, sometimes when it is run, the thread never receives the final message!

```sh
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/exam_q6`
Sending 1...
Sending 2...
Sending 3...
Thread got 1!
Thread got 2!
Thread got 3!
Sending 4...
Sending 5...
Sending finished!
Thread got 4!
Thread finished
```

**Question:**

1. Perform a code review on the channel implementation *(not the main function)*, carefully examining the usage of `unsafe` and make a judgement on the overall soundness. *(4 marks)*
2. Demonstrate or otherwise explain how to fix the issue shown above where the thread sometimes does not receive the final message. Pasting a `diff` of the necessary changes to `lib.rs` is sufficient. *(2 marks)*

------

Write your answer in `exam_q6/q6_2.txt`.

When you are finished working on your answer, submit your work with **give**:

```
give cs6991 exam_q6_2 q6_2.txt
```

### (optional) exercise: 23T1 Q7: Theory (10 marks)

The final question of the exam will be a more open-ended question which will ask you to perform some analysis or make an argument. Your argument will be judged alike an essay (i.e. are your claims substantiated by compelling arguments). Remember that you **will not** get any marks for blindly supporting / opposing Rust.

On November 10th 2022, the USA's National Security Agency (i.e. NSA) published a "Cybersecurity Information Sheet" investigating software memory safety. In this 7 page document (which you **are not** expected to read, but is accessible [here](https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF) and as a PDF in the `exam_q7` directory as `nsa.pdf`), the NSA explains that memory safety vulnerabilities represent a potent security threat, to the extent that memory-unsafe languages should be avoided if at all possible. Their overall conclusion is included within the following excerpt (which you **are** expected to read, and is also available in the `exam_q7` directory as `nsa_excerpt.txt`):

```
Examples of memory safe language include C#, Go, Java®, Ruby™, Rust®, and Swift®.

[...]

Memory issues in software comprise a large portion of the exploitable vulnerabilities
in existence. NSA advises organizations to consider making a strategic shift from
programming languages that provide little or no inherent memory protection, such as
C/C++, to a memory safe language when possible.

[...]

Memory safe languages provide differing degrees of memory usage protections, so available
code hardening defenses, such as compiler options, tool analysis, and operating system
configurations, should be used for their protections as well. By using memory safe
languages and available code hardening defenses, many memory vulnerabilities can be
prevented, mitigated, or made very difficult for cyber actors to exploit.
```

In response to this advisory, Bjarne Stroustrup (the designer and implementor of the C++ programming language) published a C++ Standards committee paper titled **A call to action: Think seriously about 'safety'; then do something sensible about it** on December 6th 2022. This paper (in a slightly redacted form) is provided below (and as a text file as `bjarne.txt` in the `exam_q7` directory).

```
[ in response to the NSA information sheet ]

That specifically and explicitly excludes C and C++ as unsafe. As is far too
common, it lumps C and C++ into the single category C/C++, ignoring 30+ years of
progress. Unfortunately, much C++ use is also stuck in the distant past, ignoring
improvements, including ways of dramatically improving safety.

Now, if I considered any of those "safe" languages superior to C++ for the range of
uses I care about, I wouldn't consider the fading out of C/C++ as a bad thing, but
that's not the case. Also, as described, "safe" is limited to memory safety, leaving
out on the order of a dozen other ways that a language could (and will) be used to
violate some form of safety and security.

[...]

There is not just one definition of "safety", and we can achieve a variety of kinds of
safety through a combination of programming styles, support libraries, and enforcement
through static analysis. [C++ language proposal P2410r0] gives a brief summary of
the approach. I envision compiler options and code annotations for requesting rules
to be enforced. The most obvious would be to request guaranteed full type-and-resource
safety. [C++ language proposal P2687R0] is a start on how the standard can support this,
R1 will be more specific. Naturally, comments and suggestions are most welcome.

Not everyone prioritizes "safety" above all else. For example, in application domains
where performance is the main concern, the [C++ language proposal P2687R0] approach
lets you apply the safety guarantees only where required and use your favorite tuning
techniques where needed. Partial adoption of some of the rules (e.g., rules for range
checking and initialization) is likely to be important. Gradual adoption of safety
rules and adoption of differing safety rules will be important. If for no other reason
than the billions of lines of C++ code will not magically disappear, and even "safe"
code (in any language) will have to call traditional C or C++ code or be called by
traditional code that does not offer specific safety guarantees.

Ignoring the safety issues would hurt large sections of the C++ community and undermine
much of the other work we are doing to improve C++. So would focusing exclusively
on safety.

What might "something sensible to do" be? I suggest making a list of issues that could
be considered safety issues (including UB) and finding ways of preventing them within
the framework of [C++ language proposal P2687R0]. That's what I plan to do.
```

From https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2739r0.pdf.

------

Read through the excerpt above, and **discuss** the following prompt:

##### Memory safety does not pose a significant enough threat to warrant substituting C or C++ code for Rust, as explained by Bjarne Stroustrup.

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