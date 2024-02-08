class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        else:
            new_node.next = self.head
            self.head = new_node

    def insertIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0

        if position == index:
            self.insertBegin(data)
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def printLL(self):
        current_node = self.head
        if current_node:
            print(current_node.data, end="")
            current_node = current_node.next

        while(current_node):
            print(", ", end="")
            print(current_node.data, end="")
            current_node = current_node.next
        print()


LList = LinkedList()

LList.insertBegin('A')
LList.insertBegin('B')
LList.insertBegin('C')
LList.insertEnd('Z')

LList.printLL()

print()
LListData = LList.head

while LListData:
    print(LListData.data)
    LListData = LListData.next

