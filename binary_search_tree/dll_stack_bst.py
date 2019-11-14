from dll_bst import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # we will be adding and subtracting based on LIFO
        self.storage = DoublyLinkedList()

    def push(self, value):
        # add to the top of the stack, aka the tail
        # increment size by 1
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        # check if size > 0
        # if true:
            # remove from the top of the stack, aka the tail
            # decrement size by 1
        # else return None
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
