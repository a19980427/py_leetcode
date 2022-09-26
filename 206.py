# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # val_list = []
        # cur = head
        # while cur:
        #     val_list.append(cur.val)
        #     cur = cur.next
        #
        # cur = head
        # index = len(val_list) - 1
        #
        # while cur:
        #     cur.val = val_list[index]
        #     index -= 1
        #     cur = cur.next
        #
        # return head
        v1 = []
        while head:
            v1.append(head.val)
            head = head.next

        tmpNode = ListNode(v1[len(v1) - 1])
        rHead = tmpNode

        for i in range(len(v1) - 2, -1, -1):
            tmpNode.next = ListNode(v1[i])
            tmpNode = tmpNode.next
        print(rHead)
        return rHead
