// DO NOT EDIT THIS FILE.
use std::iter::zip;
use q3_lib::{tuple_zip, tuple_unzip};

#[derive(Debug, PartialEq, Eq)]
struct Coordinate {
    x: i32,
    y: i32
}

impl From<(i32, i32)> for Coordinate {
    fn from(thing: (i32, i32)) -> Self {
        Coordinate {
            x: thing.0,
            y: thing.1
        }
    }
}

impl From<Coordinate> for (i32, i32) {
    fn from(thing: Coordinate) -> Self {
        (thing.x, thing.y)
    }
}

fn main() {
    let coords = vec![
        Coordinate {x: 0, y: 0},
        Coordinate {x: 7, y: -2}
    ];

    let (xs, ys) = tuple_unzip(coords);

    assert_eq!(xs, vec![0, 7]);
    assert_eq!(ys, vec![0, -2]);

    let coords: Vec<Coordinate> = tuple_zip((xs, ys));

    assert_eq!(
        coords,
        vec![
            Coordinate {x: 0, y: 0},
            Coordinate {x: 7, y: -2}
        ]
    )
}
