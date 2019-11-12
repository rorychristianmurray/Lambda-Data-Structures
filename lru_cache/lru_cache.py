from doubly_linked_list import DoublyLinkedList

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
        self.dict = {}
        self.count = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if accessed, move value to the tail
        pass

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
        if key in self.dict:
            # If the input exists, we update the value in the
            # dictionary with the new given value
            # self.dict.update(key=value)
            self.dict[key] = value
            # then move the input to the tail
            # (most recently accessed) of the linked list
            self.dll.move_to_end(key)
        else:  # if the input does not exist in our LRU
            # check if LRU is full
            if self.count < self.limit:
                # if not full, add to dictionary
                self.dict[key] = value
                # then add to tail (most recently accessed) in the linked list
                self.dll.add_to_tail(key)
                # increment count by 1
                self.count += 1
            else:  # if LRU is full
                # delete head of linked list
                removeKey = self.dll.remove_from_head()
                # add input to tail of linked list (most recently accessed)
                self.dll.add_to_tail(key)
                # delete previous head of linked list (key) from the dictionary
                del self.dict[removeKey]
                # add new input (key) to the dictionary
                self.dict[key] = value

        return self


testLRU = LRUCache()
testLRU.set("orange", "you glad")
testLRU.set("banana", "I didn't say")
print(testLRU.count)
