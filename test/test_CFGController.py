#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import unittest

from models.Sentence import Sentence
from controllers.CFGController import CFGController

class TestCFGController(unittest.TestCase):
    def test_setSentenceType(self):
        cfg = CFGController()
        text = Sentence('1.1', 'The simple fix is to just discard the services')
        cfg.setSentenceType(text)
        self.assertTrue('Code' not in text.get_tags())

        cfg = CFGController()
        text = Sentence('1.1', 'Feel free to open a new bug if there is something I missed.')
        cfg.setSentenceType(text)
        self.assertTrue('Coce' not in text.get_tags())
        
        
        text = Sentence('1.1', 'public static void main(String ar[])')
        cfg.setSentenceType(text)
        self.assertTrue('Code' in text.get_tags())
        
        text = Sentence('1.1', 'x-webobjects-server-protocol: HTTP/1.1')
        cfg.setSentenceType(text)
        self.assertTrue('Code' in text.get_tags())
        
        text = Sentence('1.1', 'Seamonkey:   http://www.mozilla.org/projects/seamonkey/')
        cfg.setSentenceType(text)
        self.assertTrue('Code' in text.get_tags())
        
        text = Sentence('1.1', 'http://hg.mozilla.org/comm-central/rev/2f6ef8daa83e')
        cfg.setSentenceType(text)
        self.assertTrue('Code' in text.get_tags())
        
        text = Sentence('1.1', '4. erase the calendar from your server')
        cfg.setSentenceType(text)
        self.assertTrue('Code' not in text.get_tags())
        
        text = Sentence('1.9', ' Perhaps we should rename one of them to _fhResult just to reduce confusion?')
        cfg.setSentenceType(text)
        self.assertTrue('Code' not in text.get_tags())
        
        text = Sentence('1.1', 'Then the loop continues with a new propfind...')
        cfg.setSentenceType(text)
        self.assertTrue('Code' not in text.get_tags())
        
        text = Sentence('1.9', '&amp;gt; Perhaps we should rename one of them to _fhResult just to reduce confusion?')
        cfg.setSentenceType(text)
        self.assertTrue('Code' not in text.get_tags())
        
        # exception: Stanford Core NLP parser didn't detect these as English sentence or their root element is not S
        text = Sentence('1.1', '5. relaunch Thunderbird')
        cfg.setSentenceType(text)
        self.assertTrue('Code' in text.get_tags())
        
        text = Sentence('1.1', 'Actual results:')
        cfg.setSentenceType(text)
        self.assertTrue('Code' in text.get_tags())
        
        # When two sentences are parsed if the first one is not a complete sentence
        # the program doesn't consider the second sentence even if it is a complete sentence
        text = Sentence('1.1', 'Fair point. I\'m not sure')
        cfg.setSentenceType(text)
        self.assertTrue('Code' in text.get_tags())
        
        
if __name__ == "__main__":
    unittest.main()