import tkinter as tk

class WordBubbleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Bubbles")

        # Create a canvas
        self.canvas = tk.Canvas(self.root, bg="#3366FF", width=600, height=400)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Sentence to be displayed
        sentence = "Tkinter is a powerful GUI toolkit for Python."

        # Create word bubbles for each word in the sentence
        self.create_word_bubbles(sentence)

        # Create a text box in the center
        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack(side=tk.BOTTOM, pady=10)
        self.text_entry.bind("<Return>", self.create_word_bubbles_from_input)

    def create_word_bubbles(self, sentence):
        # Split the sentence into words
        words = sentence.split()

        # Initialize coordinates for word bubbles
        x, y = 50, 50

        # Create word bubbles for each word
        for word in words:
            # Create a blue rounded box for each word
            box = tk.Label(self.canvas, text=word, bg="#3366FF", fg="white", padx=10, pady=5, relief=tk.RIDGE, bd=2)
            box_width = box.winfo_reqwidth()
            box_height = box.winfo_reqheight()

            # Place the box on the canvas
            self.canvas.create_window(x, y, anchor=tk.NW, window=box)

            # Update coordinates for the next word
            x += box_width + 10  # Add a small buffer
            if x + box_width > self.canvas.winfo_width() - 50:
                x = 50
                y += box_height + 10  # Add a small buffer

    def create_word_bubbles_from_input(self, event):
        # Get text from the text box
        sentence = self.text_entry.get()

        # Clear the canvas 
        self.canvas.delete("all")

        # Recreate word bubbles for the new sentence
        self.create_word_bubbles(sentence)

        # Clear the text box
        self.text_entry.delete(0, tk.END)
        
    def enter(self, text):
        '''
        when entering we have to parse out what 
        can happen
        '''

if __name__ == "__main__":
    root = tk.Tk()
    app = WordBubbleApp(root)
    root.mainloop()
