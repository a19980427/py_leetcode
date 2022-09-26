# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.length = len(head)
        list_head = ListNode()
        dicts = {}
        cur = list_head

        for val in head:
            node = ListNode()
            node.val = val
            node.next = None

            cur.next = node
            cur = node

        cur = list_head.next
        while cur:
            dicts[cur] = cur.val
            cur = cur.next

    def getRandom(self) -> int:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
