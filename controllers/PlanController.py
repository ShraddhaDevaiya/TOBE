#!/usr/bin/env python

__author__ = 'Shraddhaben Devaiya'
__email__ = 'shraddha.devaiya.1998@gmail.com'
__copyright__ = 'Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab'
__license__ = 'MIT'
__maintainer__ = 'Shraddha Devaiya'

import pandas as pd
import os
import csv

class PlanController:
    """Tag plan intention comments as PLAN.
    """
    
    def __init__(self):
        self.data1 = pd.read_csv("/home/shraddha/sh_work/sh_TOBE/TOBE/data/12_2_human.csv", engine="python")
        self.i = 0
        curr_dir = os.getcwd()
        
    
    def findPlanComment(self, sentence, count):
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
        
        if self.data1['FINAL_PLAN'][count] == 1:
            #print("SHDBG: OT label no. ", count)
            if 'PLAN' not in sentence.get_tags():
                sentence.add_a_tag('PLAN')
    
        #if pred[0] == 1:
        #    if 'OT' not in sentence.get_tags() and 'Code' not in sentence.get_tags():
        #        sentence.add_a_tag('OT')