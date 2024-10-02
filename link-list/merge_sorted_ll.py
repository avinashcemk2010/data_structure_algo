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

    
    # utility method
    @staticmethod
    def merge(ll1, ll2):
        dummy = Node(0)
        tail = dummy

        while ll1 and ll2:
            if ll1.data <= ll2.data:
                tail.next = ll1
                ll1 = ll1.next
            else:
                tail.next = ll2
                ll2 = ll2.next

            tail = tail.next

        if ll1:
            tail.next = ll1
        else:
            tail.next - ll2

        return dummy.next



ll1 = LinkList()
for i in range(1, 10, 2):
    ll1.append(i)

ll1.print_ll()

ll2 = LinkList()
for i in range(2, 10, 2):
    ll2.append(i)

ll2.print_ll()

merge_head = LinkList.merge(ll1.head, ll2.head)
current = merge_head
while current:
    print(current.data, end="-->")
    current = current.next
