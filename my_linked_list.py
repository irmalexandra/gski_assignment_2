
class LinkedList():
    
    class __Node():
        def __init__(self, data, nextNode = None):
            self.data = data
            self.__nextNode = nextNode

        def getStrData(self, returnStr = ""):
            if self.__nextNode == None:
                return str(self.data)
            else:
                return str(self.data) + " " + self.getNextNode().getStrData(returnStr)
                
        def setNextNode(self, nextNode):
            self.__nextNode = nextNode

        def getNextNode(self):
            return self.__nextNode

    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def __str__(self):
        if self.front != None:
            return self.front.getStrData()
        else:
            return ""

    def pushBack(self, data):
        newNode = self.__Node(data)
        newNode.setNextNode(None)
        if self.back != None:
            self.back.setNextNode(newNode)
        self.back = newNode

        if self.size == 0:
            self.front = newNode

        self.size += 1

    def pushFront(self, data):
        newNode = self.__Node(data)
        newNode.setNextNode(self.front)
        self.front = newNode
        
        if self.size == 0:
            self.back = newNode
        
        self.size += 1

    def popFront(self):
        if self.size >= 1:
            returnData = self.front.data
            self.front = self.front.getNextNode()
            self.size -= 1
        else:
            returnData = None

        return returnData

    def getSize(self):
        return self.size
        

    # FUNCTION IMPLEMENTED ONLY FOR PALINDROME PART OF THE ASSIGNMENT
    def getNode(self):
        return self.front
    



# newLinkedList = LinkedList()

# print(newLinkedList.popFront())

# for i in range(10):
#     if i % 2 == 0:
#         newLinkedList.pushFront(i)
#     else:
#         newLinkedList.pushBack(i)
    
#     print(newLinkedList)

# print()



