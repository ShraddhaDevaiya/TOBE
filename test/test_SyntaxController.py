#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

import unittest

from models.Sentence import Sentence
from controllers.SyntaxController import SyntaxController

class TestSyntaxController(unittest.TestCase):
    
    def test_findSyntax(self):
        syc = SyntaxController()
        
        sent1 = Sentence('1.1', 'Cc[\"@mozilla.org/browser/sessionstore;1\"].')
        syc.findSyntax(sent1)
        self.assertTrue('C' in sent1.get_tags())
        
        sent2 = Sentence('1.1', 'getService(Ci.nsISessionStore).')
        syc.findSyntax(sent2)
        self.assertTrue('C' in sent2.get_tags())
        
        sent3 = Sentence('1.1', 'getClosedTabCount(window) == 0;')
        syc.findSyntax(sent3) 
        self.assertTrue('C' in sent3.get_tags())
        
        sent4 = Sentence('1.1', 'this.mUndoCloseTabMenuItem.hidden =')
        syc.findSyntax(sent4)
        self.assertTrue('C' in sent4.get_tags())
        
        sent5 = Sentence('1.1', '-pref(\"browser.gesture.twist.right\", \"Browser:NextTab\");')
        syc.findSyntax(sent5)
        self.assertTrue('C' in sent5.get_tags())
        
        sent6 = Sentence('1.1', 'Pinching is a natural gesture for page zoom (and more widely used/known), with a low penalty for accidentally triggering.')
        syc.findSyntax(sent6)
        self.assertFalse('C' not in sent6.get_tags())
        
        sent7 = Sentence('1.1', 'return render_template(\'display.html\', response = deserialized_bug_data[\'list_of_turns\'])')
        syc.findSyntax(sent7)
        self.assertTrue('C' in sent7.get_tags())
        
        sent8 = Sentence('1.1', 'IFile file = folder.getFile(...);')
        syc.findSyntax(sent8)
        self.assertTrue('C' in sent8.get_tags())
        
        sent9 = Sentence('1.1', 'op1.execute(...);')
        syc.findSyntax(sent9)
        self.assertTrue('C' in sent9.get_tags())
        
        sent10 = Sentence('1.1', '* app/dialogs/scale-dialog.h: removed GimpScaleCallback typedef.')
        syc.findSyntax(sent10)
        self.assertTrue('C' in sent10.get_tags())
        
        sent11 = Sentence('1.1', '* app/dialogs/image-scale-dialog.[ch]: made the ImageScaleDialog struct private, return a GtkWidget* from image_scale_dialog_new() and use a GimpScaleCallback in the public API.')
        syc.findSyntax(sent11)
        self.assertTrue('C' in sent11.get_tags())

        sent12 = Sentence('1.1', 'Created an attachment (id=380567) [details] Patch v.1 (WIP)')
        syc.findSyntax(sent12)
        self.assertTrue('C' not in sent12.get_tags())

        sent13 = Sentence('1.1', 'Pushed http://hg.mozilla.org/mozilla-central/rev/097598383614')
        sent13.add_a_tag('URL')
        syc.findSyntax(sent13)
        self.assertTrue('C' not in sent13.get_tags())
        
        sent14 = Sentence('1.1', 'Created an attachment (id=380567)')
        syc.findSyntax(sent14)
        self.assertTrue('C' not in sent14.get_tags())

        sent15 = Sentence('1.1', 'Created an attachment (id=380567) [details]')
        syc.findSyntax(sent15)
        self.assertTrue('C' not in sent15.get_tags())