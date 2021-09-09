#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import re

from models.Sentence import Sentence
from controllers.TextCleanController import TextCleanController

class RSFController:
    """Filter sentences represent bug report resolution state. (Eg: based on keywords such as fix, push, patch, attachment)
    """
    
    def __init__(self):
        pass
    
    def findRSComments(self,sentence):
        """If a sentence related to a bug resolution add a RES tag to the tag list
        Parameters
        ----------
        sentence : obj
            Sentence object
        """
        tcc = TextCleanController()
        
        sentence.set_cleaned_text(tcc.clean_sentence(sentence.get_text(), r_digit=False, r_punc=False))
        
        sent = sentence.get_cleaned_text()
        if 'push' in sent:
            if re.match(r'^push.*', sent) or re.match(r'^((\S)+\s)+push(.*)?', sent):
                if 'RES' not in sentence.get_tags():
                    sentence.add_a_tag('RES')
        if 'attach' in sent:
            if re.match(r'^((\S)+\s)+attach.*', sent):
                if 'RES' not in sentence.get_tags():
                    sentence.add_a_tag('RES')
        if 'patch' in sent:
            if re.match(r'^patch.*', sent) or re.match(r'^((\S)+\s)+patch(.*)?', sent):
                if 'RES' not in sentence.get_tags():
                    sentence.add_a_tag('RES')
        if 'commit' in sent:
            if re.match(r'^commit.*', sent) or re.match(r'^((\S)+\s)+commit(.*)?', sent):
                if 'RES' not in sentence.get_tags():
                    sentence.add_a_tag('RES')
        if 'fix' in sent:
            if re.match(r'^\bfix\b.*', sent) or re.match(r'^((\S)+\s)+\bfix\b(.*)?', sent):
                if 'RES' not in sentence.get_tags():
                    sentence.add_a_tag('RES')