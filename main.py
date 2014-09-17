from tree_parse import *
from tree_draw import *
import sys

# Print help message if not enough input parameters
if (len(sys.argv)) != 5:
    print "USAGE: main.py [INF FILE] [LEAF PREFIX] [STATE] [OUTPUT IMAGE]"
    print "\t\t [INF FILE] is the path to the input .inf question file."
    print "\t\t [LEAF PREFIX] is a prefix specific to the pdf type. E.g. mgc, lf0, str."
    print "\t\t [STATE] is the state for which to draw the output graphic for."
    print "\t\t [OUTPUT IMAGE] is the path of the output tree diagram"
    sys.exit()
    
# Load a hts question file (.inf)
inputFile = sys.argv[1]
# Look for "mgc" in leaf nodes - this should be modified based on which tree is being analysed
leafPrefix = sys.argv[2]
# State for which to draw diagram
state = int(sys.argv[3])
#Image path
outputGraphic = sys.argv[4]

data = LoadTree(inputFile)

matches = GetAllLeafNodes(leafPrefix,data)

state_data = data[state]
state_matches = matches[state]
pdfTrees = dict()
for i in range(len(state_matches.keys())):
    pdfName = state_matches.keys()[i]
    pdfTrees[pdfName] = GetQSListForPDF(pdfName,  state,  matches,  data)
    

DrawTree(state_data, pdfTrees, outputGraphic)
