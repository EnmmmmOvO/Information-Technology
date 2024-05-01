use libc::{fopen, fgets, fscanf, fclose, FILE, c_char, c_int, c_double};

struct File {
    // todo!()
}

/// This function converts a string into a Vec<i8> which can
/// be used to represent a c-string.
///
/// To turn this into a *mut c_char, use Vec<i8>::as_mut_ptr().
fn to_c_string(string: &str) -> Vec<i8> {
    let bytes: Vec<u8> = String::from(string).into_bytes();
    let mut c_chars: Vec<i8> = bytes.iter().map(| c | *c as i8).collect();

    c_chars.push(0); // null terminator

    c_chars
}

impl File {
    fn open(_path: &str) -> Option<Self> {
        todo!()
    }

    fn read_string(&mut self) -> Option<String> {
        todo!()
    }

    fn read_i64(&mut self) -> Option<i64> {
        todo!()
    }

    fn read_f64(&mut self) -> Option<f64> {
        todo!()
    }

    fn read_char(&mut self) -> Option<char> {
        todo!()
    }
}

impl Drop for File {
    fn drop(&mut self) {
        println!("Dropping file.");
    }
}


fn main() {
    let mut file = File::open("data/test_file.txt").expect("Could not open file.");
    let s = file.read_string().unwrap();
    let i = file.read_i64().unwrap();
    let f = file.read_f64().unwrap();
    let c = file.read_char().unwrap();

    println!("{s} {i} {f} {c}");
}
