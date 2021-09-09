#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

from pycorenlp import StanfordCoreNLP
import re


from models.Sentence import Sentence
from controllers.TextCleanController import TextCleanController

class CFGController:
    """Generates the context free grammer (CFG) syntax parse tree.
    """
    def __init__(self):
        self.nlp = StanfordCoreNLP('http://localhost:9000')
        
    def setSentenceType(self, sentence):
        """Add a tag Code if the sentence is not a english language sentence
        Parameters
        ----------
        sentence : object
            Sentence
        """
        # clean the sentence
        #tcc = TextCleanController()
        #sentence.set_cleaned_text(tcc.clean_sentence(sentence.get_text(), r_digit=False, r_punc=False))
        
        output = self.nlp.annotate(sentence.get_text(), properties = {
            'annotators': 'tokenize, ssplit, pos, depparse, parse',
            'outputFormat': 'json'
        })
        
        spt_string = output['sentences'][0]['parse']
        
        # sanity check
        print(spt_string)
        
        # the pattern capture node S at root level or branch level
        eng_pattern = r'^\(ROOT\n.*\(S\b|.*\n.*\(S\b'
        # the pattern captuer node S at root level
        # eng_pattern = r'^\(ROOT\n.*\(S\b.*'

        if re.search(eng_pattern, spt_string):
            pass
        else:
            if 'Code' not in sentence.get_tags():
                sentence.add_a_tag('Code')
        
    
    