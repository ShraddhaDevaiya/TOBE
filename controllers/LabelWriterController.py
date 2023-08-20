#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import os
import csv

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence

class LabelWriterController:
    """Write labels to a csv file in the order of DES, Org, QT, CW, RES, OT, URL, Code.
    """

    def __init__(self):
        pass

    def write_labels(self, bug):
        """Write 0/1 to designated col in csv file if the label present
        Parameters
        ----------
        bug : BugReport object
        """

        curr_dir = os.getcwd()
        #res_path = os.path.join(curr_dir, 'data', 'res_ot_git_naive.csv')
        res_path = os.path.join(curr_dir, 'data', 'res_sh_des.csv')
        with open(res_path, 'a+', newline='') as write_obj:
            csv_writer = csv.writer(write_obj)

            # initialize the row with zeros
            # then change 0 to 1 if label present
            curr_row = [0, 0, 0, 0, 0, 0, 0, 0]

            for turn in bug.get_turns():
                for sent in turn.get_sentences():
                    labels = sent.get_tags()
                    if 'DES' in labels:
                        curr_row[0] = 1
                    if 'Org' in labels:
                        curr_row[1] = 1
                    if 'QT' in labels:
                        curr_row[2] = 1
                    if 'CW' in labels:
                        curr_row[3] = 1
                    if 'RES' in labels:
                        curr_row[4] = 1
                    if 'OT' in labels:
                        curr_row[5] = 1
                    if 'URL' in labels:
                        curr_row[6] = 1
                    if 'Code' in labels:
                        curr_row[7] = 1
                    
                    csv_writer.writerow(curr_row)
                    curr_row = [0, 0, 0, 0, 0, 0, 0, 0]


