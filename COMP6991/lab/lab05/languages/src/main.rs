use std::convert::From;

struct English;
struct Spanish;
struct French;

trait Greeting {
    fn greet(&self);
}

impl Greeting for English {
    fn greet(&self) {
        println!("Hello!");
    }
}

impl Greeting for Spanish {
    fn greet(&self) {
        println!("Hola!");
    }
}

impl Greeting for French {
    fn greet(&self) {
        println!("Bonjour!");
    }
}

struct Person {
    name: String,
    // Do you understand why this is `Box<dyn Greeting>>` instead of `Box<Greeting>` ?
    greetings: Vec<Box<dyn Greeting>>,
}

// TODO (1): Add your impl From block below, before main!
impl From<&str> for Box<dyn Greeting> {
    fn from(lang: &str) -> Self {
        if lang.contains("English") {
            Box::new(English)
        } else if lang.contains("Spanish") {
            Box::new(Spanish)
        } else {
            Box::new(French)
        }
    }
}

// DO NOT NEED TO CHANGE MAIN
fn main() {
    // john can speak English and Spanish
    let person = Person {
        name: "John".to_string(),
        greetings: vec!["English".into(), "Spanish".into()],
    };

    speak_all_greetings(&person);

    // jane can speak French
    let person = Person {
        name: "Jane".to_string(),
        greetings: vec!["French".into()],
    };

    speak_all_greetings(&person);
}

fn speak_all_greetings(person: &Person) {
    println!("{} says:", person.name);
    //TODO (2): iterate over the greetings and call greet() on each one
    person.greetings.iter().for_each(|e| e.greet());
}
