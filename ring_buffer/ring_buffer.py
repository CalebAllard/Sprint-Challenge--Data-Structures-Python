from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        

    def append(self, item):
        if self.storage.length == self.capacity:
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head               
            
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        node = self.storage.head
        for i in range(0, self.storage.length):
            list_buffer_contents.append(node.value)
            if node.next != None:
                node = node.next
            
               
        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
