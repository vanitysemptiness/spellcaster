import unittest
from src.bubble import DirtyBubble, Bubble

class BubbleTest(unittest.TestCase): 
    
    def create_bubble(self):
        quote = "quote:: those who know do not speak. Those who speak do not know -lau tsu"
        cleaned_quote = "those who know do not speak. Those who speak do not know -lau tsu"
        dirty = DirtyBubble(quote)
        self.assertEqual(dirty.raw_text, quote)
        bubble: Bubble = dirty.clean()
        self.assertIsNotNone(bubble.raw_text) # raw text populated
        self.assertEqual(bubble.cleaned_text, cleaned_quote)
        self.assertEqual(len(bubble.commands), 1)
        self.assertEqual(bubble.commands[0], 'quote')
        
if __name__ == '__main__':
    unittest.main()