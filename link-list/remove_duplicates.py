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

    def add_in_sorted_ll(self, data):
        current = self.head
        previous = None
        node = Node(data)

        if current.data > data:
            self.head = node
            node.next = current
        else:
            while current and current.data < data:
                previous = current
                current = current.next

            previous.next = node
            node.next = current

        self.print_ll()

    def delete(self, key):
        current = self.head
        previous = None

        if current.data == key:
            self.head = current.next
        else:
            while current and current.data != key:
                previous = current
                current = current.next

            if current:
                previous.next = current.next

        ll.print_ll()


ll = LinkedList()
# Insert element in link list
ls = [3,4,4,4,5,6,7,7,7,15]
for ele in ls:
    ll.append(ele)

ll.remove_duplicate()

#add element in sorted link list
ll.add_in_sorted_ll(5)
ll.add_in_sorted_ll(12)
ll.add_in_sorted_ll(1)

#delete
ll.delete(5)
ll.delete(1)


