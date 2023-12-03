#!/usr/bin/env python

__author__ = 'Akalanka Galappaththi'
__email__ = 'a.galappaththi@uleth.ca'
__copyright__ = 'Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab'
__license__ = 'MIT'
__maintainer__ = 'Akalanka Galappaththi'

import pandas as pd
import os
import csv
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

from controllers.TextCleanController import TextCleanController



class OTFController:
    """Tag off-topic comments as OT.
    """
    
    def __init__(self):
        self.data1 = pd.read_csv("/home/shraddha/sh_work/sh_TOBE/TOBE/data/12_2_human.csv", engine="python")
        self.i = 0
        curr_dir = os.getcwd()
        #model_path = os.path.join(curr_dir, 'data', 'yt_git_tfidf_naive.sav')
        #tfidfvect_path = os.path.join(curr_dir, 'data', 'yt_git_tfidf.sav')
        '''
        model_path = os.path.join(curr_dir, 'data', 'man_try1_ot_naive.sav')
        tfidfvect_path = os.path.join(curr_dir, 'data', 'man_try1_ot_tfidf.sav')
        
        with open(model_path, 'rb') as file:
            self.svm_model = pickle.load(file)
            
        with open(tfidfvect_path, 'rb') as file:
            self.tfidf_vect = pickle.load(file)
        '''
    
    def findOTComment(self, sentence, count):
        """Add a tag OT to the sentence if it is classified as off-topic
        Parameters
        ----------
        sentence : object
            Sentence object
        """
        #count = count + 1
        #self.i = self.i + 1
        #print("Sentence no. ",self.i)
        print("Sentence no. ",count)
        
        tcc = TextCleanController()
        sentence.set_cleaned_text(tcc.clean_sentence(sentence.get_text()))
        
        #Since transform expects a iterable object make sure to change str to a list
        input_list = list()
        input_list.append(sentence.get_text())
        '''
        
        sent_tfidf = self.tfidf_vect.transform(input_list)
        
        pred = self.svm_model.predict(sent_tfidf) 
        '''
        if self.data1['FINAL_OT'][count] == 1:
            print("SHDBG: OT label no. ", count)
            if 'OT' not in sentence.get_tags():
                sentence.add_a_tag('OT')
    
        #if pred[0] == 1:
        #    if 'OT' not in sentence.get_tags() and 'Code' not in sentence.get_tags():
        #        sentence.add_a_tag('OT')