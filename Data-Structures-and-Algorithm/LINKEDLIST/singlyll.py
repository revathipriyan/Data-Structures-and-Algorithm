"""
Design Singly Linked List --> Insert at beginning, end and middle, sorting, delete and search, reverse
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        """Add to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def prepend(self,data):
        """Add at the start of the list"""
        node = Node(data)
        node.next = self.head
        self.head = node

    def delete(self, data):
        """Delete the first occurrence of that data"""
        if not self.head:
            return 
        
        curr = self.head
        prev = None
        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                    return
                else:
                    self.head.next = curr.next
                return 
            prev = curr
            curr = curr.next


    def search(self, val):
        """Search for the data or return -1"""
        curr = self.head
        while curr:
            if curr.data == val:
                return True
            curr = curr.next
        return False


    def print_list(self):
        """Prints the entire list"""
        curr = self.head
        while curr:
            print(curr.data, end = "->")
            curr = curr.next
        print("None")

    def reverse(self):
        """Reverse the ll"""
        curr = self.head
        prev = None
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt

        self.head = prev

    
    def create_ll(self, data):
        for i in data:
            self.append(i)


if __name__ == "__main__":
    arr = [1,2,3,5,6,7,8]
    ll = LinkedList()
    ll.create_ll(arr)
    ll.reverse()
    ll.print_list()



    


    