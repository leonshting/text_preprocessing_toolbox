class BaseFilter:
    def __init__(self):
        pass

    def _populate_pattern(self, pattern):
        """embraces pattern with:
            1. beginning of string & end of string
            2. space & end of string
            3. beginning of string & space
            4. space & end of sentence
        """
        
