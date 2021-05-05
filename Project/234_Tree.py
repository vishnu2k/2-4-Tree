from graphviz import Digraph, nohtml

class Node:
	deg = 4
	def __init__(self):
		self.numData = 0
		self.parent = None
		self.chid_nodes = []
		self.dataArray = []
		for j in range(self.deg):
			self.chid_nodes.append(None)
		for k in range(self.deg - 1):
			self.dataArray.append(None)

	def connectChild(self, childNum, pChild):
		self.chid_nodes[childNum] = pChild
		if pChild:
			pChild.parent = self

	def disconnectChild(self, childNum):
		pTempNode = self.chid_nodes[childNum]
		self.chid_nodes[childNum] = None
		return pTempNode

	def getChild(self, childNum):
		return self.chid_nodes[childNum]

	def getParent(self):
		return self.parent

	def isLeaf(self):
		return not self.chid_nodes[0]

	def getNumItems(self):
		return self.numData

	def getItem(self, index):	
		return self.dataArray[index]

	def isFull(self):
		return self.numData==self.deg - 1

	def findItem(self, key):	
		for j in range(self.deg-1):	
			if not self.dataArray[j]:	
				break	
			elif self.dataArray[j] == key:	
				return j
		return -1

	def insertItem(self, pNewItem):
		self.numData += 1
		newKey = pNewItem
		for j in reversed(range(self.deg-1)):	
			if self.dataArray[j] == None:	
				pass	
			else:	
				itsKey = self.dataArray[j]
				if newKey < itsKey:	
					self.dataArray[j+1] = self.dataArray[j]	
				else:
					self.dataArray[j+1] = pNewItem
					return j+1
		self.dataArray[0] = pNewItem	
		return 0


	def removeItem(self):	
		pTemp = self.dataArray[self.numData-1]	
		self.dataArray[self.numData-1] = None	
		self.numData -= 1
		return pTemp

	def displayNode(self):
		temp=[]
		for j in range(self.numData):
			temp.append(self.dataArray[j])
		return temp	


class Tree234:
	def __init__(self):
		self._pRoot = Node()	

	def find(self, key):
		pCurNode = self._pRoot	
		print("\nTraversal: ")
		while True:
			print(pCurNode.dataArray,end=" --> ")
			childNumber=pCurNode.findItem(key)
			if childNumber != -1:
				return childNumber	
			elif pCurNode.isLeaf():
				return -1
			else:	
				pCurNode = self.getNextChild(pCurNode, key)

	def insert(self, dValue):	
		pCurNode = self._pRoot
		pTempItem =dValue

		while True:
			if pCurNode.isFull():	
				self.split(pCurNode)	
				pCurNode = pCurNode.getParent()	
				pCurNode = self.getNextChild(pCurNode, dValue)
			elif pCurNode.isLeaf():
				break	
			else:
				pCurNode = self.getNextChild(pCurNode, dValue)
		pCurNode.insertItem(pTempItem)	


	def split(self, pThisNode):	
		pItemC = pThisNode.removeItem()	
		pItemB = pThisNode.removeItem()	
		pChild2 = pThisNode.disconnectChild(2)	
		pChild3 = pThisNode.disconnectChild(3)	
		pNewRight = Node()	

		if pThisNode == self._pRoot:	
			self._pRoot = Node()	
			pParent = self._pRoot	
			self._pRoot.connectChild(0, pThisNode)	
		else:	
			pParent = pThisNode.getParent()	

		itemIndex = pParent.insertItem(pItemB)	
		n = pParent.getNumItems()	
		j = n-1
		while j > itemIndex:	
			pTemp = pParent.disconnectChild(j)	
			pParent.connectChild(j+1, pTemp)	
			j -= 1

		pParent.connectChild(itemIndex+1, pNewRight)
		pNewRight.insertItem(pItemC)	
		pNewRight.connectChild(0, pChild2)	
		pNewRight.connectChild(1, pChild3)	

	def getNextChild(self, pNode, theValue):
		numItems = pNode.getNumItems()
		for j in range(numItems):	
			if theValue < pNode.getItem(j):	
				return pNode.getChild(j)	
		else:	
			return pNode.getChild(j + 1)	

	def displayTree(self):
		self.recDisplayTree(self._pRoot, 0, 0,None)

	def recDisplayTree(self, pThisNode, level, childNumber,parent):
		print ('level=', level, 'child=', childNumber,pThisNode.displayNode())	
		array.append([level,childNumber,pThisNode.displayNode(),parent])
		numItems = pThisNode.getNumItems()
		for j in range(numItems+1):
			pNextNode = pThisNode.getChild(j)
			if pNextNode:
				self.recDisplayTree(pNextNode, level+1, j, pThisNode.displayNode())
			else:
				visual(array)
				return
	
	def changetree(self,nTree):
		self._pRoot = nTree._pRoot

def visual(array):
	c=m=0
	s = Digraph('structs', filename='structs_revisited.gv',node_attr={'shape': 'record'},format='png')
	for i in range(len(array)):
		if m < array[i][0]:
			m=array[i][0]
		if len(array[i][2])==3:
			s.node('struct{}{}{}'.format(array[i][0],array[i][1],array[i][3]), '<f0> {}|<f1> {}|<f2> {}'.format(array[i][2][0],array[i][2][1],array[i][2][2]))
			c+=1
		if len(array[i][2])==2:
			s.node('struct{}{}{}'.format(array[i][0],array[i][1],array[i][3]), '<f0> {}|<f1> {}'.format(array[i][2][0],array[i][2][1]))
			c+=1
		if len(array[i][2])==1:
			s.node('struct{}{}{}'.format(array[i][0],array[i][1],array[i][3]), '<f0> {}'.format(array[i][2][0]))
			c+=1
	stack=[]
	stack.append(array[0])
	for i in range(1,len(array)):
		while len(stack)!=0 and stack[-1][2]!=array[i][3]:
			tmp=stack.pop()
		s.edges([('struct{}{}{}:f{}'.format(stack[-1][0],stack[-1][1],stack[-1][3],0), 'struct{}{}{}:f0'.format(array[i][0],array[i][1],array[i][3]))])
		stack.append(array[i])
	s.render("Project/Output")

pTree = Tree234()
iplist=[]
nTree=Tree234()

def show():
	pTree.displayTree()

def insert():
  value = list(map(int,(input('Enter value to insert: ').split())))
  for i in value:
    pTree.insert(i)
    iplist.append(i)

def find():
	value = int(input('Enter value to find: '))
	found = pTree.find(value)
	if found != -1:
		print ('Found', value)
	else:
		print('Could not find', value)

def remove():
	nTree = Tree234()
	if len(iplist)==0:
		print('cant remove,the tree is empty')
	else:
		value=int(input('Enter the value to be deleted: '))
		if iplist.__contains__(value):
			iplist.remove(value)
			pTree.changetree(nTree)
			for i in range(0,len(iplist)):
				pTree.insert(iplist[i])
		else:
			print('Could not find', value)

print("\nEnter: \n1 --> Insert\n2 -->Remove\n3 --> Find\nother --> Exit")
while(True):
	array=[]
	c=int(input("\nEnter the choice: "))
	print("\n")
	if(c==1):
		insert()
		show()
	elif(c==2):
		remove()
		show()
	elif(c==3):
		find()
	else:
		print("Terminating...\n")
		break

del pTree