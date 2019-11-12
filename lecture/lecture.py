"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def add(self, value):
        self.next = ListNode(value)

    def reverse(self):
        cur = self
        new = cur.next
        while new != None:
            prev = cur
            cur = new
            new = cur.next
            cur.next = prev

        return cur


ll1 = ListNode(1)
ll2 = ListNode(2)
ll3 = ListNode(3)
ll4 = ListNode(4)
ll5 = ListNode(5)
ll6 = ListNode(6)
ll7 = ListNode(7)

ll1.next = ll2
ll2.next = ll3
ll3.next = ll4
ll4.next = ll5
ll5.next = ll6
ll6.next = ll7
ll7.next = None


def swapper(linkedList):
    prevValue = linkList.value
    newValue = linkedList.next['value']
    linkedList.next['value'] = prevValue
    linkedList.next['value'].prevValue = newValue
    next()


ln1 = ListNode(1)


print("ln1 : ", ln1)
print("ln1.value : ", ln1.value)
print("ln1.next : ", ln1.next)
