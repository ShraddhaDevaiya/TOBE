#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import re

from models.Sentence import Sentence
from controllers.TextCleanController import TextCleanController

class URLController:
    """Capture sentences contain URL(s)
    """
    
    def __init__(self):
        patterns = [
            r'.*https?://.+', r'.*ftp://.+'
        ]

        self.all_patterns = re.compile('|'.join(pat for pat in patterns))
    
    def findURL(self, sentence):
        """Find sentences that contain URL(s) and add a tag URL
        Parameters
        ----------
        sentences : obj
            Sentence object
        """
        tcc = TextCleanController()
        
        sentence.set_cleaned_text(tcc.clean_sentence(sentence.get_text(), r_digit=False, r_punc=False))
        
        if self.all_patterns.search(sentence.get_text()) is not None:
            if 'URL' not in sentence.get_tags():
                sentence.add_a_tag('URL')