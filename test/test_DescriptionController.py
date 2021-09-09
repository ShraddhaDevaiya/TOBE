#!/usr/bin/env python

__author__ = 'Akalanka Galappaththi'
__email__ = 'a.galappaththi@uleth.ca'
__copyright__ = 'Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab'
__license__ = 'MIT'
__maintainer__ = 'Akalanka Galappaththi'

import unittest

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence
from controllers.DescriptionController import DescriptionController
from controllers.CFGController import CFGController
from controllers.TextCleanController import TextCleanController

class TestDescriptionController(unittest.TestCase):
    bug1 = BugReport('infinite loop at refresh when a calendar is deleted from the server outside of Lightning', 429126, 'Bugzilla Calendar')
    turn1 = Turn(1, 'John Doe', '2020-01-02 14:27:15')
    sent1 = Sentence('1.1', 'User-Agent:       Mozilla/5.0 (X11; U; Linux x86_64; fr-FR; rv:1.8.1.13) Gecko/20080311 Iceweasel/2.0.0.13 (Debian-2.0.0.13-1)')
    sent2 = Sentence('1.2', 'When a calendar to which I am subscribed no longer exists, Lightning will try indefinitely to reach it and use 100\'%\' of my CPU. This, despite the 404 results it receives.')
    sent3 = Sentence('1.3', 'Reproducible: Always')
    sent4 = Sentence('1.4', 'Steps to Reproduce:')
    sent5 = Sentence('1.5', '1. create a calendar on your server')
    sent6 = Sentence('1.6', '2. subscribe to it via Lightning')
    sent7 = Sentence('1.7', '3. quit Thunderbird')
    sent8 = Sentence('1.8', '4. erase the calendar from your server')
    sent9 = Sentence('1.9', '5. relaunch Thunderbird')
    sent10 = Sentence('1.10', 'Actual Results:')
    sent11 = Sentence('1.11', 'A propfind is executed on the resource, resulting in a 404 error code.')
    sent12 = Sentence('1.12', 'An OPTION on the parent directory occurs, with a 200 result.')
    sent13 = Sentence('1.13', 'Then the loop continues with a new propfind...')
    sent14 = Sentence('1.14', 'Expected Results:')
    sent15 = Sentence('1.15', 'I would expect Lightning to stop trying to reach the calendar collection as')
    sent16 = Sentence('1.16', 'soon as it receives the 404 result.')
    sent17 = Sentence('1.17', 'Here is a trace of what happens (obtained with tcpflow):')
    sent18 = Sentence('1.18', 'PROPFIND /SOGo/dav/wsourdeau/Calendar/1D52AE6B-8564-0001-6A40-17B089902560/')
    
    turn1.add_a_sentence(sent1)
    turn1.add_a_sentence(sent2)
    turn1.add_a_sentence(sent3)
    turn1.add_a_sentence(sent4)
    turn1.add_a_sentence(sent5)
    turn1.add_a_sentence(sent6)
    turn1.add_a_sentence(sent7)
    turn1.add_a_sentence(sent8)
    turn1.add_a_sentence(sent9)
    turn1.add_a_sentence(sent10)
    turn1.add_a_sentence(sent11)
    turn1.add_a_sentence(sent12)
    turn1.add_a_sentence(sent13)
    turn1.add_a_sentence(sent14)
    turn1.add_a_sentence(sent15)
    turn1.add_a_sentence(sent16)
    turn1.add_a_sentence(sent17)
    turn1.add_a_sentence(sent18)
    bug1.add_a_turn(turn1)
    
    bug2 = BugReport('search suggestions passes wrong previous result to form history', 495584, 'Firefox')
    turn2 = Turn(1, 'John Doe', '2020-01-02 14:27:15')
    sent_1 = Sentence('1.1', 'MattN noticed a problem with the WIP patch from bug 469443 applied.')
    sent_2 = Sentence('1.2', 'When typing in the search box, sometimes search-suggestion entries would be displayed above the divider (where entries for previous matching searches are).')
    sent_3 = Sentence('1.3', 'The problem here is that nsSearchSuggestions.js is passing the wrong previousResult to form history.')
    sent_4 = Sentence('1.4', 'Instead of it being the previous form history search result, it\'s the SuggestAutoCompleteResult result (which contains the union of the form-history and search-suggest entries).') 
    sent_5 = Sentence('1.5', 'So, when form history refines its results as you time, it can actually add *more* entries as data leaks from the suggestions result into form history result, and it thus looks like the divider is being drawn in the wrong place.')
    sent_6 = Sentence('1.6', 'This bug wasn\'t visible before 469443, because nsFormFillController::StartSearch tries to QI the provided result to a nsIAutoCompleteSimpleResult.')
    sent_7 = Sentence('1.7', 'The search-suggestion result is only implements nsIAutoCompletResult (no \"Simple\"), so the QI fails, historyResult nee previousResult becomes null, and thus Satchel was doing a new search every time.')
    sent_8 = Sentence('1.8', 'EG:')
    sent_9 = Sentence('1.9', '1) type \"b\" in the search field.')
    sent_10 = Sentence('1.10', '2) form history finds 1 entry (\"blah\"), search-suggestions finds \"baaa\", \"bloop\", \"bzzz\", the autocompete menu shows these in order with a divider between \"blah\" and \"baaa\".')
    
    turn2.add_a_sentence(sent_1)
    turn2.add_a_sentence(sent_2)
    turn2.add_a_sentence(sent_3)
    turn2.add_a_sentence(sent_4)
    turn2.add_a_sentence(sent_5)
    turn2.add_a_sentence(sent_6)
    turn2.add_a_sentence(sent_7)
    turn2.add_a_sentence(sent_8)
    turn2.add_a_sentence(sent_9)
    turn2.add_a_sentence(sent_10)
    bug2.add_a_turn(turn2)

    bug3 = BugReport('Remember last scale method setting', 164995, 'GIMP')
    turn3 = Turn(1, 'John Doe', '2020-01-02 14:27:15')
    sent1_1 = Sentence('1.1', 'When images are rescaled now the GIMP always defaults to linear scaling.')
    turn3.add_a_sentence(sent1_1)
    bug3.add_a_turn(turn3)
    
    
    # def test_findReproduceStatements(self):
    #     dc = DescriptionController()
        
    #     dc.findBugDescription(self.turn1, self.bug1.get_title())
        
    #     self.assertTrue('DES' not in self.sent1.get_tags())
    #     self.assertTrue('DES' not in self.sent3.get_tags())
    #     self.assertTrue('DES' in self.sent4.get_tags())
    #     self.assertTrue('DES' in self.sent5.get_tags())
    #     self.assertTrue('DES' in self.sent6.get_tags())
    #     self.assertTrue('DES' in self.sent7.get_tags())
    #     self.assertTrue('DES' in self.sent8.get_tags())
    #     self.assertTrue('DES' in self.sent9.get_tags())
    #     self.assertTrue('DES' in self.sent10.get_tags())
    #     self.assertTrue('DES' in self.sent11.get_tags())
    #     self.assertTrue('DES' in self.sent12.get_tags())
    #     self.assertTrue('DES' in self.sent13.get_tags())
    #     self.assertTrue('DES' in self.sent14.get_tags())
    #     self.assertTrue('DES' in self.sent15.get_tags())
    #     self.assertTrue('DES' in self.sent16.get_tags())
    #     self.assertTrue('DES' in self.sent17.get_tags())
    #     self.assertTrue('DES' not in self.sent18.get_tags())

    # def test_findReproduceStatements2(self):
    #     dc = DescriptionController()
        
    #     dc.findBugDescription(self.turn2, self.bug2.get_title()) 
        
    #     self.assertTrue('DES' not in self.sent_1.get_tags())
    #     self.assertTrue('DES' in self.sent_2.get_tags())
    #     self.assertTrue('DES' in self.sent_3.get_tags())
    #     self.assertTrue('DES' in self.sent_4.get_tags())
    #     self.assertTrue('DES' in self.sent_5.get_tags())
    #     self.assertTrue('DES' in self.sent_6.get_tags())
    #     self.assertTrue('DES' in self.sent_7.get_tags())
    #     self.assertTrue('DES' not in self.sent_8.get_tags())
    #     self.assertTrue('DES' in self.sent_9.get_tags())
    #     self.assertTrue('DES' in self.sent_10.get_tags())

    def test_findReproduceStatements3(self):
        dc = DescriptionController()

        dc.findBugDescription(self.turn3, self.bug3.get_title())

        self.assertTrue('DES' in self.sent1_1.get_tags())  
           
if __name__ == '__main__':
    unittest.main()