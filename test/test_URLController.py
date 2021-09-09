#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import unittest

from models.Sentence import Sentence
from controllers.URLController import URLController

class TestURLController(unittest.TestCase):
    sent1 = Sentence('1.1', 'Pushed http://hg.mozilla.org/mozilla-central/rev/097598383614')
    sent2 = Sentence('1.2', '-pref(\"browser.gesture.twist.right\", \"Browser:NextTab\");')
    sent3 = Sentence('1.3', 'http://hg.mozilla.org/mozilla-central/rev/d19424342b43')
    sent4 = Sentence('1.4', 'http://hg.mozilla.org/releases/mozilla-1.9.1/rev/3329a3997d7b')
    sent5 = Sentence('1.5', 'https://bugzilla.mozilla.org/show_bug.cgi?id=502500')
    sent6 = Sentence('1.6', 'Added:     /-\\\\+[/-\\+]+[a-zA-Z0-9_!?\"|@~`$%&amp;()+;,.:&amp;lt;&amp;gt;=+-]')
    sent7 = Sentence('1.7', 'http://www.w3.org/International/questions/qa-bidi-css-markup')
    sent8 = Sentence('1.8', 'http://bugzilla.gnome.org/show_bug.cgi?id=357424')
    sent9 = Sentence('1.9', 'See http://gnomesupport.org/wiki/index.php/GnuCashPortingStatus for the porting status.')
    sent10 = Sentence('1.10', 'https://bugzilla.novell.com/show_bug.cgi?id=382360')
    sent11 = Sentence('1.11', 'C:\\JAWS510\\SETTINGS\\enu\\Default.JCF')
    sent12 = Sentence('1.12', 'PROPFIND /SOGo/dav/wsourdeau/Calendar/1D52AE6B-8564-0001-6A40-17B089902560/')
    sent13 = Sentence('1.13', 'x-webobjects-server-url: http://localhost')
    sent14 = Sentence('1.14', 'Pushed to comm-central &amp;lt;http://hg.mozilla.org/comm-central/rev/7e4da21b2924&amp;gt;')
    sent15 = Sentence('1.15', 'WebSVN link: http://websvn.kde.org/?view=rev&amp;revision=763132')
    
    def test_findURL(self):
        
        uc = URLController()
        
        uc.findURL(self.sent1)
        self.assertTrue('URL' in self.sent1.get_tags())
        uc.findURL(self.sent2)
        self.assertFalse('URL' in self.sent2.get_tags())
        uc.findURL(self.sent3)
        self.assertTrue('URL' in self.sent3.get_tags())
        uc.findURL(self.sent4)
        self.assertTrue('URL' in self.sent4.get_tags())
        uc.findURL(self.sent5)
        self.assertTrue('URL' in self.sent5.get_tags())
        uc.findURL(self.sent6)
        self.assertFalse('URL' in self.sent6.get_tags())      
        uc.findURL(self.sent7)
        self.assertTrue('URL' in self.sent3.get_tags())
        uc.findURL(self.sent8)
        self.assertTrue('URL' in self.sent4.get_tags())
        uc.findURL(self.sent9)
        self.assertTrue('URL' in self.sent5.get_tags())
        uc.findURL(self.sent10)
        self.assertTrue('URL' in self.sent10.get_tags())
        uc.findURL(self.sent11)
        self.assertFalse('URL' in self.sent11.get_tags())
        uc.findURL(self.sent12)
        self.assertFalse('URL' in self.sent12.get_tags())
        uc.findURL(self.sent13)
        self.assertTrue('URL' in self.sent13.get_tags())
        uc.findURL(self.sent14)
        self.assertTrue('URL' in self.sent14.get_tags())
        uc.findURL(self.sent15)
        self.assertTrue('URL' in self.sent15.get_tags())