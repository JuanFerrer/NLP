from textblob import TextBlob

# text = """Oh, Misty Eye of the mountain below,
# keep careful watch of my brothers' souls.
# And should the sky be filled with fire and smoke,
# keep watching over Durin's sons."""

text = "The quick brown fox jumps over the lazy dog."


blob = TextBlob(text);
tags = blob.tags

# for sentence in blob.sentences:
#     for word in sentence.words:
#         print word;

for tagPair in tags:
    print(tagPair[0] + " is " + tagPair[1])