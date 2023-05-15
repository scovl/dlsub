import spacy
from spacy.util import minibatch, compounding
from spacy.training import Example

# Load the SpaCy model
nlp = spacy.load('pt_core_news_sm')

# Load the text data from a text file
with open('porta.txt', 'r') as file:
    text = file.read()

# Tokenize the text
doc = nlp(text)

# Generate training data
train_data = [(str(sent), {"tags": [token.pos_ for token in sent]}) for sent in doc.sents]

# Train the POS tagger
for i in range(10):
    losses = {}
    batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        texts, annotations = zip(*batch)
        examples = [Example.from_dict(nlp(text), annots) for text, annots in zip(texts, annotations)]
        nlp.update(examples, losses=losses)
    print('Loss:', losses)

# Save the model to a file
nlp.to_disk('nlp_model')
