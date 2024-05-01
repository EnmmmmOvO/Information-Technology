use std::io::{self, Write};

 fn main() {
    print!("What is your name? ");
    io::stdout().flush().expect("Error: Could not flush stdout");

    let mut name = String::new();

    io::stdin().read_line(&mut name).expect("Error: Could not read line from stdin");
    
    if let Some(pos) = name.find('\n') {
        name.truncate(pos);
    }

    if name.len() == 0 {
        println!("No name entered :(, goodbye.");
    } else {
        println!("Hello, {}, nice to meet you!", name);
    }

}
