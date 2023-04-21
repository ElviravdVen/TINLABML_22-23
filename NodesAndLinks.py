side = 3

class Node:
        def __init__(self):
                self.links = []

        def getValue(self):
                sum = 0
                for link in self.links:
                        sum +=link.getValue()
                return sum

class Link:
        def __init__(self, inNode, outNode):
                self.weight = 1
                self.inNode = inNode

                outNode.links.append(self)

inNodes = [[Node () for column in range(side)] for row in range(side)]

'''
Bovenstaande code kan ook met de for loop uitgevoerd worden. Hieronder voor leesbaarheid.
inNodes = []
for rowIndex in range(side):
        row = []
        for columnIndex in range(side):
                row.append(Node())
        inNodes.append(row)
'''

outNodes = [Node () for i in range(2)]

links = []
for inRow in inNodes:
        for inNode in inRow:
                for outNode in outNodes:
                        links.append(Link(inNode, outNode))
