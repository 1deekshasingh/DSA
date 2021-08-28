class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        # self.previous = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None

    def printAllElements(self):
        temp = self.head
        while temp is not None:
            print(temp.data , end = '-->')
            temp = temp.next
        print()

    def countNodes(self):
        lenCount = 0
        temp = self.head
        while temp is not None:
            lenCount+=1
            temp = temp.next
        print(f'There are total ' +str(lenCount)+ ' nodes in the whole LinkedList')
        return lenCount



    def searchElement(self,value):
        temp = self.head
        while temp is not None:
            if temp.data ==value:
                return True
            temp = temp.next
        return False






    def insertNodeFront(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def insertNodeLast(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # newNode.next = None
            self.tail.next = newNode
            self.tail = newNode


    def insertNodeSpecificPosition(self,position,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            pos =1
            tempNode = self.head
            while pos < position-1:
                tempNode = tempNode.next
                pos+=1

            newNode.next = tempNode.next
            tempNode.next = newNode

    def insertNodePos(self,position,data):
        newNode = Node(data)
        tempNode = self.head
        for i in range(position-1):
            tempNode = tempNode.next
        newNode.next = tempNode.next
        tempNode.next = newNode



        #         tempNode.next = newNode    def insertNode(self,data,position):
        # newNode = Node(data)
        # if self.head is None:
        #     self.head = newNode
        #     self.tail = newNode
        # else:
        #     if position == 1:
        #         newNode.next = self.head
        #         self.head = newNode
        #     elif position == 0:
        #         newNode.next = None
        #         self.tail.next = newNode
        #         self.tail = newNode
        #
        #     else:
        #         index = 1
        #         tempNode = self.head
        #         while index < position:
        #             tempNode = tempNode.next
        #             index +=1
        #
        #         newNode.next = tempNod



    # def deleteNode(self,position):
    #     if position ==1:
    #         if self.head ==self.tail:
    #             self.head = None
    #             self.tail = None
    #         else:
    #             self.head = self.head.next
    #     elif position == 0:
    #         if self.head.next == None:
    #             self.tail = None
    #         else:
    #             tempNode = self.head
    #             while tempNode is not None:
    #                 if tempNode.next == self.tail:
    #                     break
    #                 tempNode = tempNode.next
    #             tempNode.next = None
    #             self.tail = tempNode
    #     else:
    #         temp = self.head
    #         index =1
    #         while index< position-1:
    #             temp = temp.next
    #             index+=1
    #         nextNode = temp.next
    #         nextNode1 = nextNode.next
    #         temp.next = nextNode1


    def deleteNodeFront(self):
        if self.head is None:
            print('The linkedlist does not exist')
        else:
            temp = self.head.next
            self.head = None
            self.head = temp
    def deleteNodeLast(self):
        if self.head is None:
            print('The linkedlist does not exist')
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next

            temp.next = None
            self.tail = temp


    def deleteNodeSpecificPosition(self,position):
        if self.head is None:
            print('The linkedlist does not exist')
        else:
            temp= self.head
            pos =1
            while pos< position-1:
                temp = temp.next
                pos+=1

            nextNode = temp.next
            nextNode1 = nextNode.next
            temp.next = None
            temp.next = nextNode1


    def rotateList(self,k):
        if self.head is None:
            print('List can not be rotated, because it is empty')
        elif self.head.next is None:
            print('List can not be rotated, because it has only one element')
        else:
            temp = self.head
            tempNext = self.head.next
            count =0
            while tempNext.next is not None:
                temp = temp.next
                tempNext = tempNext.next
                count+=1
                if count<=k:
                    temp.next = None
                    tempNext.next = self.head
                    self.head = tempNext


    def reverseList(self):
        currentNode = self.head
        currentprev = None
        nextNode = currentNode
        while currentNode is not None:
            nextNode = nextNode.next
            currentNode.next = currentprev
            currentprev = currentNode
            currentNode = nextNode
        self.head = currentprev



































singlst = SinglyLinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
singlst.head = n1
n1.previous = None
n1.next = n2
n2.previous = n1
n2.next = n3
n3.previous= n2
n3.next = n4
n4.previous = n3

singlst.tail = n4


# singlst.printAllElements()
# singlst.insertNodeFront(10)
# singlst.insertNodeLast(100)
# singlst.insertNodeSpecificPosition(4,50)

# print(singlst.searchElement(900))

# singlst.deleteNode(1)
# singlst.deleteNode(1)
# singlst.deleteNode(0)
# singlst.printAllElements()
# singlst.deleteNode(5)
# singlst.deleteNodeFront()
# singlst.deleteNodeLast()
# singlst.printAllElements()
# singlst.deleteNodeSpecificPosition(3)
singlst.printAllElements()
# singlst.rotateList(2)
# singlst.reverseList()
# singlst.insertNodePos(2,100)
singlst.reverseList()
singlst.printAllElements()