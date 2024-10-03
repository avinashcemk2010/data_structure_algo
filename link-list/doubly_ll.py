class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.previous = None
        self.data = data

class DoublyLinkList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        new_node.next = None
        new_node.previous = None 
        if self.tail:
            self.tail.next = new_node
            new_node.previous = self.tail
        else:
            self.head = new_node
            
        self.tail = new_node
        self.length += 1

    def print_forward_ll(self):
        if self.head == None or self.tail == None:
            return

        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        
        print()

    def print_backward_ll(self):
        if self.head == None or self.tail == None:
            return

        last = self.tail
        while last:
            print(last.data, end="-->")
            last = last.previous
        
        print()

    
    def get_length(self):
        print(self.length)

    
    def add_at_first(self, data):
        new_node = Node(data)
        if self.get_length() == 0:
            self.tail = new_node
        else:
            self.head.previous = new_node

        new_node.next = self.head
        self.head = new_node


    def delete_first_element(self):
        if self.get_length() == 0:
            return

        temp = self.head
        if self.head == self.tail:
            self.tail = None
        else:
            self.head.next.previous = None

        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp 

    
    def delete_last_element(self):
        temp = self.tail
        if self.head == self.tail:
            self.head = None
        else:
            self.tail.previous.next = None

        self.tail = self.tail.previous 
        temp.previous = None

        return temp 





dll = DoublyLinkList()
for i in range(10):
    dll.append(i)

dll.print_forward_ll()
dll.print_backward_ll()
dll.get_length()

dll.add_at_first(45)
dll.print_forward_ll()

dll.delete_first_element()
dll.delete_first_element()
dll.print_forward_ll()

    


            


    