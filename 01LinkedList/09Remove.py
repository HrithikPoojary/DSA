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

    def prepop(self):

        if self.head is None:
            return None
        
        temp = self.head 
        self.head = self.head.next
        temp.next = None 

        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

    def getfor(self,index):
        #print(f"index - {index} length - {self.length}")
        if index < 0 or self.length <= index:
            return None        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    def getwhile(self , index):
        if index < 0 or self.length <= index:
            return None 
        index_val = 0
        temp = self.head 
        while index_val < index:
            temp = temp.next 
            index_val += 1
        return temp.value
    
    def set_value(self , index , value):
        if self.length <= index or index < 0:
            return None 
        else :
            temp = self.head 
            for _ in range(index):
                temp = temp.next 
            temp.value = value
            return True
        
    def insert(self , index , value):
        if index < 0 or self.length < index:
            return None 
        elif index == 0:
            node = Node(value)
            node.next = self.head 
            self.head = node 
        elif index == self.length:
            node = Node(value)
            self.tail.next = node 
            self.tail = node
        else:
            temp = self.head 
            for _ in range(index-1):
                temp = temp.next 
            node = Node(value)
            node.next = temp.next
            temp.next = node 

    def remove(self , index):
        if index < 0 or self.length <= index:
            return None
        elif index ==0 :
            temp = self.head 
            self.head = self.head.next
            temp.next = None 
        elif index== self.length-1:
            temp = self.head 
            for _ in range(index-1):
                prev = temp.next
                temp = self.tail # for return
            self.tail = prev 
            self.tail.next = None
        else:
            def get(index):
                if index < 0 or self.length <= index:
                    return None 
                else:
                    temp = self.head 
                    for _ in range(index):
                        temp = temp.next 
                    return temp
            prev = get(index-1)
            temp = prev.next
            prev.next = temp.next 
            temp.next = None 
            self.length -= 1
        self.length -= 1
        return temp 
            
        
l = LinkedList(4)
l.append(2)
l.append(3)
a = l.remove(0)
print("Remove",a.value)
l.print_node()
