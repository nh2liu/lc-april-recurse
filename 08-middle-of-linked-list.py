class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
