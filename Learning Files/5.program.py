from textblob import TextBlob;
from textblob import Word;

str = "It is a cold afternoon. The cat is sleping. The cat ate some fish.";

theString = TextBlob(str);

#print(theString);
#print(theString.correct());

#for sentence in theString.sentences:
# 	print(sentence);

#print(theString.words.count('cat'));

#print(Word('cat').define());

print(Word('cat').pluralize());