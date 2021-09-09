#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

from models.Turn import Turn


class BugReport:
    """Class represents a comment of a bug report. 

    Parameters
    ----------
    title : str
        Title of the bug report (One sentence summary)
    bug_id : int
        bug_id is a unique identifier
    product : str
        Software product name
    list_of_turns :list of int
        Contains a list of comment numbers
    """

    def __init__(self, title, id, product):
        self.title = title
        self.bug_id = id
        self.product = product
        self.list_of_turns = list()
        self.topics = list()

    def add_topics(self, topics):
        """Add topic list to the bug report
        
        Parameters
        ----------
        topics : list
            List of topic words
        """
        self.topics.extend(topics)
        
    def add_a_turn(self, turn):
        """Add a comment to the list

        Parameters
        ----------
        turn : object
            Turn object
        """
        self.list_of_turns.append(turn)

    def number_of_turns(self):
        """Return the number of turns in the bug report
        
        Returns
        -------
        len : int
            Length of the list
        """
        return len(self.list_of_turns)
    
    def get_turns(self):
        """Returns a list of turns
        
        Returns
        -------
        list_of_turns : list
            List of turns
        """
        return self.list_of_turns        

    def get_a_turn(self, turn_id):
        """Return a turn with a matching ID
        Parameters
        ----------
        turn_id : int
            Turn ID
        Returns
        -------
        t : object
            Turn object
        """
        for t in self.list_of_turns:
            if t.get_id() == turn_id:
                return t
        
    def get_title(self):
        """Get title

        Returns
        -------
        title : str
            Title of the bug report
        """
        return self.title

    def set_title(self, title):
        """Set title

        Parameters
        ----------
        title : str
            Title of the bug report
        """
        self.title = title

    def set_bug_id(self, bug_id):
        """Set bug ID

        Parameters
        ----------
        bug_id : int
            Bug ID
        """
        self.bug_id = bug_id

    def get_bug_id(self):
        """Get bug ID

        Returns
        -------
        bug_id : int
            Bug ID
        """
        return self.bug_id

    def get_product(self):
        """Get product name

        Returns
        -------
        product : str
            Product name
        """
        return self.product

    def set_product(self, product):
        """Set product name

        Parameters
        ----------
        product : str
            Product name
        """
        self.product = product
