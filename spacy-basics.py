import spacy
# Load the Spanish model pipeline 
nlp = spacy.load('es_core_news_sm') # foccused on efficiency
# nlp = spacy.load('es_dep_news_trf') # foccused on accuracy

sentence = "Mi nombre es Juan y quiero comprar un boleto a Madrid"

def extract_tags(text):
    doc = nlp(text)
    tags = [(token.text, token.pos_) for token in doc]
    return tags

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage:
tags = extract_tags(sentence)
print('tags:',tags)
entities = extract_entities(sentence)
print('entities:',entities)