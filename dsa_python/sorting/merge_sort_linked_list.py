class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def merge(first_half: ListNode, second_half: ListNode):
    dummy, temp1, temp2 = ListNode(), first_half, second_half
    merge = dummy
    
    while temp1 and temp2:
        if temp1.val < temp2.val:
            merge.next = ListNode(temp1.val)
            temp1 = temp1.next
        else:
            merge.next = ListNode(temp2.val)
            temp2 = temp2.next
            
        merge = merge.next
        
    while temp1:
        merge.next = ListNode(temp1.val)
        temp1, merge = temp1.next, merge.next
        
    while temp2:
        merge.next = ListNode(temp2.val)
        temp2, merge = temp2.next, merge.next
    
    return dummy.next
            
def merge_sort(head: ListNode):
    if not head or not head.next:
        return head
        
    # Getting the second half of the list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    second_start = slow.next
    slow.next = None
    
    # Recursively calling merge sort on the head (now first half) and second half of the list
    first, second = merge_sort(head), merge_sort(second_start)
    return merge(first, second)

def print_list(head: ListNode) -> None:
    temp = head
    print('[', end='')
    while temp.next:
        print(temp.val, end=', ')
        temp = temp.next  
    print(temp.val, end=']')
    print()
        
if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    head = merge_sort(head)
    print_list(head)

    
    