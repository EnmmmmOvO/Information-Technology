use rand::Rng;

use std::time::Instant;

struct ParallelIterator {
    iter: Vec<i32>
}

impl ParallelIterator {
    fn find(&self, search_for: i32) -> Option<usize> {
        // TODO
        None
    }

    fn find_all(&self, search_for: i32) -> Vec<usize> {
        // TODO
        vec![]
    }

    fn map(&self /*you will need to add the argument here*/) -> Vec<i32> {
        // TODO
        vec![]
    }

}

trait IntoParIter {
    fn into_par_iter(self) -> ParallelIterator;
}

impl IntoParIter for Vec<i32> {
    fn into_par_iter(self) -> ParallelIterator {
        ParallelIterator { iter: self }
    }
}

fn time<T>(test_name: &str, data: T, f: impl Fn(T) -> ()) {
    let before = Instant::now();
    f(data);
    println!("Test {test_name}: {:.2?}", before.elapsed());
}


fn main() {
    let test_length = 1000000;
    let find_index = 77722;

    let mut nums: Vec<i32> = vec![0, 1].repeat(test_length / 2);
    nums[find_index] = 2;
    nums[find_index + 100] = 2;
    nums[find_index + 1000] = 2;

    time("find_normal", nums.clone(), |nums| {
        let mut iter = nums.into_iter();
        assert_eq!(iter.position(|i| i == 2), Some(find_index));
    });

    time("find_parallel", nums.clone(), |nums| {
        let iter = nums.into_par_iter();
        assert_eq!(iter.find(2), Some(find_index));
    });
}
