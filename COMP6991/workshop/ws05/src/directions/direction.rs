#[derive(Debug, Clone)]
pub struct Direction {
    pub x: i32,
    pub y: i32,
}

#[derive(Debug, Clone)]
pub enum CardinalDirection {
    North,
    East,
    South,
    West,
}
