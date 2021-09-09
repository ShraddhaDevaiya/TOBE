#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import unittest

import emoji
import string
import re
import codecs

from controllers.TextCleanController import TextCleanController


class TestTextCleanController(unittest.TestCase):
    def test_remove_emoji(self):
        text = "&amp;gt; ID=23415, 2001-11-12 I MISS THE OLD TOP GEAR😭😭😭😭 What a shame!!!. blaa, bla-blaa, bla-bla-blaa....."

        tcc = TextCleanController()
        actual = tcc.remove_emoji(text)
        expected = "&amp;gt; ID=23415, 2001-11-12 I MISS THE OLD TOP GEAR What a shame!!!. blaa, bla-blaa, bla-bla-blaa....."
        self.assertEqual(actual, expected)

    def test_remove_punctuations(self):
        text = "> &amp;gt; ID=23415, 2001-11-12 I MISS THE OLD TOP GEAR😭😭😭😭. What a shame!!!. blaa, bla-blaa, bla-bla-blaa......"
        
        tcc = TextCleanController()
        actual = tcc.remove_punctuations(text, ex_punc = [">"])
        expected = ">  amp gt  ID 23415  2001 11 12 I MISS THE OLD TOP GEAR😭😭😭😭  What a shame     blaa  bla blaa  bla bla blaa      "
        self.assertEqual(actual, expected)

    def test_remove_digits(self):
        text = "&amp;gt; ID=23415, 2001-11-12 I MISS THE OLD TOP GEAR😭😭😭😭 What a shame!!!. blaa, bla-blaa, bla-bla-blaa....."

        tcc = TextCleanController()
        actual = tcc.remove_digits(text)
        expected = "&amp;gt; ID=, -- I MISS THE OLD TOP GEAR😭😭😭😭 What a shame!!!. blaa, bla-blaa, bla-bla-blaa....."
        self.assertEqual(actual, expected)

    def test_convert_html_escape_char(self):
        text = "&amp;gt; ID=23415, 2001-11-12 I MISS THE OLD TOP GEAR😭😭😭😭 What a shame!!!. blaa, bla-blaa, bla-bla-blaa....."

        tcc = TextCleanController()
        actual = tcc.convert_html_escape_char(text)
        expected = "> ID=23415, 2001-11-12 I MISS THE OLD TOP GEAR😭😭😭😭 What a shame!!!. blaa, bla-blaa, bla-bla-blaa....."
        self.assertEqual(actual, expected)

    def test_custom_text_cleaner(self):
        text = "The method FolderDescription#createExistentResourceFromHandle(IResource,IProgressMonitor) checks if the folder already exists and returns immediately if so."
        tcc = TextCleanController()

        actual = tcc.clean_sentence(text, r_digit=True, r_punc=True, stop=True, lem=True, escape=False)
        expected = "method folderdescription createexistentresourcefromhandle iresource iprogressmonitor  check folder exists return immediately so"
        self.assertEqual(actual, expected)

    def test_text_lemmatizer(self):
        words = ['localization', 'localizer', 'scaling']
        text = 'When images are rescaled now the GIMP always defaults to linear scaling.'
        text2 = 'Remember last scale method setting'
        text3 = 'Once you localize a page we ship, you would then set the dir from ltr to rtl.'
        text4 = 'localization state, and just rely on them completing all the localization work to make it look decent.'

        tcc = TextCleanController()
        expected = ['local', 'scale', 'localize']
        exp_text = 'image rescale gimp default linear scaling'
        exp_text2 = 'remember scale method set'
        exp_text3 = 'localize page ship  set dir ltr rtl'
        exp_text4 = 'localize state  rely complete localize work make decent'

        self.assertEqual(tcc.clean_sentence(words[0]), expected[2])
        # self.assertEqual(tcc.clean_sentence(words[1]), expected[0])
        self.assertEqual(tcc.clean_sentence(words[2]), expected[1])
        self.assertEqual(tcc.clean_sentence(text, r_punc=True, r_digit=True, stop=True, lem=True), exp_text)
        self.assertEqual(tcc.clean_sentence(text2, r_punc=True, r_digit=True, stop=True, lem=True), exp_text2)
        self.assertEqual(tcc.clean_sentence(text3, r_punc=True, r_digit=True, stop=True, lem=True), exp_text3)
        self.assertEqual(tcc.clean_sentence(text4, r_punc=True, r_digit=True, stop=True, lem=True), exp_text4)

    def test_get_wordnet_pos(self):

        word_list = ["shooting", "flowers", "are", "buses", "cuts", "played", "playing"]
        tag_list = ["v", "n", "v", "n", "n", "n", "v"]
        tcc = TextCleanController()

        for i in range(len(word_list)):
            actual = tcc.get_wordnet_pos(word_list[i])
            self.assertEqual(actual, tag_list[i])


    # def test_convert_escape_char(self):
    #     text = "2) form history finds 1 entry (\"blah\"), search-suggestions finds \"baaa\", \"bloop\", \"bzzz\", the autocompete menu shows these in order with a divider between \"blah\" and \"baaa\"."
        
    #     tcc = TextCleanController()
    #     actual = tcc.convert_escape_char(text)
    #     # expected = "2) form history finds 1 entry ("blah"), search-suggestions finds "baaa", "bloop", "bzzz", the autocompete menu shows these in order with a divider between "blah" and "baaa"."

    #     # self.assertEqual(actual, expected)
    #     print(text)
    #     print(actual)

    

    # def test_clean_sentence(self):
        # text = "&amp;gt; ID=23415, 2001-11-12 I MISS THE OLD TOP GEAR😭😭😭😭 What a shame!!!. blaa, bla-blaa, bla-bla-blaa....."
        # text2 = "-pref(\"browser.gesture.twist.right\", \"Browser:NextTab\");"
        # text3 = 'Added:     /-\\\\+[/-\\+]+[a-zA-Z0-9_!?\"|@~`$%&amp;()+;,.:&amp;lt;&amp;gt;=+-]'
        # text4 = 'Steps to Reproduce:'
        # text5 = 'Expected results:'
        
        # tcc = TextCleanController()
        # actual = tcc.clean_sentence(text, r_punc=False, escape=True, ex_punc=[">"])
        # expected = "> id=, -- miss top gear shame!!!. blaa, bla-blaa, bla-bla-blaa....."
        # self.assertEqual(actual, expected)

        # actual = tcc.clean_sentence(text, ex_punc=[">", "-", "="])
        # expected = "> id= -- miss top gear shame blaa bla-blaa bla-bla-blaa"
        # self.assertEqual(actual, expected)

        # actual = tcc.clean_sentence(text, r_digit=False, ex_punc=[">"])
        # expected = "> id23415 20011112 miss top gear shame blaa blablaa blablablaa"
        # self.assertEqual(actual, expected)
        
        # actual = tcc.clean_sentence(text2, r_punc=False)
        # expected = "-pref(\"browser.gesture.twist.right\", \"browser:nexttab\");"
        # self.assertEqual(actual, expected)

        # actual = tcc.clean_sentence(text3, r_digit=False, r_punc=False)
        # expected = 'added: /-\\\\+[/-\\+]+[a-za-z0-9_!?\"|@~`$%&()+;,.:<>=+-]'
        # self.assertEqual(actual, expected)
        
        # actual = tcc.clean_sentence(text4, r_digit=False, r_punc=False)
        # expected = 'step reproduce:'
        # self.assertEqual(actual, expected)
        
        # actual = tcc.clean_sentence(text5, r_digit=False, r_punc=False)
        # expected = 'expect results:'
        # self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()