const ENROLMENTS_PATH: &str = "enrolments.psv";

use std::collections::HashMap;
use csv::ReaderBuilder;

fn main() {
    let mut record = match ReaderBuilder::new().delimiter(b'|').has_headers(false).from_path(ENROLMENTS_PATH) {
        Ok(r) => r,
        Err(e) => {
            eprintln!("{e:?}");
            return;
        }
    };

    let mut student: HashMap<String, Vec<f64>> = HashMap::new();
    let mut course: HashMap<String, i32> = HashMap::new();

    record.records().for_each(|record_result| {
        match record_result {
            Ok(result) => {

                let wam = match result.get(5) {
                    Some(wam_str) => match wam_str.parse::<f64>() {
                        Ok(wam) => wam,
                        Err(e) => {
                            eprintln!("Failed to parse WAM: {}", e);
                            return;
                        }
                    },
                    None => {
                        eprintln!("Missing WAM in record.");
                        return;
                    }
                };

                let code = match result.get(1) {
                    Some(code) => code.to_string(),
                    None => {
                        eprintln!("Missing course code in record.");
                        return;
                    }
                };

                student.entry(code).or_insert(Vec::new()).push(wam);

                if let Some(course_name) = result.get(0) {
                    *course.entry(course_name.to_string()).or_insert(0) += 1;
                } else {
                    eprintln!("Missing course name in record.");
                    return;
                }
            },
            Err(e) => {
                eprintln!("Failed to read record: {}", e);
                return;
            },
        }
    });

    println!("Number of students: {}", student.len());
    match course.iter().max_by(|x, y| x.1.cmp(y.1)) {
        Some (result) => println!("Most common course: {} with {} students", result.0, result.1),
        None => {
            eprintln!("Failed to find most common course");
            return;
        },
    }
    match course.iter().min_by(|x, y| x.1.cmp(y.1)) {
        Some (result) => println!("Least common course: {} with {} students", result.0, result.1),
        None => {
            eprintln!("Failed to find least common course");
            return;
        },
    }

    println!("Average WAM: {:.2}", student.iter()
        .map(|(_k, v)| v.iter().sum::<f64>() / v.len() as f64)
        .into_iter().sum::<f64>() / student.len() as f64);
}
