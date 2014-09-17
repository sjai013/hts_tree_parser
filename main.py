from tree_parse import *
from tree_draw import *

# Load a hts question file (.inf)
filename = "tree-mgc.inf"

# Look for "mgc" in leaf nodes - this should be modified based on which tree is being analysed
leafPrefix = "mgc"

data = LoadTree(filename)

matches = GetAllLeafNodes(leafPrefix,data)

state = 2
state_data = data[state]
state_matches = matches[state]
pdfTrees = dict()
for i in range(len(state_matches.keys())):
    pdfName = state_matches.keys()[i]
    pdfTrees[pdfName] = GetQSListForPDF(pdfName,  state,  matches,  data)
    

DrawTree(state_data, pdfTrees, '/home/sahil/Desktop/graph.png')
print "COMPLETE\n"
