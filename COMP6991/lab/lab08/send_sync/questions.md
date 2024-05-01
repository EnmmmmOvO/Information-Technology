1. I saw someone's code fail to compile because they were trying to send non-thread-safe data across threads. How does the Rust language allow for static (i.e. at compile time) guarantees that specific data can be sent/shared acrosss threads?

   > Rust uses the `Send` and `Sync` marker traits to enforce at compile time that data can safely be sent or shared across threads. If a type implements `Send`, it can be transferred to another thread. If it implements `Sync`, references to it can be shared across threads. The Rust compiler checks these trait implementations to prevent data races and ensure thread safety.

2. Do you have to then implement the Send and Sync traits for every piece of data (i.e. a struct) you want to share and send across threads?

   > It don't always have to manually implement the Send and Sync traits. Rust automatically implements these traits for types whose components are all Send or Sync. However, for types that encapsulate non-thread-safe behavior, you might need to implement these traits manually, ensuring thread safety in your implementation.

3. What types in the course have I seen that aren't Send? Give one example, and explain why that type isn't Send.

   > An example of a type that isn't `Send` is `Rc<T>` (the reference-counted pointer). `Rc<T>` isn't `Send` because it doesn't use atomic operations for reference counting, making it unsafe to share between threads as simultaneous modifications from multiple threads can lead to undefined behavior.

4. What is the relationship between Send and Sync? Does this relate to Rust's Ownership system somehow?

   > `Send` allows ownership of a type to be transferred between threads, while `Sync` allows a type to be safely shared by multiple threads via references. Both relate to Rust's ownership system by ensuring thread safety: `Send` by transferring ownership and `Sync` by enabling safe shared access. They prevent data races by ensuring proper synchronization or ownership semantics are followed.

5. Are there any types that could be Send but NOT Sync? Is that even possible?

   > Yes, it's possible for types to be `Send` but not `Sync`. For example, `Mutex<T>` is `Send` but not inherently `Sync` because while it can be safely moved to another thread (`Send`), direct shared access to its contents without locking (which would make it `Sync`) can lead to race conditions.

6. Could we implement Send ourselves using safe rust? why/why not?

   > Implementing `Send` using only safe Rust is not straightforward because `Send`'s safety guarantees often rely on internal mutability or synchronization primitives, which require careful management of memory and concurrency properties. While Rust's safe concurrency primitives like `Mutex<T>` and `Arc<T>` help manage this, creating a new type that is `Send` typically involves leveraging these existing thread-safe types rather than implementing `Send` from scratch in safe Rust.

