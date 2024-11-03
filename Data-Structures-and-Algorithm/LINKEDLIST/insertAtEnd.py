# Python Program to Insert a Node at the End of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function appends a new node at the end and returns the head.
def insertAtEnd(head, new_data):

    # Create a new node
    new_node = Node(new_data)

    # If the Linked List is empty, make the
    # new node as the head and return
    if head is None:
        return new_node

    # Store the head reference in a temporary variable
    last = head

    # Traverse till the last node
    while last.next:
        last = last.next

    # Change the next pointer of the last
    # node to point to the new node
    last.next = new_node

    # Return the head of the list
    return head


def print_list(node):

    while node:
        print(node.data, end=" ")
        node = node.next


if __name__ == "__main__":

    # Create a linked list:
    # 2 -> 3 -> 4 -> 5 -> 6
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(6)

    head = insertAtEnd(head, 1)

    print_list(head)
