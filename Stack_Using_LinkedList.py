class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None



class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def printElements(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next



    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.isEmpty():
            return "There is no any element in the stack"
        popValue = self.head.data
        self.head = self.head.next
        return popValue

    def peek(self):
        if self.isEmpty():
            return "There is no any element in the stack"
        return self.head.data


    def deleteStack(self):
        self.head = None







#
