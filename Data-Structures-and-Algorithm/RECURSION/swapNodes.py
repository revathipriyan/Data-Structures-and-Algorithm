class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Base case: If there are fewer than two nodes, no swap is needed
        if not head or not head.next:
            return head
        
        # Identify the two nodes to swap
        first_node = head
        second_node = head.next
        
        # Swap: Recurse for the rest of the list starting from the third node
        first_node.next = self.swapPairs(second_node.next)
        
        # Complete the swap by pointing the second node to the first node
        second_node.next = first_node
        
        # The second node is now the new head of the list
        return second_node

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(" -> ".join(map(str, result)))

# Example usage
if __name__ == "__main__":
    # Create a linked list from values
    values = [1, 2, 3, 4]
    head = create_linked_list(values)
    
    print("Original Linked List:")
    print_linked_list(head)
    
    # Swap nodes in pairs
    solution = Solution()
    new_head = solution.swapPairs(head)
    
    print("\nSwapped Linked List:")
    print_linked_list(new_head)
