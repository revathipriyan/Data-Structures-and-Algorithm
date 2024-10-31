# Inserting a node before a given node
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

def insert_before_key(head,key,newData):

    if head is None:
        return head
    
    prev = None
    curr = head

    if head.data == key:
        new_node = Node(newData)
        new_node.next = head
        return new_node

    while curr is not None and curr.data!=key:
        prev = curr
        curr = curr.next

    if curr is not None:
        new_node = Node(newData)
        prev.next = new_node
        new_node.next = curr

    return head

def print_list(node):
    curr = node
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list: 
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    newData = 6
    key = 1

    head = insert_before_key(head, key, newData)

    print_list(head)

        
        

            