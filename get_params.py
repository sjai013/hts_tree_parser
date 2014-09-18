from QSTreeDiagram import QSTreeDiagram
from HMMFeatureParameters import HMMFeatureParameters
import sys

 # Print help message if not enough input parameters
if (len(sys.argv)) != 6:
    print "USAGE: main.py [INF FILE] [TRICKYPHONES] [LEAF PREFIX] [STATE] [FEATURE FILE]"
    print "\t\t [INF FILE] is the path to the input .inf question file."
    print "\t\t [TRICKYPHONES] is the path to the trickyphones.txt file"
    print "\t\t [LEAF PREFIX] is a prefix specific to the pdf type. E.g. mgc, lf0, str."
    print "\t\t [STATE] is the states for which to get generated parameters for."
    print "\t\t\t This should be enclosed in a string literal, with spaces to denote different states,"
    print "\t\t\t i.e. '2 3 4'"
    print "\t\t [FEATURE FILE] is the feature file output from OpenMARY (i.e. TARGETFEATURE output)"
    sys.exit()




# Load a hts question file (.inf)
inputFile = sys.argv[1]
#Tricky phones
trickyPhones = sys.argv[2]
# Look for "mgc" in leaf nodes - this should be modified based on which tree is being analysed
leafPrefix = sys.argv[3]
# State for which to draw diagram
states = map(int, sys.argv[4].split())
#Feature file
featFile = sys.argv[5]


tree = QSTreeDiagram(inputFile,trickyPhones,leafPrefix,  createTree=False)
params = HMMFeatureParameters(tree, leafPrefix, states,  featFile)

pdfs = params.GetParameters()
params.PrintLeafNodes()
