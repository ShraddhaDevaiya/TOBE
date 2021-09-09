#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import unittest
import pandas as pd
import os
import re

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence
from controllers.TopicModelController import TopicModelController
from controllers.BugReportController import BugReportController

class TestTopicModelController(unittest.TestCase):
    # bug = BugReport('Submenu items covers parent menu items', 1234, 'Firefox')

    # turn1 = Turn(1, 'John Doe', '2020-01-02 14:27:15')
    # sent1 = Sentence(
    #     '1.1', 'When open the menu and click on submenu item, submenu covers menu items'
    # )
    # sent2 = Sentence(
    #     '1.2', 'Submenu should open on right hand side when screen space is available'
    # )
    # turn1.add_a_sentence(sent1)
    # turn1.add_a_sentence(sent2)

    # turn2 = Turn(2, 'Joan Doe', '2020-01-02 15:02:18')
    # sent3 = Sentence('2.1', 'Reply to comment 1')
    # sent4 = Sentence(
    #     '2.2',
    #     '&amp;gt; Submenu should open on right hand side when screen space is available',
    # )
    # sent5 = Sentence('2.3', 'I\'m using OS X. Submenu doesn\'t open on top of the menu.')
    # sent6 = Sentence(
    #     '2.4', 'Let\'s see anyone else face the same problem. I can\'t reproduce this.'
    # )
    # sent7 = Sentence('2.5', '&amp;gt; Random comment at the end...')
    # sent7.add_a_tag('OT')
    # sent8 = Sentence('2.6', 'Pushed to https://mozilla.bugzilla.org/bug?/12334')
    # sent8.add_a_tag('URL')
    # turn2.add_a_sentence(sent3)
    # turn2.add_a_sentence(sent4)
    # turn2.add_a_sentence(sent5)
    # turn2.add_a_sentence(sent6)
    # turn2.add_a_sentence(sent7)
    # turn2.add_a_sentence(sent8)

    # bug.add_a_turn(turn1)
    # bug.add_a_turn(turn2)
    bugs = BugReportController().createBugReport()
    list_of_bugs = bugs.get_list_of_bugs()
        
    tm = TopicModelController()
    
    def test_extractTopics(self):
        
        # topic_res = pd.DataFrame(columns=['topics', 'perplexity', 'coherance'])
        for b in self.list_of_bugs:
            topics = self.tm.extractTopics(b, numTopics=1)
            # topics, perp, coh = self.tm.extractTopics(b, numTopics=1)
            # topic_res = topic_res.append({'topics':topics, 'perplexity':perp, 'coherance':coh}, ignore_index=True)
            
            topic_string = topics[0][1]
            topic_words = re.findall(r'\b[a-z]+\b', topic_string)
            
            print(topic_words)
            
            
            break
        # record coherance and perplexity for different topic models
        # curr_dir = os.getcwd()
        # csv_path = os.path.join(curr_dir, 'data', 'topic_res.csv')
        # topic_res.to_csv(csv_path)
        
        
    # def test_findTopicSimilarity(self):
    #     topics = self.tm.extractTopics(self.list_of_bugs[0])
    #     self.tm.findTopicSimilarity(self.list_of_bugs[0], topics)
    
    def test_findTopicWordMatches(self):
        
        topics = self.tm.extractTopics(self.list_of_bugs[0])
        self.tm.findTopicWordMatches(self.list_of_bugs[0], topics)