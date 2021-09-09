#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

from models.Sentence import Sentence


class Turn:
    """Class represents a comment of a bug report. 

    Parameters
    ----------
    turn_id : int
        turn_id is a sequence number that represents order of the conversation
    author_name : str
        Author of the comment
    date_time : str
        Time stamp of the comment
    list_of_sentences :list of str
        Contains a list of sentence IDs of the turn
    """

    def __init__(self, id, author, dt):
        self.turn_id = id
        self.author_name = author
        self.date_time = dt
        self.list_of_sentences = list()

    def add_a_sentence(self, sentence):
        """Add a sentence to the list

        Parameters
        ----------
        sentence : object
            Sentence object
        """
        self.list_of_sentences.append(sentence)

    def number_of_sentences(self):
        """Return the number of sentences in the turn
        
        Returns
        -------
        len : int
            Length of the list
        """
        return len(self.list_of_sentences)

    def get_sentences(self):
        """Returns a list of sentences
        
        Returns
        -------
        list_of_sentences : list
            List of sentences
        """
        
        return self.list_of_sentences
    
    def get_a_sentence(self, s_id):
        """Return a sentence with a matching ID
        Parameters
        ----------
        id : str
            Sentence ID
        Returns
        -------
        s : object
            Sentence object
        """
        for s in self.list_of_sentences:
            if s.get_id() == s_id:
                return s
            
    def get_id(self):
        """Get turn id

        Returns
        -------
        turn_id : int
            Turn ID / Commet ID
        """
        return self.turn_id

    def set_id(self, id):
        """Set turn id

        Parameters
        ----------
        id : int
            Turn ID / Comment ID
        """
        self.turn_id = id

    def get_author(self):
        """Get author name

        Returns
        -------
        author_name : str
            Author name
        """
        return self.author_name

    def set_author(self, name):
        """Set author name

        Parameters
        ----------
        name : str
            Author name
        """
        self.author_name = name

    def get_date_time(self):
        """Get date time in YYYY-MM-DD hh:mm:ss format

        Returns
        -------
        date_time : str
            Timestamp of the comment
        """
        return self.date_time

    def set_date_time(self, date_time):
        """Set date time in YYYY-MM-DD hh:mm:ss format

        Parameters
        ----------
        date_time : str
            Timestamp
        """
        self.date_time = date_time
