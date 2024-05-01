use std::collections::VecDeque;
use std::collections::LinkedList;
use std::collections::HashMap;

const MAX_ITER: i32 = 300000;

fn main() {
    // Vectors
    vec_operations();

    // VecDeque
    vec_deque_operations();

    // TODO: your code here, for linked list insertions
    linked_list_operations();

    // TODO: your code here, for hashmap insertions
    hashmap_operations();

    // TODO: your text explanation to the questions in the spec
    // Based on the results, it is evident that VecDeque is the fastest for both insertion and
    // deletion operations.

    // - Vec, lies in its insertion operation, which merely requires adding an element to a 
    //   contiguous memory area, with a time complexity of O(1). For deletion, since it involve 
    //   removing elements from the beginning, it necessitates moving elements to fill the gap, thus
    //   incurring certain overheads.

    // - VecDeque, being a double-ended queue, is optimized for insertion and deletion at both ends.
    //   Consequently, compared to Vec, it exhibits superior performance in both insertion and
    //   deletion times. Compare with Vec, Vec deletes an element from the beginning requires moving
    //   all remaining elements to fill the void, constituting an O(n) operation. Conversely, in
    //   VecDeque, deletion of elements from either the front or back is an O(1) operation, as it
    //   simply adjusts internal pointers to disregard the deleted element, eliminating the need to
    //   move other elements. VecDeque should be considered when there is a frequent need to add or
    //   remove elements at both ends of the collection.

    // - LinkedList, during insertion at the end, necessitates traversing the entire list each time.
    //   Additionally, it requires extra memory allocation and deallocation, rendering its 
    //   efficiency in insertion and deletion lower than that of Vec and VecDeque. LinkedList should 
    //   be considered when there is a frequent need to insert or delete elements in the middle of 
    //   the collection, especially when the number of elements is large. Additionally, since each
    //   element in a LinkedList is allocated individually, without the need to know the maximum 
    //   size of the data structure in advance, nor to reallocate the entire data structure when 
    //   increasing or decreasing elements, it offers certain advantages.

    // - HashMap, the insertion and deletion operations have a time complexity close to O(1),
    //   but the actual performance is influenced by the hash function and collision resolution
    //   strategy. Compared to the others, it takes a longer time to complete.

    // Did the results surprise you? Why or why not?.
    
    // - I was surprised by the optimization of Vec in Rust, particularly its significant
    //   advantage in insertion and deletion at the end compared to what I had always considered to
    //   be the faster operation of front deletion in a LinkedList.

    // - regarding HashMap, I understand that as the data volume increases, the efficiency of
    //   insertion and deletion becomes much lower than that of LinkedList, which also operates at
    //   O(n). This insight challenges preconceived notions about the performance of different data
    //   structures and underscores the importance of choosing the appropriate structure based on
    //   specific operational requirements.

    // - When testing on different machines, I found that VecDeque was faster on a Mac, but Vec was
    //   faster on a CSE machine. This could be due to differences in CPU architecture and
    //   frequency, as well as the speed and latency of memory, all of which can influence the
    //   results.


}

/// measure the insertion and removal
/// operations of a vector
fn vec_operations() {
    let mut vec = Vec::new();

    let time_start = std::time::Instant::now();
    for i in 0..MAX_ITER {
        vec.push(i);
    }
    let time_end = std::time::Instant::now();

    println!("==== Vector ====");
    println!("insert: {:?}", time_end - time_start);

    let time_start = std::time::Instant::now();
    for _ in 0..MAX_ITER {
        vec.remove(0);
    }
    let time_end = std::time::Instant::now();

    println!("remove: {:?}", time_end - time_start);
}

/// measure the insertion and removal
/// operations of a VecDeque
fn vec_deque_operations() {
    let mut vec_deque = VecDeque::new();

    let time_start = std::time::Instant::now();
    for i in 0..MAX_ITER {
        vec_deque.push_back(i);
    }
    let time_end = std::time::Instant::now();

    println!("==== VecDeque ====");
    println!("insert: {:?}", time_end - time_start);

    let time_start = std::time::Instant::now();
    for _ in 0..MAX_ITER {
        vec_deque.pop_front();
    }
    let time_end = std::time::Instant::now();

    println!("remove: {:?}", time_end - time_start);
}

/// measure the insertion and removal
/// operations of a LinkedList
fn linked_list_operations() {
    let mut linked_list = LinkedList::new();

    let time_start = std::time::Instant::now();
    for i in 0..MAX_ITER {
        linked_list.push_back(i);
    }
    let time_end = std::time::Instant::now();

    println!("==== LinkedList ====");
    println!("insert: {:?}", time_end - time_start);

    let time_start = std::time::Instant::now();
    for _ in 0..MAX_ITER {
        linked_list.pop_front();
    }
    let time_end = std::time::Instant::now();

    println!("remove: {:?}", time_end - time_start);
}

/// measure the insertion and removal
/// operations of a HashMap
fn hashmap_operations() {
    let mut hashmap = HashMap::new();

    let time_start = std::time::Instant::now();
    for i in 0..MAX_ITER {
        hashmap.insert(i, i);
    }
    let time_end = std::time::Instant::now();

    println!("==== HashMap ====");
    println!("insert: {:?}", time_end - time_start);

    let time_start = std::time::Instant::now();
    for i in 0..MAX_ITER {
        hashmap.remove(&i);
    }
    let time_end = std::time::Instant::now();

    println!("remove: {:?}", time_end - time_start);
}