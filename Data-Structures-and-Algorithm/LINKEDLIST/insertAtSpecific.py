# Python Program to Insert a Node At a Specific
# Position in Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_position(head, position, data):
    new_node = Node(data)

    if position == 1:
        new_node.next = head
        head = new_node
        return head
    
    curr = head
    prev = None
    for _ in range(1, position) :
        prev = curr
        curr = curr.next
        
    
    prev.next = new_node
    new_node.next = curr


    return head

def print_list(head):
    while head:
        print(f" {head.data}", end="")
        head = head.next
    print()

# Creating the list 3->5->8->10
head = Node(3)
head.next = Node(5)
head.next.next = Node(8)
head.next.next.next = Node(10)

data, pos = 12, 3
head = insert_at_position(head, pos, data)
print_list(head)
