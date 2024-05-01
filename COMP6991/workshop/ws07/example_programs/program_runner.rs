//! This program runs a program and writes its output
//! to a file.
use std::process::Command;
use std::fs::File;
use std::env;

pub fn execute(args: &[String]){
    let log = File::create(&args[1]).expect("failed to open log");

    let mut cmd = Command::new(&args[2])
        .args(&args[3..])
        .stdout(log)
        .spawn()
        .expect("failed to start ");

    cmd.wait().expect("failed to finish ");

}


fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        panic!("Usage: ./program_runner output_file argv")
    }
    execute(&args);
}
