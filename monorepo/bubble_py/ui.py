import tkinter as tk

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("bubbles")

        # Set the default size of the window
        self.root.geometry("400x300")

        # Create a blue background
        self.background = tk.Canvas(self.root, bg="#3366FF", width=400, height=300)
        self.background.pack(expand=True, fill=tk.BOTH)

        # Create a frame to hold the bubbles
        self.bubble_frame = tk.Frame(self.background, bg="#3366FF")
        self.bubble_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Create a text box at the bottom
        self.text_entry = tk.Entry(self.bubble_frame, width=40)
        self.text_entry.pack(side=tk.LEFT, padx=10)
        self.text_entry.bind("<Return>", self.create_bubble)

    def create_bubble(self, event):
        # Get text from the text box
        text = self.text_entry.get()

        # Display the text in a blue bubble
        bubble_label = tk.Label(self.bubble_frame, text=text, bg="#3366FF", fg="white", padx=10, pady=5, relief=tk.RIDGE, bd=2)
        bubble_label.pack(side=tk.RIGHT, anchor=tk.E)

        # Clear the text box
        self.text_entry.delete(0, tk.END)