import nltk
from nltk import *

text="This is NLP chunking process task"

word=word_tokenize(text)

posTagss=pos_tag(word)

pattern="NP: {<DT>?<JJ>*<NN>}"

chunker=RegexpParser(pattern)
output =chunker.parse(posTagss)

print(output)
output.draw()