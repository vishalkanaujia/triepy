from trie import *

# Create the tree
mytrie = Trie()

# Get the input ready
s = "The quick brown fox jumps over the lazy dog"

toks = s.strip().split()

for tok in toks:
     # Insert key:value {word: meaning} in to tree
     mytrie.addWord(mytrie.rootNode, tok, "blabla")

# If search is successful, you will get meaning in
# a list
result = False
meaning = []
result = mytrie.search(mytrie.rootNode, "lazy", meaning)

# Output
print meaning
