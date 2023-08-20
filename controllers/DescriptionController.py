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
        
            if re.search(r'occurs|not found|Not found|not available error|error report|404 error|Exception|due to the fact|due to signal|becomes null|I attached|as a result|After installation|after.*installation|After disabling|appears after|after selecting|currently|Currently|sometimes|when I try|when I open|when I log|when trying|stop trying|entries|tries|Entries|no longer exists|wrong|did not respond|will not be|fails to load|it crashes|crash report|see crashes|crashed|the cause|instead of|Instead of|Keep-Alive|keep-alive|keeping track|allow me|allows to|some problems|still problematic|given this problem|have this problem|problem:|is the problem|but problem|would be displayed|would help\.|would do|would not be|would be worth|would be handy|would be available|would expect|would simply|would like that|would like your|would migrate|wanted to complete|want to create|want to remove|want to make|want to do|want to be able|normallt selects|may require|be required|I required|must not|must check|must also|it seems that|instead of it being|instead of adding|was expecting|Can we|was able to|should be able to|want to be able to|still be able to|correct/?|work correctly|correct|but sees that|but this|but my|but I didn\'t|but has|but maybe|but then|but I|but it|but after|but problem|but rules|but never|but multiple|but not|than before|before I would|According to|Expected .esults|expected\|Actual .esults?|teps to..eproduce|reproduce', sent.get_cleaned_text()) is not None:
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
            
    
    