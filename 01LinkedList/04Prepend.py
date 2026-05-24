class Node:

    def __init__(self,value):
        self.value = value 
        self.next = None

    
class LinkedList:

    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1

    def print_node(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def append(self,value):
        append_node = Node(value)
        if self.head is None:
            self.head = append_node
            self.tail = append_node
        else:
            self.tail.next = append_node
            self.tail = append_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None 

        temp = self.head
        pre = self.head 

        while temp.next is not None:
            pre = temp 
            temp = temp.next

        self.tail = pre 
        self.tail.next = None

        self.length -= 1
        if self.length == 0:
            self.head = None 
            self.tail = None

    def prepend(self, value):
        prepend_node = Node(value)
        if self.head is None:
            self.head = prepend_node
            self.tail = prepend_node
        else:
            prepend_node.next = self.head
            self.head = prepend_node
        self.length += 1


l = LinkedList(4)
l.append(2)
l.append(3)
l.pop()
l.prepend(10)
l.print_node()
