#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import os
import xml.etree.ElementTree as ET

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence
from models.ListOfBugReports import ListOfBugReports
from view.Display import Display


class BugReportController:
    """The control class to read data and create bug report objects.
    Ojbects are added to the list_of_bug_report list and returns to main.
    """

    def __init__(self):
        pass

    def createBugReport(self):
        """Returns a list of bug reports
        Returns
        -------
        list : BugReport object
            List of bug report objects
        """
        xml_data = self.readXML("bugs.xml")

        tree = ET.parse(xml_data)
        root = tree.getroot()

        list_of_bug_report = ListOfBugReports()

        for report in root:
            bug_report = None
            for item in report.iter("BugReport"):
                for title in item.iter("Title"):
                    _bugId, _product, _title = self.extractInfoFromTitle(title.text)
                    bug_report = BugReport(_title, _bugId, _product)
                i = 1

                for turn in item.iter("Turn"):
                    for date in turn.iter("Date"):
                        _date = date.text

                    for user in turn.iter("From"):
                        _user = user.text
                    _turn = Turn(i, _user, _date)

                    for text in turn.iter("Text"):
                        j = 1
                        for sentence in text.iter("Sentence"):
                            if sentence.text is None:
                                _sentenceText = ""
                            else:
                                _sentenceText = sentence.text
                            _sentence = Sentence(str(i) + "." + str(j), _sentenceText)
                            _turn.add_a_sentence(_sentence)
                            j += 1

                    bug_report.add_a_turn(_turn)
                    i += 1

            list_of_bug_report.add_report(bug_report)

            # Display().displayBugReport(bug_report)
        # Display().displayMessage('Number of bug reports in the list: {}'.format(list_of_bug_report.number_of_bug_reports()))

        return list_of_bug_report

    def readXML(self, filename):
        """Read the XML bug report corpus
        
        Parameters
        ----------
        filename : str
            File name of the bug report corpus
            
        Returns
        -------
        bug_report_data : file object
            file object that contains an XML file
        
        Raises
        ------
        IOError
            If file name is not found in data directory
        """
        curr_dir = os.getcwd()
        data_file_path = os.path.join(curr_dir, "data", filename)

        try:
            bug_report_data = open(data_file_path, encoding="utf8")
            return bug_report_data

        except IOError:
            Display().displayMessage("The file is missing!")

    def extractInfoFromTitle(self, text):
        """In bug report corpus title is in a format of '(id) product_name - title'
        ExtractInfoFromTitle strip of the bug report ID, product name and title
           
        Parameters
        ----------
        text : str
            Bug report title with additional information
        
        Returns
        -------
        _id : str
            Bug report id
        _product : str
            Product name of which bug occured
        _title : str
            Bug report title
           
        """
        _id = text[text.find("(") + 1 : text.find(")")].strip()
        _product = text[text.find(")") + 1 : text.find("-")].strip()
        _title = text[text.find("-") + 1 : -1].strip()

        return _id, _product, _title
    
    def getWordCount(self, bug):
        """Count number of words in a bug report
        Parameters
        ----------
        bug : object
            BugReport object
        Returns
        -------
        count : int
            number of words
        """
        count = 0
        for turn in bug.get_turns():
            for sent in turn.get_sentences():
                count += len(sent.get_text().split())
                
        return count
