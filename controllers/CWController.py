#!/usr/bin/env python

__author__ = 'Akalanka Galappaththi'
__email__ = 'a.galappaththi@uleth.ca'
__copyright__ = 'Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab'
__license__ = 'MIT'
__maintainer__ = 'Akalanka Galappaththi'

import networkx as nx
import matplotlib.pyplot as plt

from models.BugReport import BugReport
from models.Turn import Turn
from models.Sentence import Sentence
from models.ListOfBugReports import ListOfBugReports
from controllers.TextCleanController import TextCleanController


class CWController:
    """Find clue word based links between comments/turns in a bug report.    
    """

    def __init__(self):
        self.tcc = TextCleanController()

    def findLinks(self, bug_report):
        """Add the tag CW to a sentence if clue words found. Sentence was chosen if that is in the quotation graph.
        Parameters
        ----------
        bug_report : object
            BugReport object
        """
        G = self.createQuotationGraph(bug_report)
        nodes = G.nodes
        # print(nodes)

        # call this function to display graph
        # self.displayGraph(G)
        
        if not nx.is_empty(G):
            
            for node in nodes:
                # freq contains count of clue words in a sentence
                freq = 0
                
                turn = bug_report.get_a_turn(int(node.split('.')[0]))
                
                sentence = turn.get_a_sentence(node)
                # print('\n{}'.format(sentence.get_id()))
                
                if sentence is not None:
                    sentence.set_cleaned_text(self.tcc.clean_sentence(sentence.get_text(), r_punc=True, r_digit=True))
                    
                    words = list(sentence.get_cleaned_text().split())
                    # print('{}'.format(words))

                    # count matching words in predecessor nodes
                    pred = list(G.predecessors(node))
                    for p in pred:
                        pred_t = bug_report.get_a_turn(int(p.split('.')[0]))
                        pred_s = pred_t.get_a_sentence(p)

                        # print('{}'.format(pred))
                    
                        if pred_s is not None:
                            pred_s.set_cleaned_text(self.tcc.clean_sentence(pred_s.get_text(), r_punc=True, r_digit=True))
                            
                            pred_w = list(pred_s.get_cleaned_text().split())
                            for w in words:
                                if w in pred_w:
                                    freq += 1
                                    # print('{}:{}'.format(w,sentence.get_id()))
                    
                    # count matching words in successor nodes            
                    succ = list(G.successors(node))
                    for s in succ:
                        succ_t = bug_report.get_a_turn(int(s.split('.')[0]))
                        succ_s = succ_t.get_a_sentence(s)
                    
                        # print('{}'.format(succ))

                        if succ_s is not None:
                            succ_s.set_cleaned_text(self.tcc.clean_sentence(succ_s.get_text(), r_punc=True, r_digit=True))
                            
                            succ_w = list(succ_s.get_cleaned_text().split())
                            for w in words:
                                if w in succ_w:
                                    freq += 1
                                    # print('{}:{}'.format(w,sentence.get_id()))
                    
                    if freq >= 1:
                        if 'CW' not in sentence.get_tags():
                            sentence.add_a_tag('CW')
                        # if 'OT' in sentence.get_tags():
                        #     sentence.get_tags().remove('OT')
                        # if 'C' in sentence.get_tags():
                        #     sentence.get_tags().remove('C')
        
    
    def createQuotationGraph(self, bug_report):
        """Create and return the quotation graph for a bug report. Call supporting functions findQuotes and findOriginalSentences. 
        Parameters
        ----------
        bug_report : object
            BugReport object
        Returns
        -------
        G : graph object
            quotation graph
        """
        # list of nodes and edges for quotation graph
        nodes = []
        edges = []

        # flag indicates original sentence of the quoted sentence is found
        flag = False

        for turn in bug_report.get_turns():

            for sentence in turn.get_sentences():

                if self.findQuotes(sentence):
                    
                    curr_turn_id = turn.get_id()
                    flag = False
                    for i in range(curr_turn_id - 1, 0, -1):
                        prev_turn = bug_report.get_a_turn(i)
                        for sent in prev_turn.get_sentences():
                            if self.findOriginalSentence(sentence.get_text(), sent.get_text()):
                                                                
                                if sent.get_id() not in nodes:
                                    nodes.append(sent.get_id())
                                flag = True
                                if ('Org' not in sent.get_tags()):
                                    sent.add_a_tag('Org')
                                if ('QT' not in sentence.get_tags()):
                                    sentence.add_a_tag('QT')
                                break
                        if (flag == True):
                            # quote_sent_index contain the index of the array/list of that sentence
                            quote_sent_index = turn.get_sentences().index(sentence)
                            for j in range(quote_sent_index - 1, -1, -1):
                                if not self.findQuotes(turn.get_sentences()[j]):
                                    if (sent.get_id(), turn.get_sentences()[j].get_id()) not in edges:
                                        edges.append((turn.get_sentences()[j].get_id(),sent.get_id()))
                                else:
                                    break
                            for k in range(quote_sent_index + 1, len(turn.get_sentences())):
                                if not self.findQuotes(turn.get_sentences()[k]):
                                    if (
                                        sent.get_id(),
                                        turn.get_sentences()[k].get_id(),
                                    ) not in edges:
                                        edges.append(
                                            (
                                                turn.get_sentences()[k].get_id(),
                                                sent.get_id(),
                                            )
                                        )
                                else:
                                    break
                            break

        G = nx.DiGraph()

        G.add_edges_from(edges)

        return G

    def findQuotes(self, sentence):
        """Return true if a sentence is started with '>' otherwise false
        
        Parameters
        ----------
        sentence : object
            Sentence object
        Returns
        -------
        True/False : boolean
        """
        # use TextCleanController to convert html escape chars to its corresponding symbol
        
        sentence.set_cleaned_text(
            self.tcc.clean_sentence(sentence.text, r_digit=False, r_punc=False)
        )
        if len(sentence.get_cleaned_text()) != 0:
            if sentence.get_cleaned_text()[0] == '>':
                return True
            else:
                return False

    def findOriginalSentence(self, sent1, sent2, threshold=3):
        """Return true if the sent1 and sent2 has a matching sequence of words and the sequence length is longer than predefined threshold.
        
        Parameters
        ----------
        sent1 : str
            Quoted sentence
        sent2 : str
            Original sentence 
        Returns
        -------
        True/False : boolean
        """

        # of the sentence starts with > symbol it is not an original sentence
        # print('{}\n{}'.format(sent1, sent2))
        sent1 = self.tcc.clean_sentence(sent1, r_punc=False, r_digit=False, stop=False, lem=False)
        sent2 = self.tcc.clean_sentence(sent2, r_punc=False, r_digit=False, stop=False, lem=False)
        # print('{}\n{}'.format(sent1, sent2))
        if len(sent2) != 0 and sent2[0] == '>':
            return False

        # split the words in sentences because we are matching the common sub-substring based on words
        s1_words = sent1.split(' ')
        s2_words = sent2.split(' ')
        
        start_pos = 0  # starting position of sub-string in original sentence
        seq_length = 0  # length of the word sequence
        longest_seq_length = 0

        for x in range(0, len(s1_words)):
            if s1_words[x] in s2_words:
                start_pos = s2_words.index(s1_words[x])
            else:
                continue  # if the word doesn't exist in the original sentence ignore the word and search again with next word
            
            
            seq_length = 0
            for y in range(start_pos, len(s2_words)):
                if s1_words[x] == s2_words[y]:
                    seq_length += 1
                    if x < len(s1_words) - 1:
                        x += 1  # match the next word in the quoted sentences
                    else:
                        break  # break when x pointing to the last word in the list
                    y += 1
                else:
                    break  # if no match start a new sequence
            
            if longest_seq_length < seq_length:
                longest_seq_length = seq_length

        if longest_seq_length > threshold:
            return True
        else:
            return False

    def displayGraph(self, G):
        nx.draw(G, pos=nx.circular_layout(G, scale=1, center=None), font_size=8, with_labels=True)
        plt.show()