"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder():
    """ machine for finding random words from dictionary.
    >>> wf = WordFinder("words.txt")
    235886 words read
        

    >>> wf.random() in [w.strip() for w in open("words.txt")]
    True

    >>> wf.random() in [w.strip() for w in open("words.txt")]
    True

    >>> wf.random() in [w.strip() for w in open("words.txt")]
    True""" 

    
    def __init__(self, path):
        """Read dictionary and reports # items read."""
        words_file = open(path)
        self.words = self.parse(words_file)        
        print(f"{len(self.words)} words read")

    def parse(self, words_file):
        """Parse words_file -> list of words."""
        return [word.strip() for word in words_file]

    def random(self):
        """Return random word."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):

    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True"""

    def parse(self, words_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [word.strip() for word in words_file 
        if word.strip() and not word.startswith("#")]

        

            

    


