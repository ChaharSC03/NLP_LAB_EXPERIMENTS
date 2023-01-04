# https://www.holisticseo.digital/python-seo/nltk/wordnet#:~:text=NLTK%20Wordnet%20can%20be%20used,meanings%20within%20a%20lexical%20database.


import nltk
from nltk.corpus import wordnet

synonyms=[]
antonyms=[]

# input1=input("enter the word::");
input1="love"

#synonyms
for syn in wordnet.synsets(input1):
    for i in syn.lemmas():
        synonyms.append(i.name())

print(synonyms)

#antonyms

for syn in wordnet.synsets(input1):
    for i in syn.lemmas():
        if i.antonyms():
            antonyms.append(i.antonyms()[0].name())

print("\n")
print(antonyms)