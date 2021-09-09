#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"


class ListOfBugReports:
    """Hold a list of bug reports.
    
    Parameters
    ----------
    list_of_bugs : list
        List of BugReport objects
    """

    list_of_bugs = list()

    def __init__(self):
        pass

    def add_report(self, bug_report):
        """Add a bug report to the list

        Parameters
        ----------
        bug_report : object
            BugReport object
        """
        self.list_of_bugs.append(bug_report)

    def number_of_bug_reports(self):
        """Returns number of bug report objects in the list
        Returns
        -------
        len : int
            Length of the list
        """
        return len(self.list_of_bugs)

    def get_list_of_bugs(self):
        """Returns a list of bug reort objects
        Returns
        -------
        list_of_bugs : list
            BugReport object list
        """
        return self.list_of_bugs
