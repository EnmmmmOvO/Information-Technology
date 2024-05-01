use std::io;

fn main() {
    let pattern_string = std::env::args()
        .nth(1)
        .expect("missing required command-line argument: <pattern>");

    let pattern = &pattern_string;

    let mut input = String::new();
    loop {
        match io::stdin().read_line(&mut input) {
            Ok (0) => break,
            Ok (_) => {
                if input.contains(pattern) {
                    print!("{input}");
                }
                input.clear();
            }
            Err (e) => {
                eprintln!("error: {}", e);
                break;
            }
        }
    }
}
