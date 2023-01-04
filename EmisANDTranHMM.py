from collections import defaultdict

def calculate_probabilities(data):
    # Count the number of times each transition and emission occurs
    transition_counts = defaultdict(int)
    emission_counts = defaultdict(int)
    for sentence in data:
        for i in range(len(sentence)):
            word, tag = sentence[i]
            emission_counts[tag] += 1
            if i > 0:
                prev_tag = sentence[i-1][1]
                transition_counts[(prev_tag, tag)] += 1
    
    # Calculate the transition and emission probabilities
    transition_probs = defaultdict(float)
    emission_probs = defaultdict(float)
    for prev_tag, tag in transition_counts:
        transition_probs[(prev_tag, tag)] = transition_counts[(prev_tag, tag)] / emission_counts[prev_tag]
    for tag, count in emission_counts.items():
        emission_probs[tag] = count / sum(emission_counts.values())
    
    return transition_probs, emission_probs

# Calculate the transition and emission probabilities for the given data
data = [
    [('The', 'DET'), ('cat', 'NOUN'), ('sat', 'VERB'), ('on', 'ADP'), ('the', 'DET'), ('mat', 'NOUN')],
    [('The', 'DET'), ('dog', 'NOUN'), ('ran', 'VERB'), ('through', 'ADP'), ('the', 'DET'), ('garden', 'NOUN')]
]
transition_probs, emission_probs = calculate_probabilities(data)
print(transition_probs)
print(emission_probs)
