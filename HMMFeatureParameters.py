'''
This file is used to parse a set of existing features (generated using MARY), so that the actual path can be traversed in the tree
'''
class HMMFeatureParameters:
    feats = []
    tree = []
    leafPrefix = []
    states = []
    featsFile = ""
    leafNodes = []
    
    def __init__(self, tree, leafPrefix, states,  featsFile):
        self.tree = tree
        self.leafPrefix = leafPrefix
        self.states = states
        self.featsFile = featsFile
        self.ParseTree()
        
    def ParseTree(self):
        f = open(self.featsFile)
        raw_feats = f.read().split("\n\n")
        raw_feats.pop() # Remove last element (which is blank)
        
        #Split headers'
        raw_feats[0] = raw_feats[0].split("\n")
        
        #Remove non-feature text (i.e. "ByteValuedFeatureProcessor")
        for item in raw_feats[0]:
            if "FeatureProcessors" in item:
                raw_feats[0].remove(item)
        
        #Have to do this twice because for some reason, it doesn't pick up everything up first time
        for item in raw_feats[0]:
            if "FeatureProcessors" in item:
                    raw_feats[0].remove(item)
        
        for i in range(len(raw_feats[0])):
            raw_feats[0][i] = raw_feats[0][i].split()
            
        #Parse list of features (element [1] contains information on all items)
        raw_feats[1] = raw_feats[1].split("\n")
        for i in range(len(raw_feats[1])):
            raw_feats[1][i] = raw_feats[1][i].split()
        
        #Construct structure containing all features
        feats = []
        for model in raw_feats[1]:
            featList = dict()
            for i in range(len(model)):
                featList[raw_feats[0][i][0]] =  model[i]
            
            feats.append(featList)
                

        self.feats = feats
            
    def PrintLeafNodes(self):
        for i in range(len(self.leafNodes)):
            print_text = self.leafNodes[i][0]
            for key in self.leafNodes[i][1]:
                print_text += " " + self.leafNodes[i][1][key]
        
            print print_text
                    
            
    def GetParameters(self):
        leafNodes = []
        treeData = self.tree.treeData
        leafPrefix = self.leafPrefix
        states = self.states
        feats = self.feats
        
        for phoneFeats in feats:
            state_leaves = dict()
            for state in states:
                state_data = treeData[state]
       
                treeFinished = False
                thisQSNum = 0
                nextQSNum = 0
                while (not treeFinished):
                    thisQSNum = nextQSNum
                    thisQS = state_data[thisQSNum]
                    feat = thisQS[0]
                    if thisQS[1] == phoneFeats[feat]:
                        nextQSNum = thisQS[3]
                    else:
                        nextQSNum = thisQS[2]
                    
                    if type(nextQSNum) is not int:
                        state_leaves[state] = nextQSNum
                        treeFinished = True
                
            leafNodes.append([phoneFeats['phone'],  state_leaves])
            # Traverse features based on tree
        self.leafNodes = leafNodes
        return leafNodes    
