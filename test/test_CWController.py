#!/usr/bin/env python

__author__ = 'Akalanka Galappaththi'
__email__ = 'a.galappaththi@uleth.ca'
__copyright__ = 'Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab'
__license__ = 'MIT'
__maintainer__ = 'Akalanka Galappaththi'

import unittest
import networkx as nx

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence
from controllers.CWController import CWController
from view.Display import Display


class TestCWController(unittest.TestCase):
    bug = BugReport('Submenu items covers parent menu items', 1234, 'Firefox')

    turn1 = Turn(1, 'John Doe', '2020-01-02 14:27:15')
    sent1 = Sentence(
        '1.1', 'When open the menu and click on submenu item, submenu covers menu items'
    )
    sent2 = Sentence(
        '1.2', 'Submenu should open on right hand side when screen space is available'
    )
    turn1.add_a_sentence(sent1)
    turn1.add_a_sentence(sent2)

    turn2 = Turn(2, 'Joan Doe', '2020-01-02 15:02:18')
    sent3 = Sentence('2.1', 'Reply to comment 1')
    sent4 = Sentence(
        '2.2',
        '&amp;gt; Submenu should open on right hand side when screen space is available',
    )
    sent5 = Sentence('2.3', 'I\'m using OS X. Submenu doesn\'t open on top of the menu.')
    sent6 = Sentence(
        '2.4', 'Let\'s see anyone else face the same problem. I can\'t reproduce this.'
    )
    sent7 = Sentence('2.5', '&amp;gt; Random comment at the end...')
    turn2.add_a_sentence(sent3)
    turn2.add_a_sentence(sent4)
    turn2.add_a_sentence(sent5)
    turn2.add_a_sentence(sent6)
    turn2.add_a_sentence(sent7)
    
    turn3 = Turn(3, 'Bart Simpson', '2020-02-28 13:37:34')
    sent8 = Sentence('3.1', '&amp;gt; + mod1')
    sent9 = Sentence('3.2', '&amp;gt; + mod2')
    sent10 = Sentence('3.3', '&amp;gt; + mod3')
    sent11 = Sentence('3.4', 'Since this is now implemented on Win7 with Multitouch screens please be sure not to disable it for Windows.')
    turn3.add_a_sentence(sent8)
    turn3.add_a_sentence(sent9)
    turn3.add_a_sentence(sent10)
    turn3.add_a_sentence(sent11)

    turn4 = Turn(4, 'Lisa Simpson', '2020-02-28 13:37:34')
    sent12 = Sentence('4.1', '&amp;gt; Since this is now implemented on Win7 with Multitouch screens please be sure not to disable it for Windows.')
    sent13 = Sentence('4.2', 'And maybe Windows 7 is just better at discriminating between gestures.')
    sent14 = Sentence('4.3', 'OTOH it wouldn\'t be a big deal to just disable it globally.')
    sent15 = Sentence('4.4', 'Safari doesn\'t use it, and Rob confirmed that IE doesn\'t use it on Windows 7.')
    turn4.add_a_sentence(sent12)
    turn4.add_a_sentence(sent13)
    turn4.add_a_sentence(sent14)
    turn4.add_a_sentence(sent15)

    bug.add_a_turn(turn1)
    bug.add_a_turn(turn2)
    bug.add_a_turn(turn3)
    bug.add_a_turn(turn4)

    def test_findQuotes(self):

        cwc = CWController()
        self.assertFalse(cwc.findQuotes(self.sent1))
        self.assertFalse(cwc.findQuotes(self.sent2))
        self.assertTrue(cwc.findQuotes(self.sent4))
        self.assertFalse(cwc.findQuotes(self.sent3))
        self.assertFalse(cwc.findQuotes(self.sent5))
        self.assertTrue(cwc.findQuotes(self.sent8))
        self.assertTrue(cwc.findQuotes(self.sent9))
        self.assertTrue(cwc.findQuotes(self.sent10))

    def test_findOriginalSentence(self):
        s1 = 'some users do not want the menu, and others do not want any session tracks'
        s2 = 'some users do not want the menu,'
        s3 = 'text that does not match'
        s4 = 'and others do not want any session tracks'
        s5 = 'a problem with this patch is that the session data is still stored in memory while the app is running, and by removing this pref, there\'s no way to disable that.'
        s6 = 'and others don\'t want any session tracks stored in memory at all.'
        s7 = '&amp;gt; This bug is just rotate, but do we want to consider pinching too?'
        s8 = '&amp;gt; This bug is just rotate, but do we want to consider pinching too?'
        s9 = 'And I wasn\'t able to reproduce this bug on my machine at work, although both home and work machines run Debian/testing (but have different hardware).'
        s10 = '(but have different hardware)'
        
        cwc = CWController()
        self.assertTrue(cwc.findOriginalSentence(s2, s1))
        self.assertFalse(cwc.findOriginalSentence(s3, s1))
        self.assertTrue(cwc.findOriginalSentence(s4, s1))
        self.assertFalse(cwc.findOriginalSentence(self.sent8.get_text(), self.sent6.get_text()))
        self.assertFalse(cwc.findOriginalSentence(s5, s6))
        self.assertFalse(cwc.findOriginalSentence(s7, s8))
        # special case because hardware). != hardware). Since the threshold is more than 3 s10 is not a quote of s9
        self.assertFalse(cwc.findOriginalSentence(s9, s10))

    def test_createQuotationGraph(self):
        cwc = CWController()

        actual_G = cwc.createQuotationGraph(self.bug)

        expected_edges = [('2.1', '1.2'), ('2.3', '1.2'), ('2.4', '1.2')]
        expected_G = nx.DiGraph()
        expected_G.add_edges_from(expected_edges)

        for e in expected_edges:
            self.assertTrue(e in actual_G.edges)

    def test_findLinks(self):
        cwc = CWController()
        
        cwc.findLinks(self.bug)
        
        self.assertTrue('CW' in self.sent2.get_tags())
        self.assertTrue('Org' in self.sent2.get_tags())
        self.assertTrue('CW' in self.sent5.get_tags())
        self.assertFalse('CW' in self.sent6.get_tags())
        self.assertFalse('CW' in self.sent1.get_tags())
        self.assertFalse('QT' in self.sent8.get_tags())
        self.assertTrue('QT' not in self.sent9.get_tags())
        self.assertTrue('Org' in self.sent11.get_tags())
        self.assertTrue('CW' in self.sent11.get_tags())
        self.assertTrue('QT' in self.sent12.get_tags())
        self.assertTrue('CW' in self.sent13.get_tags())
        self.assertTrue('CW' in self.sent14.get_tags())
        self.assertTrue('CW' in self.sent15.get_tags())
        
        # Display().displayBugReport(self.bug)

if __name__ == '__main__':
    unittest.main()
