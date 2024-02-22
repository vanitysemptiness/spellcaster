

pub mod BubbleCache{
    pub struct Cache {
        bubbles: HashSet<Bubble>,
        topics: HashSet<String>,
    }
    
    impl Cache {
    
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
    
        fn add_topic(&mut self, topic: String) {
            self.topics.insert(topic);
        }
    
        fn get_bubbles(&self) -> &HashSet<Bubble> {
            &self.bubbles
        }
    
        fn get_topics(&self) -> &HashSet<String> {
            &self.topics
        }
    }

    #[cfg(test)]
    mod tests {
        use super::BubbleCache::Cache;
        use super::BubbleCache::Bubble; // Import Bubble type if not already imported
        use std::collections::HashSet;

        #[derive(Debug, PartialEq, Eq, Hash)] // Assuming Bubble has these traits
        struct Bubble {
            // Define fields for Bubble
        }

        #[test]
        fn test_new_cache() {
            let cache = Cache::new();
            assert!(cache.get_bubbles().is_empty());
            assert!(cache.get_topics().is_empty());
        }

        #[test]
        fn test_add_bubble() {
            let mut cache = Cache::new();
            let bubble = Bubble {
                // Create a Bubble instance for testing
            };

            cache.add_bubble(bubble.clone());

            assert_eq!(cache.get_bubbles(), &hashset![bubble]);
            assert!(cache.get_topics().is_empty());
        }

        #[test]
        fn test_add_topic() {
            let mut cache = Cache::new();
            let topic = String::from("example_topic");

            cache.add_topic(topic.clone());

            assert!(cache.get_bubbles().is_empty());
            assert_eq!(cache.get_topics(), &hashset![topic]);
        }

        // Additional tests for other methods...

        // You can add more tests to cover other methods like get_bubbles, get_topics, etc.
    }

}