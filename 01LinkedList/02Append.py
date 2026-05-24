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

l = LinkedList(4)
l.append(2)
l.append(3)
l.print_node()
