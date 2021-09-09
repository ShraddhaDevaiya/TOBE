#!/usr/bin/env python

__author__ = 'Akalanka Galappaththi'
__email__ = 'a.galappaththi@uleth.ca'
__copyright__ = 'Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab'
__license__ = 'MIT'
__maintainer__ = 'Akalanka Galappaththi'

import unittest

from models.Sentence import Sentence
from controllers.OTFController import OTFController

class TestOTFController(unittest.TestCase):
    
    def test_findOTComments(self):
        sent1 = Sentence('1.2', 'What is the purpose of that method?')
        sent2 = Sentence('2.4', 'This bug is a diplicate of http://bugzilla.mozilla.org/bug/12341')
        sent3 = Sentence('3.2', 'Thank you for the suggestion')
        sent4 = Sentence('1.1', 'Good thinking')
        sent5 = Sentence('2.6', 'Thank you')
        
        otc = OTFController()
        
        otc.findOTComment(sent1)
        otc.findOTComment(sent2)
        otc.findOTComment(sent3)
        otc.findOTComment(sent4)
        otc.findOTComment(sent5)
        
        self.assertTrue('OT' not in sent1.get_tags())
        self.assertTrue('OT' not in sent2.get_tags())
        self.assertTrue('OT' not in sent3.get_tags())
        self.assertTrue('OT' in sent4.get_tags())
        self.assertTrue('OT' in sent5.get_tags())