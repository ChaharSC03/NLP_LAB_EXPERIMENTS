from nltk.tag import hmm
import nltk
# Train the HMM tagger
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(nltk.corpus.brown.tagged_sents(tagset='universal'))

print(tagger.confusion)
print("\n")
transition_matrix = tagger._transitions_matrix()
print(transition_matrix)

print("\n")
# Use the HMM tagger to predict the POS tags for a sequence of words
sentence = ['The', 'cat', 'sat', 'on', 'the', 'mat']
tags = tagger.tag(sentence)

emission_matrix = tagger._forward_probability(sentence)
print(emission_matrix)


print(tags)