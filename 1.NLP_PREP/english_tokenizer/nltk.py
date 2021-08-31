from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


sentence = "Natural language processing (NLP) is a subfield of computer science, information engineering, " \
           "and artificial intelligence concerned with the interactions between computers and human (natural) languages, " \
           "in particular how to program computers to process and analyze large amounts of natural language data."

print(word_tokenize(sentence))


paragraph = "Natural language processing (NLP) is a subfield of computer science, information engineering, " \
            "and artificial intelligence concerned with the interactions between computers and human (natural) languages, " \
            "in particular how to program computers to process and analyze large amounts of natural language data. Challenges " \
            "in natural language processing frequently involve speech recognition, natural langauge understanding, " \
            "and natural language generation."

print(sent_tokenize(paragraph))