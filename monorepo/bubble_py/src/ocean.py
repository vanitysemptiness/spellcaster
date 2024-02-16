import pickle

class Ocean:
    
    def __init__(self):
        self.bubbles = set()
        self.tides = set()
        self.BUBBLES_PATH = 'resources/bubbles.pkl'
        self.TIDES_PATH = 'resources/tides.pkl'
    
    def save(self):
        '''
        write bubbles and tides to 
        a bubbles.pkl and tides.pkl
        '''
        # Writing the set to a pickle file
        with open(self.BUBB, 'wb') as file:
            pickle.dump(self.BUBBLES_PATH, file, protocol=pickle.HIGHEST_PROTOCOL)
        with open('resources/tides.pkl', 'wb') as file:
            pickle.dump(self.TIDES_PATH, file, protocol=pickle.HIGHEST_PROTOCOL)
            
    def load(self):
        # Reading the set back from the pickle file
        with open(self.BUBBLES_PATH, 'rb') as file:
            self.bubbles = pickle.load(file)
        with open(self.TIDES_PATH, 'rb') as file:
            self.tides = pickle.load(file)


