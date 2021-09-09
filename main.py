#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

from controllers.BugReportController import BugReportController
from controllers.SummaryController import SummaryController
from controllers.TextCleanController import TextCleanController
from controllers.CWController import CWController
# from controllers.CFGController import CFGController
from controllers.SyntaxController import SyntaxController
from controllers.OTFController import OTFController
from controllers.RSFController import RSFController
from controllers.URLController import URLController
from controllers.DescriptionController import DescriptionController
from controllers.TopicModelController import TopicModelController
from controllers.TextCleanController import TextCleanController
from controllers.LabelWriterController import LabelWriterController

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence

from view.Display import Display

import networkx 

import pprint

if __name__ == "__main__":
    # create a list of bug reports object and get the list
    bugs = BugReportController().createBugReport()
    list_of_bugs = bugs.get_list_of_bugs()
    
    # Only need to call the summary controller if you need to extract annotated
    # summaries from the corpus. Otherwise leave it as it is.
    # # create a list of summaries

    # summary_list = SummaryController().createSummary()
    # word_count = SummaryController().wordCount(list_of_bugs, summary_list)
    
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(word_count)
    
    # for i in range(len(list_of_bugs)):
    #     print(BugReportController().getWordCount(list_of_bugs[i]))
   
    for bug in list_of_bugs:
        # take one bug report at a time
        # bug = list_of_bugs[1]

        
        

        # start the process with noise identification
        
        # first: find greeting statements
        # second: find codes
        # third: find URLs

        otc = OTFController()
        urlc = URLController()
        syc = SyntaxController()
        for turn in bug.get_turns():
            for sent in turn.get_sentences():
                urlc.findURL(sent)
                syc.findSyntaxSupervised(sent)
                otc.findOTComment(sent)

        # find clue word related links between comments/turns
        cwc = CWController()
        cwc.findLinks(bug)


        # follow with resulution statement identification
        rsfc = RSFController()
        
        for turn in bug.get_turns():
            if turn.get_id() == 1:
                continue
            for sent in turn.get_sentences():
                rsfc.findRSComments(sent)
        
        # find steps to reproduce, expected results and actual results in the first comment
        dc = DescriptionController()
        
        for turn in bug.get_turns():
            if turn.get_id() == 1:
                dc.findBugDescription(turn, bug.get_title())
                break
        
        # find topic related sentences
        tm = TopicModelController()
        
        topics = tm.extractTopics(bug, numTopics=1)
        tm.findTopicWordMatches(bug,topics)

        # run all sentences through TextCleanController to make a better display of sentences
        # tcc = TextCleanController()

        # for turn in bug.get_turns():
        #     for sent in turn.get_sentences():
        #         sent.set_cleaned_text(tcc.clean_sentence(sent.get_text(), r_digit=False, r_punc=False, stop=False, lem=False, escape=True))

        # write labels to csv
        lbl = LabelWriterController()
        lbl.write_labels(bug)

        # # display bug report with tags
        # dis = Display()
        # dis.displayBugReport(bug, ct=True)
    



