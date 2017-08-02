from pattern.en import parse
from pattern.en import parsetree
import json

text1 = """Oh, misty eye of the mountain below,
keep careful watch of my brothers' souls.
And should the sky be filled with fire and smoke,
keep watching over Durin's sons."""

text1 = "Keep careful watch of my brother's soul"

text = "I love this big sky, and this dumb lizard."
text1 = "I want to go home"
text1 = "It had been a wonderful night"
text1 = "Tahm is fat"
text1 = "The quick brown fox jumped over the lazy dog"

# tokens = parse(text, relations=True).split()[0]
tokens = parsetree(text, relations=True)
sentence = {}
nouns = []
verbs = []
adjectives = []

print text

for s in tokens:
    for chunk in s.chunks:
        print "Chunk:           " + chunk.string + "\n  Role: " + str(chunk.role) + "\n     Related to: " + str(chunk.related)
        adjectives = []
        if chunk.type == "VP":
            verbs.append(chunk.string)
        else:
            for word in chunk.words:
                if word.type.startswith("NN") or word.type.startswith("PRP"):
                    nouns.append(word.string)
                    sentence[word.string] = {}
                    sentence[word.string]["attributes"] = adjectives
                    sentence[word.string]["actions"] = []
                    sentence[word.string]["actionsReceived"] = []
                    # Decide whether the object acts or is acted upon
                    if len(chunk.related) > 0:
                        for r in chunk.related:
                            if str(r.type).startswith("VP"):
                                if str(chunk.role) == "SBJ":
                                    sentence[word.string]["actions"].append(r.string)
                                elif str(chunk.role) == "OBJ":
                                    sentence[word.string]["actionsReceived"].append(r.string)
                elif word.type.startswith("JJ"):
                    adjectives.append(word.string)
                elif word.type.startswith("VB"):
                    verbs.append(word.string)
                elif word.type.startswith("ASD"):
                    pass

print json.dumps(sentence, indent=2)
