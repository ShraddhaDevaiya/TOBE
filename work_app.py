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
#from controllers.OTFController import OTFController
from controllers.RSFController import RSFController
from controllers.URLController import URLController
from controllers.CWController import CWController
# from controllers.CFGController import CFGController
#from controllers.SyntaxController import SyntaxController
from controllers.TopicModelController import TopicModelController
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
    
    # create controller objects
    #otc = OTFController()
    rsc = RSFController()
    urlc = URLController()
    # cfgc = CFGController()
    #syc = SyntaxController()
    tmc = TopicModelController()
    tcc = TextCleanController()
    
    for turn in list_of_bugs[i].get_turns():
        for sent in turn.get_sentences():
            # cfgc.setSentenceType(sent)
            urlc.findURL(sent)
            #syc.findSyntax(sent)
            #otc.findOTComment(sent)
            
            
            
    # Need a separate loop since the first comment doesn't have resolution sentences        
    for turn in list_of_bugs[i].get_turns():
        if turn.get_id() == 1:
            continue
        for sent in turn.get_sentences():
            rsc.findRSComments(sent)
    
    # find clue word related links between comments/turns
    cwc = CWController()
    cwc.findLinks(list_of_bugs[i]) 
    
    # find topic words in sentences
    topics = tmc.extractTopics(list_of_bugs[i])
    tmc.findTopicWordMatches(list_of_bugs[i], topics)
    
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
    
    # list index selector
    i = int(request.args.get('id'))
    # print(i)
    
    # create controller objects
    #otc = OTFController()
    rsc = RSFController()
    urlc = URLController()
    # cfgc = CFGController()
    #syc = SyntaxController()
    tmc = TopicModelController()
    tcc = TextCleanController()

    for turn in list_of_bugs[i].get_turns():
        for sent in turn.get_sentences():
            # cfgc.setSentenceType(sent)
            urlc.findURL(sent)
            #syc.findSyntax(sent)
            #otc.findOTComment(sent)
            
            
            
    # Need a separate loop since the first comment doesn't have resolution sentences        
    for turn in list_of_bugs[i].get_turns():
        if turn.get_id() == 1:
            continue
        for sent in turn.get_sentences():
            rsc.findRSComments(sent)
    
    # find clue word related links between comments/turns
    cwc = CWController()
    cwc.findLinks(list_of_bugs[i]) 
    
    # find topic words in sentences
    topics = tmc.extractTopics(list_of_bugs[i])
    tmc.findTopicWordMatches(list_of_bugs[i], topics)
    
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