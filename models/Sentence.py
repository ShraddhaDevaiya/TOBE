#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"


class Sentence:
    """Class represents a sentence of a comment of a bug report

    Parameters
    ----------
    sentence_id : str
        sentence_id is a combination of turn_id and the sequence number
        (ex: 1.3 means turn 1 and 3rd sentence of the turn)
    text : str
        orginal sentence text as appeared in the bug report
    cleaned_text : str
        cleaned text after removing irrelevant characters, stop words,
        turning to lower case and lemmatizing
    tags :list of str
        tags indicate the type of the sentence (description, clarification,
        plan, resolution) and/or picked by certain algorithm
    """

    def __init__(self, id, text):
        self.sentence_id = id
        self.text = text
        self.cleaned_text = ""
        self.tags = list()

    def get_id(self):
        """Get sentence id

        Returns
        -------
        sentence_id : int
            Sentence ID
        """
        return self.sentence_id

    def set_id(self, id):
        """Set sentence id

        Parameters
        ----------
        id : int
            Sentence ID
        """
        self.sentence_id = id

    def get_text(self):
        """Get sentence

        Returns
        -------
        text : str
            Sentence
        """
        return self.text

    def set_text(self, text):
        """Set sentence

        Parameters
        ----------
        text : str
            Sentence
        """
        self.text = text

    def get_cleaned_text(self):
        """Get cleaned sentence

        Returns
        -------
        cleaned text : str
            Cleaned sentence
        """
        return self.cleaned_text

    def set_cleaned_text(self, c_text):
        """Set cleaned sentence

        Parameters
        ----------
        c_text : str
            Cleaned sentence
        """
        self.cleaned_text = c_text

    def add_a_tag(self, tag):
        """Add a tag to the tags list

        Parameters
        ----------
        tag : str
            tag string
        """
        self.tags.append(tag)
    def remove_a_tag(self, tag):
        """Remove a tag from the list if exist
        Parameters
        ----------
        tag : str
            tag string
        """
        if tag in self.tags:
            self.tags.remove(tag)
            
    def get_tags(self):
        """Returns the list of tags for a sentence

        Returns
        -------
        tags : list of str
            list of tags for a sentence
        """
        return self.tags
