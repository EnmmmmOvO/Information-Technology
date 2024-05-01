use std::default::Default;
use std::ops::Add;
use std::convert::From;
use crate::direction::Direction;

/// Represent a 2D coordinate.
pub struct Coordinate {
    pub x: i32,
    pub y: i32
}

impl Coordinate {
    /// Create a new coordinate.
    fn new(x: i32, y: i32) -> Coordinate {
        Coordinate {x, y}
    }
}

impl Default for Coordinate {
    fn default() -> Self {
        Coordinate { x: 0, y: 0}
    }
}

impl Add for Coordinate {
    type Output = Coordinate;

    fn add(self, rhs: Coordinate) -> Self::Output {
        Coordinate { x: self.x + rhs.x, y: self.y + rhs.y}
    }
}

impl Add<Direction> for Coordinate {
    type Output = Coordinate;

    fn add(self, rhs: Direction) -> Self::Output {
        Coordinate { x: self.x + rhs.x, y: self.y + rhs.y}
    }
}

impl From<Direction> for Coordinate {
    fn from(dir: Direction) -> Coordinate {
        Coordinate { x: dir.x, y: dir.y }
    }
}
