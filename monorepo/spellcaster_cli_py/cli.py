from collections import namedtuple
import datetime
from keyword_tagging import identify_important_words_tfidf

# Define a namedtuple to store notes with content and timestamp
Note = namedtuple("Note", ["content", "timestamp"])

def main():
  """
  Runs a simple CLI for taking notes.
  """
  print("Welcome to your note taker! ✨")
  notes = set()

  while True:
    print("Type your note (or 'q' to quit):")

    # Handle multi-line input using a flag
    is_multi_line = False
    note_content = ""

    while True:
      line = input("  ")

      # Check for multi-line input indicator, quit command, or backspace
      if line == ".":
        is_multi_line = True
        break
      elif line == "q":
        break
      elif line == "\b":
        # Handle backspace by removing the last character
        if note_content:
          note_content = note_content[:-1]
          print("\b \b", end="")  # Clear the last character and space
      else:
        note_content += line + "\n"

      # Print a newline indicator for multi-line input
      if is_multi_line:
        print("    ")

    if note_content:
      # Add note to the set with a timestamp
      notes.add(Note(note_content.strip(), datetime.datetime.now()))

    # Print all notes with timestamps
    if notes:
      print("\nRecent Spell:")
      for note in notes:
        print(f"- {note.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{note.content.strip()}")
        print(f"important words: {identify_important_words_tfidf(note_content)}")

    #loops infinitely, no way to escape

  print("\nExiting...")

if __name__ == "__main__":
  main()
