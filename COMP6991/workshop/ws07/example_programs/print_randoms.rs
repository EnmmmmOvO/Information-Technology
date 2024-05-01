use rand::distributions::{Distribution, Uniform};
use std::{thread, time};

fn gen_randoms() {
    let mut rng = rand::thread_rng();
    let d20 = Uniform::from(1..=20);

    loop {
        let ten_millis = time::Duration::from_millis(10);

        thread::sleep(ten_millis);
        let throw = d20.sample(&mut rng);
        println!("Roll the die: {}", throw);

        if throw == 1 {
            break;
        }
    }
}

fn main() {
    gen_randoms();
}
