from QSTreeDiagram import QSTreeDiagram
import sys

# Print help message if not enough input parameters
if (len(sys.argv)) != 6:
    print "USAGE: draw_tree.py [INF FILE] [TRICKYPHONES] [LEAF PREFIX] [STATE] [OUTPUT IMAGE]"
    print "\t\t [INF FILE] is the path to the input .inf question file."
    print "\t\t [TRICKYPHONES] is the path to the trickyphones.txt file"
    print "\t\t [LEAF PREFIX] is a prefix specific to the pdf type. E.g. mgc, lf0, str."
    print "\t\t [STATE] is the state/states for which to draw the output graphic for."
    print "\t\t\t This should be enclosed in a string literal, with spaces to denote different states,"
    print "\t\t\t i.e. '2 3 4'"
    print "\t\t [OUTPUT IMAGE PREFIX] is the path of the output tree diagram.."
    print "\t\t\t(actual name will be appended by '_[STATE].png'"
    print "EXAMPLE: draw_tree.py 'tree-mgc.inf' 'trickyPhones.txt' 'mgc' '2 3 5' './tree_mgc'"
    sys.exit()
else:
    # Load hts question file (.inf)
    inputFile = sys.argv[1]
    #Tricky phones
    trickyPhones = sys.argv[2]
    # Prefix for leaf nodes
    leafPrefix = sys.argv[3]
    # State(s) for which to draw diagram
    states = map(int, sys.argv[4].split())
    #Image path
    outputGraphicPrefix = sys.argv[5]
    
    print "[INF FILE] = ",  inputFile
    print "[TRICKYPHONES] = ",  trickyPhones
    print "[LEAF PREFIX] = ",  leafPrefix
    print "[STATES] = ",  states
    print "[OUTPUT IMAGE PREFIX] = ",  outputGraphicPrefix


tree = QSTreeDiagram(inputFile,trickyPhones,leafPrefix,  state=states)

for i in states:
    format = 'svg'
    outputFilename = outputGraphicPrefix + "_" + str(i) + "." + format
    tree.DrawTree(i, outputFilename,  format)
