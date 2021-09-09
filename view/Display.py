#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import pprint
import json

from models.Turn import Turn
from models.Sentence import Sentence
from models.BugReport import BugReport
from models.ListOfBugReports import ListOfBugReports

pp = pprint.PrettyPrinter(indent=2)


class Display:
    def __init__(self):
        pass

    def displayMessage(self, msg):
        """Display message

        Parameters
        ----------
        msg : str
            Message
        """
        print("{}".format(msg))

    def displayBugReport(self, bugReport, ct=False):
        """Display bug report
        
        Parameters
        ----------
        bugReport : object
            Bug reort object
        ct : boolean
            Parameter that enable the print cleaned text
        """
        print("{}".format(bugReport.get_title()))

        for turn in bugReport.list_of_turns:
            print("\n \t Author:{}".format(turn.get_author()))
            print("\t Date:{}".format(turn.get_date_time()))

            for sentence in turn.list_of_sentences:
                if ct == True:
                    print(
                        "\t\t {} : {}".format(
                            sentence.get_id(), sentence.get_cleaned_text()
                        )
                    )
                    print("\t\t {}".format(sentence.get_tags()))
                else:
                    print("\t\t {} : {}".format(sentence.get_id(), sentence.get_text()))
                    print("\t\t {}".format(sentence.get_tags()))
                    
    def getBugReportJson(self, bugReport, ct=False):
        """Display bug report
        
        Parameters
        ----------
        bugReport : int
            Bug reort object
        ct : boolean
            Parameter that enable the print cleaned text
        Returns
        -------
        j_obj : json object
            Bugreport as a JSON
        """
                   
        return json.dumps(bugReport, default=lambda obj: obj.__dict__)
    
        
