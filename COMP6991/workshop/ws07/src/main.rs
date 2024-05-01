use rand::Rng;
use std::cmp::Eq;
use std::collections::HashSet;
use std::hash::Hash;

#[allow(dead_code)]
enum TaskResult {
    Finished(HashSet<Prerequisites>),
    RunMeAgain,
}

/// This is a particular task that needs to be run.
///
/// A task has "prerequisites" -- it can't run until
/// they have happened.
struct Task<'a> {
    prerequisites: HashSet<Prerequisites>,
    task: Box<dyn FnMut() -> TaskResult + 'a>,
}

/// This contains all the tasks, and also all the prerequisites
/// that have already happened.
struct Scheduler<'a> {
    tasks: Vec<Task<'a>>,
    prerequisites: HashSet<Prerequisites>,
}

impl<'a> Scheduler<'a> {
    fn start(mut self) {
        let mut rng = rand::thread_rng();
        loop {
            if self.tasks.is_empty() {
                break;
            }
            let random_index = rng.gen_range(0..self.tasks.len());
            if self.tasks[random_index]
                .prerequisites
                .is_subset(&self.prerequisites)
            {
                let mut task = self.tasks.swap_remove(random_index);
                let task_result = (task.task)();
                match task_result {
                    TaskResult::Finished(new_prerequisites) => {
                        self.prerequisites.extend(new_prerequisites.into_iter());
                    }
                    TaskResult::RunMeAgain => {
                        self.tasks.push(task);
                    }
                }
            }
        }
    }

    fn add_task(&mut self, task: Task<'a>) {
        self.tasks.push(task);
    }

    fn new() -> Self {
        Self {
            tasks: vec![],
            prerequisites: HashSet::new(),
        }
    }
}

/// This is a list of every "event" that can happen in our
/// scheduler system.
#[derive(PartialEq, Eq, Hash)]
enum Prerequisites {
    CleanedTestFile,
    CleanedCargo,
    CargoBuiltPrintRandoms,
    CargoBuiltProgramRunner,
    WrittenRandoms,
}

/// Tasks should happen in this order:
///
/// Clean Cargo  -> Wait until cargo is clean -> Build PrintRandoms -> Wait until it's built.  -> Run PrintRandoms with ProgramRunner
///                                          \                                                 |
///                                           -> Build ProgramRunner -> Wait until it's built -|
///                                                                                            |
/// Clean Test File --------------------------------------------------------------------------/
use std::process::{Command, Stdio};

fn run_command(command: &[&str]) {
    Command::new(command[0])
        .args(&command[1..])
        .stdout(Stdio::piped())
        .spawn()
        .unwrap()
        // If only we could use try_wait() here.
        .wait()
        .unwrap();
}

fn main() {
    //
    let mut scheduler = Scheduler::new();

    // Add the task to clean cargo. Doesn't require anything,
    // and once we've done it, we've started the clean command.
    scheduler.add_task(Task {
        prerequisites: HashSet::new(),
        task: Box::new(|| {
            println!("Cleaning cargo.");
            run_command(&["cargo", "clean"]);
            TaskResult::Finished(HashSet::from([Prerequisites::CleanedCargo]))
        }),
    });

    // Build the print_randoms binary
    scheduler.add_task(Task {
        prerequisites: HashSet::from([Prerequisites::CleanedCargo]),
        task: Box::new(|| {
            println!("Building print_randoms.");
            run_command(&["cargo", "build", "--bin", "print_randoms"]);
            TaskResult::Finished(HashSet::from([Prerequisites::CargoBuiltPrintRandoms]))
        }),
    });

    // Build the program_runner binary
    scheduler.add_task(Task {
        prerequisites: HashSet::from([Prerequisites::CleanedCargo]),
        task: Box::new(|| {
            println!("Building program_runner");
            run_command(&["cargo", "build", "--bin", "program_runner"]);
            TaskResult::Finished(HashSet::from([Prerequisites::CargoBuiltProgramRunner]))
        }),
    });

    // Run the program_runner binary
    scheduler.add_task(Task {
        prerequisites: HashSet::from([
            Prerequisites::CleanedTestFile,
            Prerequisites::CargoBuiltPrintRandoms,
            Prerequisites::CargoBuiltProgramRunner,
        ]),
        task: Box::new(|| {
            println!("Running program_runner.");
            run_command(&[
                "cargo",
                "run",
                "--bin",
                "program_runner",
                "randoms",
                "cargo",
                "run",
                "--bin",
                "print_randoms",
            ]);
            TaskResult::Finished(HashSet::from([Prerequisites::WrittenRandoms]))
        }),
    });

    // We also want to make sure there isn't a file called
    // "randoms"
    scheduler.add_task(Task {
        prerequisites: HashSet::new(),
        task: Box::new(|| {
            println!("Removing randoms.");
            run_command(&["rm", "-f", "randoms"]);
            TaskResult::Finished(HashSet::from([Prerequisites::CleanedTestFile]))
        }),
    });

    scheduler.start();
}
