#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import re
import os
import pickle

from models.Sentence import Sentence
# from controllers.TextCleanController import TextCleanController

class SyntaxController:
    """Capture syntax in a sentence
    """
    def __init__(self):
        curr_dir = os.getcwd()
        pattern_file_path = os.path.join(curr_dir, "data", "regex3.txt")
        
        patterns = list()
        with open(pattern_file_path) as f:
            patterns = [line.rstrip() for line in f]
            
        self.all_patterns = re.compile('|'.join(pat for pat in patterns))

        curr_dir = os.getcwd()
        model_path = os.path.join(curr_dir, 'data', 'svm_c.sav')
        tfidfvect_path = os.path.join(curr_dir, 'data', 'tfidf_c.sav')
        
        with open(model_path, 'rb') as file:
            self.svm_model = pickle.load(file)
            
        with open(tfidfvect_path, 'rb') as file:
            self.tfidf_vect = pickle.load(file)
    
    def findSyntax(self, sentence):
        """Find sentences that contain codes and add a tag Code
        Parameters
        ----------
        sentences : obj
            Sentence object
        """
        
        if 'URL' not in sentence.get_tags():
            if not re.match(r'.*Created an attachment \(.+\).*', sentence.get_text()):
                if self.all_patterns.search(sentence.get_text()):
                    if 'Code' not in sentence.get_tags():
                        sentence.add_a_tag('Code')
            

    def findSyntaxSupervised(self, sentence):

        #Since transform expects a iterable object make sure to change str to a list
        input_list = list()
        input_list.append(sentence.get_text())
        
        sent_tfidf = self.tfidf_vect.transform(input_list)
        
        pred = self.svm_model.predict(sent_tfidf)
        
        if pred[0] == 0:
            if 'code' not in sentence.get_tags():
                sentence.add_a_tag('Code')
        