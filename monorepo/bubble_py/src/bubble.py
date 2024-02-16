

class ReservedBubbles:
    COMMAND_SEPARATOR = '::'
    SAVE = 'save'
    LIST = 'list'

class Bubble:
    
    def __init__(self, text: str):
        self.text: str = text
        self.cleaned_text = None
        self.commands = None
        
class Suds:
    '''
    an unprocessed bubble
    it may contain reserved commands like save
    
    '''
    
    def __init__(self, raw_text: str):
        self.raw_text: str = raw_text
        self.cleaned_bubble: Bubble = self.clean(self.raw_text)
        
    def clean(raw_text):
        '''
        "A new bubble"
        "tide:: A new Bubble"
        Save:: tide:: a new Bubble
        Save:: tide::
        The user can either give a fixed command
            or do a tide shift
        Tide shifts are expected to happen all the time
        Maybe a hashtag should indicate a tide shift
        '''
        ls = raw_text.split(ReservedBubbles.COMMAND_SEPARATOR)
        # the Bubble should be the last one