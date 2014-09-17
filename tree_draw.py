'''
This module allows the drawing of HTS question trees.

MODULES REQUIRED:
    pydot (including all dependencies)
'''

import pydot

def DrawTree(questions, pdfTree,  saveAs):
    graph = pydot.Dot(graph_type='graph')
    
    # Add all questions as nodes 
    for i in range(len(questions)):
        nodeName = "qs%d" %i
        nodeLabel = "%s=%s" %(questions[i][0],  questions[i][1])
        graph.add_node(pydot.Node(nodeName, label=nodeLabel,style="filled", fillcolor="#ffaaaa"))
    
    # Add all pdfs as nodes
    for pdfName in pdfTree.keys():
        graph.add_node(pydot.Node(pdfName, label=pdfName,  style="filled",  fillcolor="#aaffaa"))
    
    # Draw edges (could merge this with above loop, but code is more readable this way)
    for pdfName in pdfTree.keys():
        for i in range(len(pdfTree[pdfName])-1):
            # Iterate through all questions for this output PDF, linking n with n+1
            node_this = "qs%d" %pdfTree[pdfName][i][0][0]
            node_next = "qs%d" %pdfTree[pdfName][i+1][0][0]
            qsAnswer = "{}".format(pdfTree[pdfName][i][1])
            edge_key = (node_this, node_next)
            # need to make sure edges doesn't exist, otherwise pydot draws multiple lines which look horrible
            if edge_key not in graph.obj_dict['edges'].keys():
                edge = pydot.Edge(node_this,  node_next,  label=qsAnswer)
                graph.add_edge(edge)
            
        # At end, draw the link between final node and leaf node
     
        
        node_this = node_next
        node_next = pdfName
        qsAnswer = "{}".format(pdfTree[pdfName][i+1][1])
        edge = pydot.Edge(node_this,  node_next,  label=qsAnswer)
        graph.add_edge(edge)
        
    
    graph.write_png(saveAs)
    print "File written to " + saveAs
    
