use serde::Deserialize;
use std::collections::VecDeque;
use std::io;

#[derive(Debug, Deserialize)]
enum Instruction {
    Set(i32),
    Left,
    Right,
    Reset,
}

#[derive(Debug, PartialEq)]
struct Light {
    // TODO: change me!
    left: Option<Box<Light>>,
    right: Option<Box<Light>>,
    brightness: i32,
}

fn get_instructions_from_stdin() -> VecDeque<Instruction> {
    let mut instructions = String::new();
    io::stdin().read_line(&mut instructions).unwrap();
    ron::from_str(&instructions).unwrap()
}

fn light_iterate(local: Option<Box<Light>>, result: &mut Vec<i32>) {
    match local {
        Some(i) => {
            result.push(i.brightness);

            light_iterate(i.left, result);
            light_iterate(i.right, result);
        },
        None => return
    }
}

fn main() {
    let instructions = get_instructions_from_stdin();
    let mut light = Box::from(Light { left: None, right: None, brightness: 0 });
    let mut local = &mut light;

    for i in instructions {
        match i {
            Instruction::Set(brightness) => local.brightness = brightness,
            Instruction::Left => local = local.left.get_or_insert_with(|| Box::new(Light { left: None, right: None, brightness: 0 })),
            Instruction::Right => local = local.right.get_or_insert_with(|| Box::new(Light { left: None, right: None, brightness: 0 })),
            Instruction::Reset => local = &mut light
        }
    }

    let mut result: Vec<i32> = vec![];
    light_iterate(Some(light), &mut result);
    println!("{}", result.iter().sum::<i32>() / result.len() as i32)
}
