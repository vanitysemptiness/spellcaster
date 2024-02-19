

use std::collections::HashSet;

#[warn(dead_code)]
mod bubble {

    const TOPIC_SEPARATOR: &str = "::";

    struct Bubble {
        text: String,
        topics: Vec<String>
    }

    impl Bubble {
        fn new(text: &str, topics: Vec<String>) -> Bubble {
            Bubble {
                text: text.to_string(),
                topics,
            }
        }
    }

    pub struct DirtyBubble {
        raw: String,
    }

    #[allow(private_interfaces)]
    impl DirtyBubble {
        // Constructor method to create a new DirtyBubble instance
        pub fn new(raw: &str) -> DirtyBubble {
            DirtyBubble { raw: String::from(raw) }
        }

        // Clean method that splits the input string on "::" and trims whitespace
        pub fn clean(&self) -> Bubble {
            let mut topics: Vec<String> = self.raw
                .split(TOPIC_SEPARATOR)
                .map(|s| s.trim().to_string())
                .collect();
            let text: String = topics.pop().unwrap_or_default();
            let bubble: Bubble = Bubble::new(&text, topics);
            bubble
        }
    }

    pub struct Ocean {
        bubbles: HashSet<Bubble>,
        topics: HashSet<String>,
    }

    impl Ocean {

        const SAVE: &str = "save";

        fn new() -> Ocean {
            Ocean {
                bubbles: HashSet::new(),
                topics: HashSet::new(),
            }
        }
    
        fn add_bubble(&mut self, bubble: Bubble) {
            self.bubbles.insert(bubble);
        }
    
        fn add_topic(&mut self, topic: Topic) {
            self.topics.insert(topic);
        }
    
        fn get_bubbles(&self) -> &HashSet<Bubble> {
            &self.bubbles
        }
    
        fn get_topics(&self) -> &HashSet<Topic> {
            &self.topics
        }
    }

    // unit tests
    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn test_create_bubble() {
            // Arrange
            let text = "This is a bubble";
            let topics = vec![
                "Rust".to_string(),
                "Testing".to_string(),
            ];

            // Act
            let bubble = Bubble::new(&text, topics.clone());

            // Assert
            assert_eq!(bubble.text, text);
            assert_eq!(bubble.topics, topics);
        }

        #[test]
        fn create_dirty_bubble() {
            let text: String = String::from("quote:: those who know do not speak. those who speak do not know -lau tsu");
            let dirty: DirtyBubble = DirtyBubble::new(&text);
            let bubble: Bubble = dirty.clean();
            let expected_text: String = String::from("those who know do not speak. those who speak do not know -lau tsu");
            assert_eq!(expected_text, bubble.text);
            assert_eq!(1, bubble.topics.len());
            assert_eq!(String::from("quote"), bubble.topics[0])
        }

        #[test]
        fn create_dirty_bubble_multiple_topics() {
            let text: String = String::from("reflection:: philosopy:: quote:: those who know do not speak. those who speak do not know -lau tsu");
            let dirty: DirtyBubble = DirtyBubble::new(&text);
            let bubble: Bubble = dirty.clean();
            let expected_text: String = String::from("those who know do not speak. those who speak do not know -lau tsu");
            assert_eq!(expected_text, bubble.text);
            assert_eq!(3, bubble.topics.len());
            assert_eq!(String::from("reflection"), bubble.topics[0]);
            assert_eq!(String::from("philosopy"), bubble.topics[1]);
            assert_eq!(String::from("quote"), bubble.topics[2]);
        }
    }
}



