use bmp::consts::{RED, LIME, BLUE, WHITE};

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();

    for path in args.iter() {
        println!("===== {path} =====");
        let img = bmp::open(path);
        match img {
            Ok(_) => {
               let image = img.unwrap();
                for x in 0..image.get_height() {
                    for y in 0..image.get_width() {
                        match image.get_pixel(y, x) {
                            RED => print!("R "),
                            BLUE => print!("B "),
                            LIME => print!("G "),
                            WHITE => print!("W "),
                            _ => panic!("given a colour not r g or b"),
                        }
                    }
                    println!();
                }
            }
            Err(e) =>  {
                println!("Error! {e:?}");
            }
        }
    }
}
