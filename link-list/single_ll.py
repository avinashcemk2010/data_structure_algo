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

    def len(self):
        current_node = self.head
        count = 0

        if self.head:
            while current_node:
                count += 1
                current_node = current_node.next

            return count
        else:
            return 0

    def insert_at_pos(self, data, pos):
        len_of_ll = self.len()
        if pos > len_of_ll + 1:
            return 'please provide valid position to insert'

        if pos == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            count = 1
            while count < pos-1:
                current_node = current_node.next
                count += 1

            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node 
        

    def delete(self, pos):
        current_node = self.head
        count = 1

        if pos == 1:
            self.head = self.head.next
        else:
            while current_node:
                if count == pos-1:
                    current_node.next = current_node.next.next

                current_node = current_node.next
                count += 1

        self.print_ll()

    def search_element(self, ele):
        current_node = self.head
        pos = 1
        while current_node:
            if current_node.data == ele:
                return pos

            pos += 1
            current_node = current_node.next

    
    def reverse(self):
        pass 

            


ll= LinkedList()

# Insert element in link list
ls = [1,2,3,4,5,6,7,8,9,10]
for ele in ls:
    ll.append(ele)

ll.print_ll()

# len of link list
print(f'length of link list:{ll.len()}')

# insert 29 at pos 4
ll.insert_at_pos(29, 4)
print(f'after insertin 29 at 4th pos')
ll.print_ll()
ll.insert_at_pos(299, 12)
print(f'after insertin 299 at 12th pos')
ll.print_ll()
ll.insert_at_pos(299, 115)
print(f'after insertin 299 at 115th pos')
ll.print_ll()
ll.insert_at_pos(0, 1)
print(f'after insertin 0 at 1st pos')
ll.print_ll()

# delete an element at i th position
ll.delete(4)

# search an element in link list
ele = 5
pos = ll.search_element(ele)
print(f'{ele} is present at {pos} location')

ele = 299
pos = ll.search_element(ele)
print(f'{ele} is present at {pos} location')

# reverse the link list
ll.reverse()







    