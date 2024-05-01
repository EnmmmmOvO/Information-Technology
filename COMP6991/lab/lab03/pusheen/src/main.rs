fn main() {
    let mut vec = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // Within the context of Rust's borrowing rules, only a single mutable reference is permitted within the same scope. For the given problem:

    // let a = &mut vec;  constitutes the first mutable reference;
    // let b = &mut vec;  constitutes the second mutable reference, within the scope of a;
    
    // a.push(11);        occurs within the scope of a, where there exists another mutable reference to the same target besides a, contravening 
    //                    Rust's borrowing rules, hence, it fails to compile.
    // b.push(12);

    // Rust enforces this rule to ensure that at any given moment, only one pointer can write data, thus averting undefined behavior resulting
    // from data races, and ensuring data safety and concurrency safety.

    let a = &mut vec;
    a.push(11);

    let b = &mut vec;
    b.push(12);

    // Upon adjustment, the scope of a concludes following the execution of a.push(11). When b is instantiated, a is no longer in use, thus 
    // Rust permits the creation of a new mutable reference, b.
}
