#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import unittest

from controllers.BugReportController import BugReportController
from controllers.SummaryController import SummaryController

class TestSummaryController(unittest.TestCase):
    
    def test_createSummary(self):
        sc = SummaryController()
        
        summary_list = sc.createSummary()
        
        self.assertEqual(len(summary_list), 35)
        self.assertEqual(len(summary_list[0][1]), 15)
        self.assertEqual(len(summary_list[0][2]), 19)
        self.assertEqual(len(summary_list[0][3]), 11)
        
    def test_wordCount(self):
        brl = BugReportController().createBugReport()
        bug_list = brl.get_list_of_bugs()
        
        sc = SummaryController()
        summary_list = sc.createSummary()
        
        word_count = sc.wordCount(bug_list, summary_list)
        
        self.assertEqual(len(word_count), 35)
        self.assertEqual(word_count[5][1], 175)