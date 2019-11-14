# from doubly_linked_list import DoublyLinkedList
# from doubly_linked_list import ListNode

from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


# dll = DoublyLinkedList()
# print("dll : ", dll)
# dll.add_to_tail(12)
# print("dll : ", dll.tail.value)


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.storage = {}
        self.count = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if key exists
        # print("self.storage : ", self.storage)
        # print("\n\n\n")
        # print("self.storage[key].value : ", self.storage[key].value)
        # print("\n\n\n")
        if key in self.storage:
            # move the key to the tail of the dll (mra)
            currNode = self.storage[key]
            print("currNode : ", currNode)
            self.dll.move_to_end(currNode)
            # retrieve associated value from storage
            return currNode.value[1]
        else:  # if key does not exist
            print(f"No such key : {key} exists")
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        # When receiving an input, we check first if the input exists already in our LRU
        # print("self.storage[key] : ", self.storage[key])
        if key in self.storage:
            # If the input exists, we update the value in the
            # storageionary with the new given value
            # self.storage.update(key=value)
            currNode = self.storage[key]
            currNode.value = (key, value)
            # then move the input to the tail
            # (most recently accessed) of the linked list
            self.dll.move_to_end(currNode)
            return
         # if the input does not exist in our LRU
         # check if LRU is full

        elif self.count < self.limit:
            # if not full, add to storage
            # then add to tail (most recently accessed) in the linked list
            self.dll.add_to_tail((key, value))
            self.storage[key] = self.dll.tail
            # increment count by 1
            self.count += 1
            print("self.dll.head.value[0]", self.dll.head.value[0])
        elif self.count >= self.limit:  # if LRU is full
            print("count : ", self.count)
            print("limit : ", self.limit)
            print("\n\n\n")
            # print("self.storage elif : ", self.storage)
            print("self.dll.head : ", self.dll.head)
            print("self.dll.head.value[0] : ", self.dll.head.value[0])
            print("\n\n\n")
            # delete previous head of linked list (key, val) from thestorage
            del self.storage[self.dll.head.value[0]]
            self.dll.remove_from_head()
            # add new input (key) to the storage
            self.storage[key] = (key, value)
            self.dll.add_to_tail((key, value))
            self.storage[key] = self.dll.tail
            # delete head of linked list
            # add input to tail of linked list (most recently accessed)


testLRU = LRUCache()
testLRU.set("orange", "you glad")
# testLRU.set("banana", "I didn't say")
# testLRU.set("ten", "its ten")
# print("count : ", testLRU.count)
print("get : ", testLRU.get('orange'))


# print("testLRU.dll.head.value : ", testLRU.dll.head.value.value)
# print("testLRU.dll.head.value : ", testLRU.dll.tail.value)
# # print()
