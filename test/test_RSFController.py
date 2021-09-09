#!/usr/bin/env python

__author__ = 'Akalanka Galappaththi'
__email__ = 'a.galappaththi@uleth.ca'
__copyright__ = 'Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab'
__license__ = 'MIT'
__maintainer__ = 'Akalanka Galappaththi'

import unittest

from models.Sentence import Sentence
from controllers.RSFController import RSFController

class TestRSFController(unittest.TestCase):
    
    def test_findRSComments(self):
        rsc = RSFController()
        
        sent1 = Sentence('1.1', 'Pushed http://hg.mozilla.org/mozilla-central/rev/097598383614')
        rsc.findRSComments(sent1)
        self.assertTrue('RES' in sent1.get_tags())
        
        sent2 = Sentence('1.2', 'Created an attachment (id=383211) [details] Patch v.2')
        rsc.findRSComments(sent2)
        self.assertTrue('RES' in sent2.get_tags())
        
        sent3 = Sentence('1.3', '(From update of attachment 383211 [details])')
        rsc.findRSComments(sent3)
        self.assertTrue('RES' in sent3.get_tags())
        
        sent4 = Sentence('1.4', 'onemen: This patch significantly affects Tab Mix Plus:')
        rsc.findRSComments(sent4)
        self.assertTrue('RES' in sent4.get_tags())
        
        sent5 = Sentence('1.5', 'Create a patch')
        rsc.findRSComments(sent5)
        self.assertTrue('RES' in sent5.get_tags())
        
        sent6 = Sentence('1.6', 'If there are no objections, I could commit the patch.')
        rsc.findRSComments(sent6)
        self.assertTrue('RES' in sent6.get_tags())
        
        sent7 = Sentence('1.7', 'Committed to both branches:')
        rsc.findRSComments(sent7)
        self.assertTrue('RES' in sent7.get_tags())
        
        sent8 = Sentence('1.8', 'Thanks for the review. It\'s now committed')
        rsc.findRSComments(sent8)
        self.assertTrue('RES' in sent8.get_tags())
        
        sent9 = Sentence('1.9', 'This means that to truly fix the bug, we\'d have to change the operations')
        rsc.findRSComments(sent9)
        self.assertTrue('RES' in sent9.get_tags())
        
        sent10 = Sentence('1.10', 'This fixes the problem, but isn\'t quite correct...')
        rsc.findRSComments(sent10)
        self.assertTrue('RES' in sent10.get_tags())
        
        sent11 = Sentence('1.11', 'The simple fix it to just discard the service\'s form history result')
        rsc.findRSComments(sent11)
        self.assertTrue('RES' in sent11.get_tags())
        
        sent12 = Sentence('1.12', 'FWIW, I\'m not nearly as keen on disabling that one, and am fairly-to-surely likely to WONTFIX such a bug.')
        rsc.findRSComments(sent12)
        self.assertTrue('RES' not in sent12.get_tags())