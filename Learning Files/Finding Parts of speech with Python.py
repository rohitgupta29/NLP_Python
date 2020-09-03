# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:40:03 2020

@author: infom
"""


from textblob import TextBlob

sentence = "The boy is running. The boys stopped to watch the bear."

tSentence = TextBlob(sentence)
# the abrivations are to be refered from Pann Tree Tagset.
#print(tSentence.tags)

wordSet = set()

for word, pos in tSentence.tags:
    if pos.startswith('NN'):
        #Lemmatize word
        lemmWord = word.lemmatize()
        wordSet.add(lemmWord)
        #print('Nouns : ')
        
        #print(lemmWord + "  :  " + pos)
        
#to get elements without duplicates      
print(wordSet)