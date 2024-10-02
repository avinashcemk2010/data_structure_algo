class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = None 

        if self.head:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = new_node
        else:
            self.head = new_node

    def print_ll(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next

        print()

    @staticmethod
    def add(ll1, ll2):

        dummy = Node(0)
        tail = dummy
        carry = 0
        sum = 0
        while ll1 or ll2:
            if ll1 and ll1.data:
                x = ll1.data  
            else:
                x = 0
            if ll2 and ll2.data:
                y = ll2.data
            else:
                y = 0
            sum = x + y + carry
            carry = int(sum / 10)
            data_to_add = int(sum % 10)
            tail.next = Node(data_to_add) 
            tail = tail.next
            if ll1: ll1 = ll1.next
            if ll2: ll2 = ll2.next

        if carry:
            tail.next = Node(carry)
            
        return dummy.next


ll1 = LinkList()
for i in range(1, 10, 2):
    ll1.append(i)

ll1.print_ll()

ll2 = LinkList()
for i in range(2, 10, 2):
    ll2.append(i)

ll2.print_ll()

add_head = LinkList.add(ll1.head, ll2.head)
current = add_head
while current:
    print(current.data, end="-->")
    current = current.next