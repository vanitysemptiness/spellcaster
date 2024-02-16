import bubble_parser as bp

class ReservedBubbles:
    COMMAND_SEPARATOR = '::'
    SAVE = 'save'
    LIST = 'list'

class Bubble:
    
    def __init__(self, raw_text: str, cleaned_text: str, commands: list):
        self.raw_text: str = raw_text
        self.cleaned_text: str = cleaned_text
        self.commands: list = commands
        
class Suds:
    '''
    an unprocessed bubble
    it may contain reserved commands like save
    
    '''
    
    def __init__(self, raw_text: str):
        self.raw_text: str = raw_text
        
    def clean(self, raw_text: str):
        '''
        "A new bubble"
        "tide:: A new Bubble"
        Save:: tide:: a new Bubble
        Save:: tide::
        The user can either give a fixed command
            or do a tide shift
        Tide shifts are expected to happen all the time
        Maybe a hashtag should indicate a tide shift
        
        Can be used like Suds(text).clean() will create a Bubble
        '''
        ls: list = raw_text.split(ReservedBubbles.COMMAND_SEPARATOR)
        cleaned_text: str = bp.extract_bubble_text(ls)
        commands: list = bp.extract_commands(ls) # the Bubble should be the last one
        return Bubble(raw_text, cleaned_text, commands)
        
        