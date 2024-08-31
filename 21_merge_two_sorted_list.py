import unittest

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None

        if not list1:
            return list2

        if not list2:
            return list1

        head = None
        lastAttachedNode = None
        list1ToBeProcessed = list1
        list2ToBeProcessed = list2

        while list1ToBeProcessed or list2ToBeProcessed:
            nextNode = None
            if not list2ToBeProcessed or (list1ToBeProcessed and list1ToBeProcessed.val < list2ToBeProcessed.val):
                nextNode = list1ToBeProcessed
                list1ToBeProcessed = list1ToBeProcessed.next
            else:
                nextNode = list2ToBeProcessed
                list2ToBeProcessed = list2ToBeProcessed.next
            if not head:
                head = nextNode
            else:
                lastAttachedNode.next = nextNode
            lastAttachedNode = nextNode
        return head


class SolutionTestCase(unittest.TestCase):
    def getHeadNode(self, list):
        if not list:
            return None

        head = None
        for el in reversed(list):
            head = ListNode(el, head)
        return head

    def getNodesAsList(self, headNode):
        if not headNode:
            return []

        resultList = [headNode.val]
        nextElem = headNode.next
        while nextElem != None:
            resultList.append(nextElem.val)
            nextElem = nextElem.next
        return resultList

    def test_solution(self):
        list1 = self.getHeadNode([1, 2, 4])
        list2 = self.getHeadNode([1, 3, 4])
        result = Solution().mergeTwoLists(list1, list2)

        self.assertEqual(self.getNodesAsList(result), [1, 1, 2, 3, 4, 4])

    def test_solution_2(self):
        list1 = self.getHeadNode([])
        list2 = self.getHeadNode([1])
        result = Solution().mergeTwoLists(list1, list2)

        self.assertEqual(self.getNodesAsList(result), [1])

    def test_solution_3(self):
        list1 = self.getHeadNode([-9, 3])
        list2 = self.getHeadNode([5, 7])
        result = Solution().mergeTwoLists(list1, list2)

        self.assertEqual(self.getNodesAsList(result), [-9, 3, 5, 7])


unittest.main()
