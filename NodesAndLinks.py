class Node:
	def __init__(self):
		self.links = []

class Link:
	def __init__(self, inNode, outNode):
		self.weight = 1
		self.inNode = inNode

		outNode.links.append(self)

inNodes = [Node () for i in range(9)]
outNodes = [Node () for i in range(2)]

links = []
for inNode in inNodes:
	for outNode in outNodes:
		links.append(Link(inNode, outNode))
