#reuters contain news documents
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict


#create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda:0))
# print(model)

#Count frequency of co-occurance
for sentence in reuters.sents():
    for w1, w2, w3 in trigrams(sentence, pad_right = True, pad_left = True):
        model[(w1,w2)][w3] += 1
# print(model)

#Lets transform the count of probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count

# print(model)

#predicting the next word
word_1 = dict(model["today","the"])
# print(word_1)

#word 2
word_2 = dict(model["the","price"])
# print(word_2)

import random

#starting words

text = ["today","the"]
sentence_finished = False
while not sentence_finished:
    #select a random probability threshold
    r = random.random()
    accumulator = .0

    for word in model[tuple(text[-2:])].keys():
        accumulator += model[tuple(text[-2:])][word]
        #select words that are above the probability threshold
        if accumulator >= r:
            text.append(word)
            break

    if text[-2:] == [None,None]:
        sentence_finished = True

print(' '.join([t for t in text if t]))
