#!/usr/bin/env python

__author__ = "Akalanka Galappaththi"
__email__ = "a.galappaththi@uleth.ca"
__copyright__ = "Copyright 2020, The Bug Report Summarization Project @ Sybil-Lab"
__license__ = "MIT"
__maintainer__ = "Akalanka Galappaththi"

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
import gensim
import gensim.corpora as corpora
import os
import re
# import pyLDAvis.gensim

from models.Sentence import Sentence
from models.Turn import Turn
from models.BugReport import BugReport
from controllers.TextCleanController import TextCleanController

class TopicModelController:
    """Extract topic words from a bug report
    """
    
    def __init__(self):
        self.id2word = dict()
        self.lda_model = object
    
    def extractTopics(self, bug, numTopics = 1):
        """Extract topcs and return list of topics words
        Parameters
        ----------
        bug : object
            BugReport object
        numTopics : int
            Number of topics that will be extracted from the bug report
        Returns
        -------
        topics : numpy.ndarray
            Multimdeminsion array of topic words of each topic.
        """
        tcc = TextCleanController()
        
        # list contains all words of a bug report after cleaning
        # This will be used to create the bug report corpus
        all_words = []
        
        for turn in bug.get_turns():
            for sent in turn.get_sentences():
                temp_tags = sent.get_tags()
                if 'OT' not in temp_tags and 'C' not in temp_tags and 'URL' not in temp_tags:
                    sent.set_cleaned_text(tcc.clean_sentence(sent.get_text()))
                    all_words.append(sent.get_cleaned_text().split())
        
        self.id2word = corpora.Dictionary(all_words)
        
        corpus = [self.id2word.doc2bow(word) for word in all_words]
        
        self.lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                    id2word=self.id2word,
                                                    num_topics=numTopics,
                                                    random_state=100,
                                                    update_every=1,
                                                    chunksize=100,
                                                    passes=10,
                                                    alpha='auto',
                                                    per_word_topics=True)
        
        # lda_display = pyLDAvis.gensim.prepare(self.lda_model, corpus, self.id2word)
        
        # curr_dir = os.getcwd()
        # file_name = 'topic'+str(numTopics)+'.html'
        # topic_html = os.path.join(curr_dir, 'view', file_name)
        # pyLDAvis.save_html(lda_display, topic_html)
        
        # coherence_model_lda = gensim.models.CoherenceModel(model=self.lda_model, texts=all_words, dictionary=self.id2word, coherence='c_v')
        # coherence_lda = coherence_model_lda.get_coherence()
        
        # return self.lda_model.show_topics(), self.lda_model.log_perplexity(corpus), coherence_lda
        
        return self.lda_model.show_topics()
      
    # This function works when numTopics > 1    
    def findTopicSimilarity(self, bug, topics):
        """Compare each sentence with topics to determine topic similarity. If similarity score is high assign tag 'Topic'
        Parameters
        ----------
        bug : object
            BugReport object
        topics : numpy.ndarray
            List of topic words of each topic
        """
        for turn in bug.get_turns():
            for sent in turn.get_sentences():
                temp_tags = sent.get_tags()
                if 'OT' not in temp_tags and 'Code' not in temp_tags and 'URL' not in temp_tags:
                    sent_words = [sent.get_cleaned_text().split()]
                    sent2bow = [self.id2word.doc2bow(word) for word in sent_words]
                    
                    #print('{} : {}'.format(sent.get_id(),self.lda_model.get_document_topics(sent2bow)))
                    for prob in self.lda_model.get_document_topics(sent2bow):
                        print('{} : {}'.format(sent.get_id(),prob))
    
    
    # Find topic word coorccurrences in sentences
    def findTopicWordMatches(self, bug, topics):
        """Compare each sentence with topic words to find word cooccurrencess. If more than 2 topic words appear add tag 'Topic'
        Parameters
        ----------
        bug : object
            BugReport object
        topics : numpy.ndarray
            List of topic words of each topic
        """
        
        topic_words = re.findall(r'\b[a-z]+\b', topics[0][1])
        # print(topic_words)
        
        # add the topic words to bug report object
        bug.add_topics(topic_words)
        
        count = 0
        for turn in bug.get_turns():
            for sent in turn.get_sentences():
                temp_tags = sent.get_tags()
                if 'OT' not in temp_tags and 'URL' not in temp_tags:
                    # need to get the 0th index becuase the list is inside a list
                    sent_words = [sent.get_cleaned_text().split()][0]
                    # print(sent_words)
                    for word in topic_words:
                        for w in sent_words:
                            if word == w:
                                count += 1
                    # print(count)
                    if count > 2:
                        if 'Topic' not in sent.get_tags():
                            sent.add_a_tag('Topic')
                count = 0
                    