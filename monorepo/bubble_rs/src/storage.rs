

mod storage {
    use std::collections::HashSet;
    use std::fs::{File, OpenOptions};
    use std::io::{self, Read, Write};
    use serde::de::DeserializeOwned;
    use serde::Serialize;

    /// Reads data of a generic type that implements the `DeserializeOwned` trait from a JSON file
    /// and returns a `HashSet<T>`.
    fn read_from_file<T>(file_path: &str) -> io::Result<HashSet<T>>
    where
        T: DeserializeOwned + Eq + std::hash::Hash,
    {
        let mut file = File::open(file_path)?;
        let mut json_data = String::new();
        file.read_to_string(&mut json_data)?;
        let elements: Vec<T> = serde_json::from_str(&json_data)?;
        Ok(elements.into_iter().collect())
    }

    /// Saves data of a generic type that implements the `Serialize` trait to a JSON file.
    pub fn save_to_file<T>(data: &HashSet<T>, file_path: &str) -> io::Result<()>
    where
        T: Serialize,
    {
        let mut file = OpenOptions::new()
            .write(true)
            .truncate(true)
            .create(true)
            .open(file_path)?;

        let json_data = serde_json::to_string(data)?;
        file.write_all(json_data.as_bytes())?;

        Ok(())
    }


    #[cfg(test)]
    mod tests {

        use super::*;

        use crate::bubble_model::bubble_model::Bubble;

        use tempfile::tempdir;

        #[test]
        fn test_save_and_read_bubbles() {
            // Arrange
            let temp_dir = tempdir().expect("Failed to create temporary directory");
            let file_path = temp_dir.path().join("bubbles.json");
            let text: String = String::from("text");
            let topics: Vec<String> = vec![String::from("topic")];
            let bubble: Bubble = Bubble::new(&text, topics);
            let mut bubbles: HashSet<Bubble> = HashSet::new();
            bubbles.insert(bubble);
            let file_path_str: String = String::from(file_path.to_str().unwrap_or_default());
            // Act
            // Save the HashSet<Bubble> to a file
            assert!(super::save_to_file(&bubbles, &file_path_str).is_ok());

            // Read the HashSet<Bubble> back from the file
            let read_bubbles_set: HashSet<Bubble> = super::read_from_file(&file_path.to_str().unwrap_or_default()).expect("Failed to read bubbles from file");

            // Assert
            assert_eq!(bubbles, read_bubbles_set);

            // Cleanup
            drop(temp_dir);  // Automatically cleans up the temporary directory and its contents
        }

        #[test]
        fn test_save_and_read_strings() {
            // Arrange
            let temp_dir = tempdir().expect("Failed to create temporary directory");
            let file_path = temp_dir.path().join("strings.json");

            let strings_set: HashSet<String> = vec!["apple".to_string(), 
            "banana".to_string(), "cherry".to_string()].into_iter().collect();

            let file_path_str: String = String::from(file_path.to_str().unwrap_or_default());
            // Act
            // Save the HashSet<String> to a file
            assert!(super::save_to_file(&strings_set, &file_path_str).is_ok());

            // Read the HashSet<String> back from the file
            let read_strings_set: HashSet<String> = super::read_from_file(&file_path_str).expect("Failed to read strings from file");

            // Assert
            assert_eq!(strings_set, read_strings_set);

            // Cleanup
            drop(temp_dir);  // Automatically cleans up the temporary directory and its contents
        }
    }
}