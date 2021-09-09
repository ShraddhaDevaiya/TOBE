#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag
import emoji
import string
import re
import os
import csv
import html
import codecs

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence
from models.ListOfBugReports import ListOfBugReports


class TextCleanController:
    """Remove irrelevant charachter, stopwords and lematize words.
    """

    def __init__(self):
        pass

    def clean_sentence(self, sentence, r_digit=True, r_punc=True, stop=True, lem=True, escape=False, ex_punc=[]):
        """Clean a sentence
        Parameters
        ----------
        sentence : str
            Sentence
        r_digit : boolean
            Parameter default is True to remove digits. False indicates not to remove digits.
        r_punc : boolean
            Parameter default is True to remove punctuations. False indicates not to remove punctuations.
        escape : boolean
            Parameter default is False. Set to True to remove the slash from  \".
        ex_punc : list
            List of punctuations need to be remain in the sentence
        Returns
        -------
        cleaned_sentence : str
            Sentence in lower case after removing emojis, punctuations, digits, stopwords, and convert to origin
            html escape char and orgina root word form
        """
        wordnet_lemmatizer = WordNetLemmatizer()
        english_stopwords = stopwords.words("english")

        # extending stopword list
        curr_dir = os.getcwd()
        stopword_path = os.path.join(curr_dir, "data", "smart_stop_words.csv")
        
        with open(stopword_path, 'r') as stopword_file:
            csv_file = csv.reader(stopword_file)
            for row in csv_file:
                english_stopwords.extend(row)
                    
        tokens = sentence.split()

        if r_punc == True:
            tokens = [self.remove_punctuations(token, ex_punc) for token in tokens]

        if r_digit == True:
            tokens = [self.remove_digits(token) for token in tokens]

        tokens = [self.remove_emoji(token) for token in tokens]

        tokens = [self.convert_html_escape_char(token) for token in tokens]

        tokens = [self.convert_escape_char(token) for token in tokens]

        if stop == True:
            tokens = [token for token in tokens if token.lower() not in english_stopwords]

        if lem == True:
            tokens = [
                wordnet_lemmatizer.lemmatize(
                    token.lower(), self.get_wordnet_pos(token.lower())
                )
                for token in tokens
            ]

        cleaned_sentence = " ".join(tokens)

        cleaned_sentence = cleaned_sentence.strip()

        return cleaned_sentence

    def convert_html_escape_char(self, sentence):
        """Convert html escape char to its symbol
        Parameters
        ----------
        sentence : str
            Sentence
        Returns
        -------
        sentence : str
            Sentence with converted html escape characters 
        """
        count = 0
        while count < 2:
            sentence = html.unescape(sentence)
            count += 1

        return sentence

    def get_wordnet_pos(self, word):
        """Map POS tag to first character lemmatize() accepts. 
        If no match wordnet.NOUN is the default value.
        
        Parameters
        ----------
        word : str
            Word
        Returns
        -------
        POS tag : wordnet POS tag
            Wordnet part of speach tag of the word 
        """
        tag = pos_tag([word])[0][1][0].upper()
        tag_dict = {
            "J": wordnet.ADJ,
            "N": wordnet.NOUN,
            "V": wordnet.VERB,
            "R": wordnet.ADV,
        }

        return tag_dict.get(tag, wordnet.NOUN)

    def remove_emoji(self, word):
        """Removes emojis from the text.
        
        Parameters
        ----------
        word : str
            Word
        Returns
        -------
        text : str
            Text with no emojis.
        """
        return emoji.get_emoji_regexp().sub(u"", word)

    def remove_punctuations(self, word, ex_punc):
        """Removes punctuations form the text.
        
        Parameters
        ----------
        word : str
            Word
        ex_punc : list
            list of punctuations that will be remain in the text
        Returns
        -------
        text : str
            Text with no punctuations.
        """
        new_punc_list = string.punctuation
        if len(ex_punc) != 0:
            for i in ex_punc:
                new_punc_list = new_punc_list.replace(i, "")
        regex = re.compile("[%s]" % re.escape(new_punc_list))
        return regex.sub(" ", word)

    def remove_digits(self, word):
        """
        
        Parameters
        ----------
        word : str
            Word
        Returns
        -------
        text : str
            Text with no digits.
        """
        return word.translate(str.maketrans("", "", string.digits))

    def convert_escape_char(self, sentence):
        """Convert escape chars to regular chars

        Parameters
        ----------
        sentence : str
            Sentence
        Returns
        -------
        sentence : str
            Sentence with converted escape characters

        """
        return codecs.getdecoder("unicode_escape")(sentence)[0]
