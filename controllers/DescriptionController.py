#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import re

from models.Turn import Turn
from models.Sentence import Sentence
from controllers.TextCleanController import TextCleanController
from controllers.CFGController import CFGController

class DescriptionController:
    """Detect steps to reproduce, actual and expected output in bug description.    
    """
    
    def __init__(self):
        pass
    
    def findBugDescription(self, turn, title):
        """Find sentences represent steps to reproduce, expecte and actual results
        Parameters
        ----------
        turn : object
            Turn object
        title : str
            Title of the bug report
        """
        tcc = TextCleanController()
        # cfg = CFGController()
        
        # flag to indicate steps to reproduce is found
        flag = False
        for sent in turn.get_sentences(): 
            
            # cfg.setSentenceType(sent)
            sent.set_cleaned_text(tcc.clean_sentence(sent.get_text(), r_punc=False, r_digit=False))
        
            if re.search(r'step.reproduce', sent.get_cleaned_text()) is not None or \
                re.search(r'actual results?', sent.get_cleaned_text()) is not None or \
                    re.search(r'expect results?', sent.get_cleaned_text()) is not None:
                        # if 'Code' in sent.get_tags():
                        #     sent.get_tags().remove('Code')
                        sent.add_a_tag('DES')
                        flag = True
               
            if flag:
                if re.match(r'^\d(\.|\))', sent.get_text()):
                    # if 'Code' in sent.get_tags():
                    #     sent.get_tags().remove('Code')
                    if 'DES' not in sent.get_tags():
                        sent.add_a_tag('DES')
                if 'DES' not in sent.get_tags():
                    sent.add_a_tag('DES')
                    # if 'OT' in sent.get_tags():
                    #     sent.get_tags().remove('OT')
                
            elif flag == False:
                
                title_words = set(tcc.clean_sentence(title, r_punc=True, r_digit=True, stop=True, lem=True).split())
                # print(title_words)
                sent.set_cleaned_text(tcc.clean_sentence(sent.get_text(), r_punc=True, r_digit=True, stop=True, lem=True))
                sent_words = set(sent.get_cleaned_text().split())
                # print(sent_words)
                for w in title_words:
                    if w in sent_words: 
                        if 'DES' not in sent.get_tags():
                            sent.add_a_tag('DES')
                            # if 'OT' in sent.get_tags():
                            #     sent.get_tags().remove('OT')
                            # if 'Code' in sent.get_tags():
                            #     sent.get_tags().remove('Code')
            
    
    