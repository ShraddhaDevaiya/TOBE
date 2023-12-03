#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
import json
from jinja2 import Template

from controllers.BugReportController import BugReportController
from controllers.OTFController import OTFController
from controllers.PlanController import PlanController
from controllers.RSFController import RSFController
from controllers.URLController import URLController
from controllers.CWController import CWController
# from controllers.CFGController import CFGController
# from controllers.SyntaxController import SyntaxController
#SH_FIX
#from controllers.TopicModelController import TopicModelController
from controllers.DescriptionController import DescriptionController
from controllers.TextCleanController import TextCleanController
from view.Display import Display

# load .env file
load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/', methods=['GET','POST'])
def display():
    # create a ListOfBugReport object and get the list
    bugs = BugReportController().createBugReport()
    list_of_bugs = bugs.get_list_of_bugs()
    
    # list index selector
    i = 0
    #SH_FIX
    count = 0
    
    # create controller objects
    otc = OTFController()
    planc = PlanController()
    rsc = RSFController()
    urlc = URLController()
    # cfgc = CFGController()
    # syc = SyntaxController()
    #tmc = TopicModelController()
    tcc = TextCleanController()
    
    
    for turn in list_of_bugs[i].get_turns():
        for sent in turn.get_sentences():
            # cfgc.setSentenceType(sent)
            urlc.findURL(sent)
            #syc.findSyntax(sent)
            #SH_FIX
            #otc.findOTComment(sent)
            otc.findOTComment(sent, count)
            planc.findPlanComment(sent, count)
            count = count + 1
            
            
            
    # Need a separate loop since the first comment doesn't have resolution sentences        
    for turn in list_of_bugs[i].get_turns():
        if turn.get_id() == 1:
            continue
        for sent in turn.get_sentences():
            rsc.findRSComments(sent)
    
    # find clue word related links between comments/turns
    cwc = CWController()
    cwc.findLinks(list_of_bugs[i]) 
    
    #SH_FIX
    # find topic words in sentences
    #topics = tmc.extractTopics(list_of_bugs[i])
    #tmc.findTopicWordMatches(list_of_bugs[i], topics)
    
    # find steps to reproduce, expected results and actual results in the first comment
    dc = DescriptionController()
    
    for turn in list_of_bugs[i].get_turns():
        if turn.get_id() == 1:
            dc.findBugDescription(turn, list_of_bugs[i].get_title())
            break      
    #SH_FIX
    # run all sentences through TextCleanController to make a better display of sentences
    for turn in list_of_bugs[i].get_turns():
        for sent in turn.get_sentences():
            sent.set_cleaned_text(tcc.clean_sentence(sent.get_text(), r_digit=False, r_punc=False, stop=False, lem=False, escape=True))

    # call the display option after running automatic labeling
    bug_data = Display().getBugReportJson(list_of_bugs[i], ct=True)
    deserialized_bug_data = json.loads(bug_data)
    
    # sanity check for list of turns
    # print(deserialized_bug_data['list_of_turns'])
    
    # createa jinja template 
    return render_template('display.html', response = deserialized_bug_data)

@app.route('/select', methods=['GET','POST'])
def selectDisplay():
    # create a ListOfBugReport object and get the list
    bugs = BugReportController().createBugReport()
    list_of_bugs = bugs.get_list_of_bugs()
    #SH_FIX
    count = 0
    # list index selector
    i = int(request.args.get('id'))
    # print(i)
    
    # create controller objects
    otc = OTFController()
    planc = PlanController()
    rsc = RSFController()
    urlc = URLController()
    # cfgc = CFGController()
    # syc = SyntaxController()
    #tmc = TopicModelController()
    tcc = TextCleanController()

    if i == 0:
        count = 0
    elif i == 1:
        count = 31
    elif i == 2:
        count = 31 + 57
    elif i == 3:
        count = 31 + 57 + 91
    elif i == 4:
        count = 31 + 57 + 91 + 44
    elif i == 5:
        count = 31 + 57 + 91 + 44 + 102
    elif i == 6:
        #FIXME
        count = 31 + 57 + 91 + 44 + 102 + 31
    elif i == 7:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56
    elif i == 8:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82
    elif i == 9:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17
    elif i == 10:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50
    elif i == 11:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41
    elif i == 12:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73
    elif i == 13:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50
    elif i == 14:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52
    elif i == 15:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98
    elif i == 16:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69
    elif i == 17:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85
    elif i == 18:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46
    elif i == 19:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56
    elif i == 20:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46
    elif i == 21:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18
    elif i == 22:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194
    elif i == 23:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65
    elif i == 24:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90
    elif i == 25:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60
    elif i == 26:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60 + 136
    elif i == 27:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60 + 136 + 55
    elif i == 28:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60 + 136 + 55 + 24
    elif i == 29:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60 + 136 + 55 + 24 + 93
    elif i == 30:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60 + 136 + 55 + 24 + 93 + 50
    elif i == 31:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60 + 136 + 55 + 24 + 93 + 50 + 39
    elif i == 32:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60 + 136 + 55 + 24 + 93 + 50 + 39 + 85
    elif i == 33:
        count = 31 + 57 + 91 + 44 + 102 + 31 + 56 + 82 + 17 + 50 + 41 + 73 + 50 + 52 + 98 + 69 + 85 + 46 \
            + 56 + 46 + 18 + 194 + 65 + 90 + 60 + 136 + 55 + 24 + 93 + 50 + 39 + 85 + 104

    for turn in list_of_bugs[i].get_turns():
        for sent in turn.get_sentences():
            # cfgc.setSentenceType(sent)
            urlc.findURL(sent)
            # syc.findSyntax(sent)
            #SH_FIX
            #otc.findOTComment(sent)
            otc.findOTComment(sent, count)
            planc.findPlanComment(sent, count)
            count = count + 1
            
            
            
    # Need a separate loop since the first comment doesn't have resolution sentences        
    for turn in list_of_bugs[i].get_turns():
        if turn.get_id() == 1:
            continue
        for sent in turn.get_sentences():
            rsc.findRSComments(sent)
    
    # find clue word related links between comments/turns
    cwc = CWController()
    cwc.findLinks(list_of_bugs[i]) 
    
    #SH_FIX
    # find topic words in sentences
    #topics = tmc.extractTopics(list_of_bugs[i])
    #tmc.findTopicWordMatches(list_of_bugs[i], topics)
    
    # find steps to reproduce, expected results and actual results in the first comment
    dc = DescriptionController()
    
    for turn in list_of_bugs[i].get_turns():
        if turn.get_id() == 1:
            dc.findBugDescription(turn, list_of_bugs[i].get_title())
            break      

    # run all sentences through TextCleanController to make a better display of sentences
    for turn in list_of_bugs[i].get_turns():
        for sent in turn.get_sentences():
            sent.set_cleaned_text(tcc.clean_sentence(sent.get_text(), r_digit=False, r_punc=False, stop=False, lem=False, escape=True))

    # call the display option after running automatic labeling
    bug_data = Display().getBugReportJson(list_of_bugs[i])
    deserialized_bug_data = json.loads(bug_data)
    
    # sanity check for list of turns
    # print(deserialized_bug_data['list_of_turns'])
    
    # createa jinja template 
    return render_template('display.html', response = deserialized_bug_data)

if __name__ == '__main__':
    app.run()