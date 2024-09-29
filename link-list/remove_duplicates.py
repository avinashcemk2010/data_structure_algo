class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next

        print()

    
    def remove_duplicate(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

        self.print_ll()


ll = LinkedList()
# Insert element in link list
ls = [1,1,3,4,4,4,5,6,7,7,7]
for ele in ls:
    ll.append(ele)

ll.remove_duplicate()
