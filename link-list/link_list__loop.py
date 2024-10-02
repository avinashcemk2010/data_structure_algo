class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        n6.next = n3
        self.head = n1

    # floyd cycle detection algorithm
    def detect_loop_ll(self, get_starting_node = False, remove_loop = False):
        fast_ptr = self.head
        slow_ptr = self.head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

            if slow_ptr == fast_ptr:
                if get_starting_node == True:
                    return self.get_starting_node(slow_ptr)

                if remove_loop:
                    return self.removeLoop(slow_ptr)

                return True

        return False

    def removeLoop(self, slo_ptr):
        temp = self.head
        while(slo_ptr.next != temp.next):
            slo_ptr = slo_ptr.next
            temp = temp.next

        slo_ptr.next = None

    def get_starting_node(self, slow_ptr):
        temp = self.head
        while(temp != slow_ptr):
            temp = temp.next
            slow_ptr = slow_ptr.next

        return temp.data


ll = LinkedList()
ll.append() 
print(f'Its a loop? {ll.detect_loop_ll()}')

print(f'Starting node of loop? {ll.detect_loop_ll(get_starting_node=True)}')

ll.detect_loop_ll(remove_loop=True)
print(f'Its a loop? {ll.detect_loop_ll()}')



    