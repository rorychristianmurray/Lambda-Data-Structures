from dll_bst import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # it has directional pointers so we know
        # where something is in the 'queue'
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # take the dll
        # run add to tail and pass it value
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        # check if size > 0
        # if yes, dequeue
            # take the dll
            # run add remove from tail
            # decrement size by 1
        # if not, return None
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        # return size of queue
        return self.size
