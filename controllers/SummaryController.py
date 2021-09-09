#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import os
import xml.etree.ElementTree as ET

from models.ListOfBugReports import ListOfBugReports
from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence
from view.Display import Display

class SummaryController:
    """Read xml file and extract word count of extractive summary
    """
    
    def __init__(self):
        pass
    
    def createSummary(self):
        """Create a list of dictionaries. Each dictionary contains word count of the summary
        """
        xml_data = self.readXML("annotation.xml")

        tree = ET.parse(xml_data)
        root = tree.getroot()
        
        summary_list = list()
        for elem in root:
            for report in elem.iter('BugReport'):
                ext_summaries = dict()
                i = 1
                for annot in report.iter('Annotation'):
                    for exts in annot.iter('ExtractiveSummary'):
                        sent_list = list()
                        for sent in exts.iter('Sentence'):
                            sent_list.append(str(sent.get('ID')).strip())
                    ext_summaries[i] = sent_list
                    i += 1
            summary_list.append(ext_summaries)
            
        return summary_list
    
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
            
    def wordCount(self, bugReports, summaries):
        
        word_count = list()
        for i in range(len(summaries)):
            count_dict = dict()
            for key in summaries[i].keys():
                count = 0
                for id in summaries[i][key]:
                    _turn = id.split('.')[0]
                    count += len(bugReports[i].get_a_turn(int(_turn)).get_a_sentence(id).get_text().split())
                count_dict[key] = count
            word_count.append(count_dict)
            
        return word_count