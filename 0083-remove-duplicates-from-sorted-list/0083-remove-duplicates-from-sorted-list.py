class Solution:
    def deleteDuplicates(self, head):
        current = head

        # Traverse the linked list
        while current is not None and current.next is not None:

            # If duplicate node found
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head