import debug
import sys

#Create a debug logger
d = debug.pydbg("trie")

class Node:
    def __init__(self, value, data=None):
        self.char = value
        # We intend to keep a list of values for a key
        self.data = []
        # XXX: List of Node
        self.children = []

class Trie:
    def __init__(self):
        self.rootNode = Node('0')

    def addWord(self, myNode, myString, meaning):
        lenString = len(myString)

        # Initialization
        l = 0
        temp  = myNode
        lastnode = myNode

        while l < lenString:
            # Get the list of Nodes and start adding nodes down in
            # the tree
            nodeList = temp.children
            found = 0
            if nodeList:
                lenList = len(nodeList)
                for i in xrange(lenList):
                    if (nodeList[i].char == myString[l]):
                        temp = nodeList[i]
                        found = 1

            # If not found, add a new node
            if found == 0:
                d.DLOG(0, "%s %s", "addWord", myString[l])
                t = Node(myString[l])
                (temp.children).append(t)
                temp = t

            lastnode = temp
            l += 1

        # Assign the meaning
        d.DLOG(0, "%s %s %s", lastnode.char, " => ", meaning)
        (lastnode.data).append(meaning)
        return

    def search(self, myNode, myString, meaning):
        # Get the string length
        slen = len(myString)

        # Start string search from the first node of TRIE
        idx  = 0
        result = self.findWord(myNode, myString, slen, idx, meaning)
        if 1 == result:
            return True

        return False

    def findWord(self, myNode, myString, slen, idx, meaning):
        if idx == slen:
            meaning.append(myNode.data)
            return 1

        nodeList = myNode.children
        for n in nodeList:
            d.DLOG(0, "%s %s %s %s", "findWord", n.char, "==", myString[idx])
            if (n.char == myString[idx]):
                if (1 == self.findWord(n, myString, slen, (idx + 1), meaning)):
                    return 1

        return 0

    def display(self, myNode, level):
        nodeList = myNode.children
        for n in nodeList:
            print n.data
            print "%d:%s", (level, n.char)
            self.display(n, level + 1)
