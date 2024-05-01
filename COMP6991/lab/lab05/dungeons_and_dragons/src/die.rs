use rand::prelude::*;
use rand_chacha::ChaCha20Rng;

/// Takes in a max value and returns a random number between 1 and max
// DO NOT MODIFY
fn get_random_value(max: u8) -> u8 {
    let mut rng = ChaCha20Rng::seed_from_u64(2);
    rng.gen_range(1..=max)
}

pub enum Die {
    D4,
    D6,
    D8,
    D10,
    D12,
    D20,
}

pub struct Coin;


// MODIFY/ADD BELOW HERE ONLY


pub fn roll<T: Num>(item: T) -> u8 {
    get_random_value(item.num())
}

pub trait Num {
    fn num(&self) -> u8;
}

impl Num for Coin {
    fn num(&self) -> u8 {
        2
    }
}

impl Num for Die {
    fn num(&self) -> u8 {
        match self {
            Die::D4 => 4,
            Die::D6 => 6,
            Die::D8 => 8,
            Die::D10 => 10,
            Die::D12 => 12,
            Die::D20 => 20,
        }
    }
}

