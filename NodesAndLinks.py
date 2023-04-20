side = 3

class Node:
        def __init__(self):
                self.links = []

class Link:
        def __init__(self, inNode, outNode):
                self.weight = 1
                self.inNode = inNode

                outNode.links.append(self)

inNodes = [[Node () for column in range(side)]for row in range(side)]
outNodes = [Node () for i in range(2)]

links = []
for inRow in inNodes:
        for inNode in inRow:
                for outNode in outNodes:
                        links.append(Link(inNode, outNode))
