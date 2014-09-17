from tree_parse import *
from tree_draw import *
from parse_feats import *
import sys



# Print help message if not enough input parameters
if (len(sys.argv)) != 6:
    print "USAGE: main.py [INF FILE] [TRICKYPHONES] [LEAF PREFIX] [STATE] [OUTPUT IMAGE]"
    print "\t\t [INF FILE] is the path to the input .inf question file."
    print "\t\t [TRICKYPHONES] is the path to the trickyphones.txt file"
    print "\t\t [LEAF PREFIX] is a prefix specific to the pdf type. E.g. mgc, lf0, str."
    print "\t\t [STATE] is the state for which to draw the output graphic for."
    print "\t\t [OUTPUT IMAGE] is the path of the output tree diagram"
    sys.exit()
    
# Load a hts question file (.inf)
inputFile = sys.argv[1]
#Tricky phones
trickyPhones = sys.argv[2]
# Look for "mgc" in leaf nodes - this should be modified based on which tree is being analysed
leafPrefix = sys.argv[3]
# State for which to draw diagram
state = int(sys.argv[4])
#Image path
outputGraphic = sys.argv[5]


feats = ParseTree("targetFeat.txt")

data = LoadTree(inputFile,  trickyPhones)

matches = GetAllLeafNodes(leafPrefix,data)

state_data = data[state]

pdfs = GetTreeLeaf(feats, state_data, leafPrefix)

for  pdf in pdfs:
    print pdf

state_matches = matches[state]
pdfTrees = dict()
for i in range(len(state_matches.keys())):
    pdfName = state_matches.keys()[i]
    pdfTrees[pdfName] = GetQSListForPDF(pdfName,  state,  matches,  data)
    

DrawTree(state_data, pdfTrees, outputGraphic)
