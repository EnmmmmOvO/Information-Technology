pub mod directions;

use crate::directions::{coordinate::Coordinate, direction::Direction};

use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};

use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize)]
struct Circle {
    cx: i32,
    cy: i32,
    r: i32,
    stroke: String,
    fill: String,
    #[serde(rename = "stroke-width")]
    stroke_width: i32,
}

#[derive(Clone)]
pub struct Planet {
    pub coordinate: Coordinate,
    pub weight: i32,
}

impl Planet {
    fn get_location(&self) -> Coordinate {
        self.coordinate.clone()
    }

    fn get_weight(&self) -> i32 {
        self.weight
    }

    fn as_circle(&self) -> Circle {
        Circle {
            cx: self.coordinate.x,
            cy: self.coordinate.y,
            r: self.weight,
            stroke: "green".to_string(),
            fill: "black".to_string(),
            stroke_width: 3,
        }
    }
}

#[derive(Clone)]
pub struct Asteroid {
    pub coordinate: Coordinate,
    pub velocity: Direction,
}

impl Asteroid {
    fn get_location(&self) -> Coordinate {
        self.coordinate.clone()
    }

    fn get_velocity(&self) -> Direction {
        self.velocity.clone()
    }

    fn as_circle(&self) -> Circle {
        Circle {
            cx: self.coordinate.x,
            cy: self.coordinate.y,
            r: 2,
            stroke: "green".to_string(),
            fill: "black".to_string(),
            stroke_width: 3,
        }
    }
}

#[derive(Clone)]
pub enum ObjectType {
    Planet(Planet),
    Asteroid(Asteroid),
}

impl ObjectType {
    fn get_circle(&self) -> Circle {
        match self {
            ObjectType::Planet(p) => p.as_circle(),
            ObjectType::Asteroid(a) => a.as_circle(),
        }
    }
}

fn get_distance(x1: i32, y1: i32, x2: i32, y2: i32) -> i32 {
    (((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) as f64).sqrt() as i32
}

fn apply_physics(mut objects: Vec<ObjectType>, gravitational_constant: i32) -> Vec<ObjectType> {
    // Go through each pair of objects, and apply
    let gravity_sources = objects
        .iter()
        .filter_map(|o| {
            return if let ObjectType::Planet(p) = o {
                Some((p.coordinate.clone(), p.weight))
            } else {
                None
            };
        })
        .collect::<Vec<_>>();

    objects.iter_mut().for_each(|o| {
        if let ObjectType::Asteroid(asteroid) = o {
            gravity_sources
                .iter()
                .for_each(|(planet_coord, planet_weight)| {
                    let distance = get_distance(
                        planet_coord.x,
                        planet_coord.y,
                        asteroid.coordinate.x,
                        asteroid.coordinate.y,
                    );
                    let distance = distance * distance;

                    let force = Direction {
                        x: (asteroid.coordinate.x - planet_coord.x)
                            * planet_weight
                            * gravitational_constant
                            / distance,
                        y: (asteroid.coordinate.y - planet_coord.y)
                            * planet_weight
                            * gravitational_constant
                            / distance,
                    };
                    asteroid.velocity.x -= force.x;
                    asteroid.velocity.y -= force.y;

                    let vel = asteroid.velocity.clone();
                })
        }
    });

    // Apply the new velocity to each object.
    objects.iter_mut().for_each(|object| {
        if let ObjectType::Asteroid(asteroid) = object {
            asteroid.coordinate.x += asteroid.velocity.x;
            asteroid.coordinate.y += asteroid.velocity.y;
        }
    });

    objects
}

fn handle_connection(
    mut stream: TcpStream,
    mut objects: Vec<ObjectType>,
    gravitational_constant: i32,
) -> Vec<ObjectType> {
    objects = apply_physics(objects, gravitational_constant);

    let circles = objects.iter().map(|o| o.get_circle()).collect::<Vec<_>>();
    let contents = serde_json::to_string(&circles).unwrap();
    let status_line = "HTTP/1.1 200 OK";
    let response = format!(
        "{status_line}\r\nContentType: application/json\r\nAccess-Control-Allow-Origin: *\r\n\r\n{contents}\r\n"
    );
    stream.write_all(response.as_bytes()).unwrap();
    stream.flush().unwrap();
    stream.shutdown(std::net::Shutdown::Both).unwrap();

    objects
}

pub fn start_server(uri: &str, mut objects: Vec<ObjectType>, gravitational_constant: i32) -> ! {
    let listener = TcpListener::bind(uri).unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        objects = handle_connection(stream, objects, gravitational_constant);
    }

    unreachable!()
}
