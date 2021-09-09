#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import unittest

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence
from models.ListOfBugReports import ListOfBugReports


class TestSentence(unittest.TestCase):
    def test_get_id(self):
        """
        Test get_id returns the correct sentence ID
        """
        s = Sentence("1.1", "This is sample sentence text in a bug report turn/comment")
        self.assertEqual(s.get_id(), "1.1")
        self.assertNotEqual(s.get_id(), "1")

    def test_get_text(self):
        """
        Test get_text returns the correct text in text variable
        """
        s = Sentence("1.1", "This is sample sentence text in a bug report turn/comment")
        self.assertEqual(
            s.get_text(), "This is sample sentence text in a bug report turn/comment"
        )
        self.assertNotEqual(s.get_text(), "Different text")

    def test_get_cleaned_text(self):
        """
        Test get_cleaned_text returns the correct text in cleaned_text variable
        """
        s = Sentence("1.1", "This is sample sentence text in a bug report turn/comment")
        s.set_cleaned_text("sample sentence text bug report turn comment")
        self.assertEqual(
            s.get_cleaned_text(), "sample sentence text bug report turn comment"
        )
        self.assertNotEqual(
            s.get_cleaned_text(), "This sample sentence text bug report turn comment"
        )

    def test_set_id(self):
        """
        Test set_id assigns the correct sentence ID
        """
        s = Sentence("1.1", "This is sample sentence text in a bug report turn/comment")
        s.set_id("1.3")
        self.assertEqual(s.get_id(), "1.3")
        self.assertNotEqual(s.get_id(), "1.1")

    def test_set_text(self):
        """
        Test set_sentence assigns the correct text
        """
        s = Sentence("1.1", "This is sample sentence text in a bug report turn/comment")
        s.set_text("Different text to replace orignal sentence")
        self.assertEqual(s.get_text(), "Different text to replace orignal sentence")
        self.assertNotEqual(
            s.get_text(), "This is sample sentence text in a bug report turn/comment"
        )

    def test_set_cleaned_text(self):
        """
        Test set_cleaned_text assingns the correct cleaned text
        """
        s = Sentence("1.1", "This is sample sentence text in a bug report turn/comment")
        s.set_cleaned_text("sample sentence text bug report turn comment")
        self.assertEqual(
            s.get_cleaned_text(), "sample sentence text bug report turn comment"
        )
        self.assertNotEqual(
            s.get_cleaned_text(), "This sample sentence text bug report turn comment"
        )

    def test_remove_tag(self):
        s = Sentence('1.1', 'Expected results:')
        s.add_a_tag('C')
        
        self.assertTrue('C' in s.get_tags())
        
        s.remove_a_tag('C')

        self.assertTrue('C' not in s.get_tags())
        
class TestTurn(unittest.TestCase):
    def test_get_id(self):
        """
        Test get_id returns the correct turn ID
        """
        t = Turn(1, "John Doe", "2009-05-29 20:37:31")

        self.assertEqual(t.get_id(), 1)

    def test_get_author(self):
        """
        Test get_author returns the correct authro name
        """
        t = Turn(1, "John Doe", "2009-05-29 20:37:31")

        self.assertEqual(t.get_author(), "John Doe")

    def test_get_date_time(self):
        """
        Test get_date_time returns the correct date_time
        """
        t = Turn(1, "John Doe", "2009-05-29 20:37:31")

        self.assertEqual(t.get_date_time(), "2009-05-29 20:37:31")

    def test_set_id(self):
        """
        Test set_id assigns the value correctly
        """
        t = Turn(2, "John Doe", "2009-05-29 20:37:31")
        t.set_id(1)

        self.assertEqual(t.get_id(), 1)
        self.assertNotEqual(t.get_id(), 2)

    def test_set_author(self):
        """
        Test set_author assigns the value correctly
        """
        t = Turn(1, "John Doe", "2009-05-29 20:37:31")
        t.set_author("Joan Doe")

        self.assertEqual(t.get_author(), "Joan Doe")
        self.assertNotEqual(t.get_author(), "John Doe")

    def test_set_date_time(self):
        """
        Test set_date_time returns the correct date_time
        """
        t = Turn(1, "John Doe", "2009-05-29 20:37:31")
        t.set_date_time("2009-06-29 20:00:31")

        self.assertEqual(t.get_date_time(), "2009-06-29 20:00:31")
        self.assertNotEqual(t.get_date_time(), "2009-05-29 20:37:31")

    def test_number_of_sentences(self):
        """
        Test number_of_sentences returns the correct length of the list
        """
        s1 = Sentence("1.1", "Sample sentence 1")
        s2 = Sentence("1.2", "Sample sentence 2")

        t = Turn(1, "John Doe", "2009-05-29 20:37:31")

        self.assertEqual(t.number_of_sentences(), 0)

        t.add_a_sentence(s1)

        self.assertEqual(t.number_of_sentences(), 1)

        t.add_a_sentence(s2)

        self.assertEqual(t.number_of_sentences(), 2)


class TestBugReport(unittest.TestCase):
    
    def test_add_topics(self):
        """Test add_topics by checking the length and content of the topics list variable
        """
        br = BugReport("Search list has no history", 30252, "Firefox")
        br.add_topics(['form', 'results', 'history'])
        
        self.assertEqual(3, len(br.topics))
        self.assertTrue('form' in br.topics)
        self.assertTrue('results' in br.topics)
        self.assertTrue('history' in br.topics)
        
    def test_get_id(self):
        """
        Test get_id returns the correct bug report ID
        """
        br = BugReport("Search list has no history", 30252, "Firefox")

        self.assertEqual(br.get_bug_id(), 30252)

    def test_get_title(self):
        """
        Test get_title returns the correct title
        """
        br = BugReport("Search list has no history", 30252, "Firefox")

        self.assertEqual(br.get_title(), "Search list has no history")

    def test_get_product(self):
        """
        Test get_product returns the correct product name
        """
        br = BugReport("Search list has no history", 30252, "Firefox")

        self.assertEqual(br.get_product(), "Firefox")

    def test_set_id(self):
        """
        Test set_id assigns the value correctly
        """
        br = BugReport("Search list has no history", 30252, "Firefox")
        br.set_bug_id(40123)

        self.assertEqual(br.get_bug_id(), 40123)
        self.assertNotEqual(br.get_bug_id(), 30252)

    def test_set_title(self):
        """
        Test set_title assigns the value correctly
        """
        br = BugReport("Search list has no history", 30252, "Firefox")
        br.set_title("Search list history is empty")

        self.assertEqual(br.get_title(), "Search list history is empty")
        self.assertNotEqual(br.get_title(), "Search list has no history")

    def test_set_product(self):
        """
        Test set_date_time returns the correct date_time
        """
        br = BugReport("Search list has no history", 30252, "Firefox")
        br.set_product("Eclipse")

        self.assertEqual(br.get_product(), "Eclipse")
        self.assertNotEqual(br.get_product(), "Firefox")

    def test_number_of_turns(self):
        """
        Test number_of_turns returns the correct length of the list
        """
        s1 = Sentence("1.1", "Sample sentence 1")
        s2 = Sentence("1.2", "Sample sentence 2")
        s3 = Sentence("2.1", "Sample comment 1")

        t1 = Turn(1, "John Doe", "2009-05-29 20:37:31")
        t1.add_a_sentence(s1)
        t1.add_a_sentence(s2)

        t2 = Turn(2, "Joan Doe", "2009-06-29 20:39:31")
        t2.add_a_sentence(s3)

        br = BugReport("Search list has no history", 30252, "Firefox")

        self.assertEqual(br.number_of_turns(), 0)

        br.add_a_turn(t1)

        self.assertEqual(br.number_of_turns(), 1)

        br.add_a_turn(t2)

        self.assertEqual(br.number_of_turns(), 2)

    def test_get_a_turn(self):
        t1 = Turn(1, "John Doe", "2009-05-29 20:37:31")
        t2 = Turn(2, "Joan Doe", "2009-06-29 20:39:31")
        br = BugReport("Search list has no history", 30252, "Firefox")
        br.add_a_turn(t1)
        br.add_a_turn(t2)
        
        self.assertEqual(1, br.get_a_turn(1).get_id())
        self.assertEqual(2, br.get_a_turn(2).get_id())
        
if __name__ == "__main__":
    unittest.main()
