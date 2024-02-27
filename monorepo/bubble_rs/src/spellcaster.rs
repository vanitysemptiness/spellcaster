use std::io::{self, Write};
use std::collections::{HashSet, HashMap};

#[derive(Debug, Eq, PartialEq, Hash)]
struct Bubble {
    topic: String,
    text: String,
}

impl Bubble {
    // Constructor method for creating a new Bubble
    fn new(topic: &str, text: &str) -> Self {
        Bubble {
            topic: topic.to_string(),
            text: text.to_string(),
        }
    }
}

#[derive(Debug)]
struct Bubbles {
    content: HashMap<String, Vec<Bubble>>,
}

impl Bubbles {
    // Constructor method for creating a new Bubbles
    fn new() -> Self {
        Bubbles {
            content: HashMap::new(),
        }
    }

    // Add a Bubble to the Bubbles content
    fn add_bubble(&mut self, bubble: Bubble) {
        self.content
            .entry(bubble.topic.clone())
            .or_insert_with(Vec::new)
            .push(bubble);
    }

    // Print the Bubbles in the desired format
    fn print_bubbles(&self) {
        for (topic, bubbles) in &self.content {
            println!("Topic: {}", topic);
            for bubble in bubbles {
                println!("Text: {}", bubble.text);
            }
            println!(); // Separate topics
        }
    }
}

fn parse_bubble(bubbles: &mut Bubbles, input: &str) {
    // Split the input on ":"
    let parts: Vec<&str> = input.split(':').map(|s| s.trim()).collect();

    // Check if the input has at least two parts
    if parts.len() >= 2 {
        let topic = parts[0];
        let text = parts[1];

        // Create a new Bubble and add it to the HashSet
        let new_bubble = Bubble::new(topic, text);
        bubbles.add_bubble(new_bubble);
    } else {
        println!("Invalid input: {}", input);
    }
}
/*
   Spellcaster CLI: A simple command-line interface for spellcasting.

   This CLI continuously prompts the user to enter a spell or command. The user's input
   is then processed, and the corresponding spell or action is executed. The loop
   continues until the user decides to exit by entering "exit".
*/
fn main() {
    // global repo for bubbles
    let mut bubbles: Bubbles = Bubbles::new();
    loop {
        // Print a prompt
        print!("✨ ");
        io::stdout().flush().unwrap(); // Ensure the prompt is displayed

        // Read user input
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");

        // Trim newline characters from the input
        let input = input.trim();

        // Check if the user wants to exit
        if input.eq_ignore_ascii_case("exit") {
            println!("Exiting the Spellcaster CLI.");
            break;
        }

        // Process the spell or command
        parse_bubble(&mut bubbles, input);
        println!("Bubbles: {:#?}", bubbles);
    }
}
