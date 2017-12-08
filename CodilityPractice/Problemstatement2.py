class IntList:
    def __init__(self, initvalue):
        self.value = initvalue
        self.next = None


class Solution:
    def solution(self,intList):
        count = 0
        while intList is not None:
            count += 1
            intList = intList.next
        return count

class main:
    head = None
    intList = IntList(1)
    intList.next = head
    head = intList

    intList1 = IntList(2)
    intList1.next = head
    head = intList1

    intList2 = IntList(3)
    intList2.next = head
    head = intList2

    solution = Solution()
    print solution.solution(head)