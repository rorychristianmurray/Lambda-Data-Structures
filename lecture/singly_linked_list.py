class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # def __str__(self):
    #     self.head = None
    #     self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def print_singly_linked_list(self):
        node = self.head
        while node:
            print(str(node.data))

            node = node.next


list = SinglyLinkedList()
list.insert_node(1)
list.insert_node(2)
list.insert_node(3)
list.insert_node(4)
list.insert_node(5)
list.insert_node(6)
list.insert_node(7)
list.insert_node(8)
list.insert_node(9)
list.insert_node(10)
list.insert_node(11)
list.insert_node(12)
list.insert_node(13)
list.insert_node(14)


list.print_singly_linked_list()
