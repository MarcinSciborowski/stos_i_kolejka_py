class Node:
    def __init__(self, dane=None, next_node=None):
        self.dane = dane
        self.next_node  = next_node

    def __str__(self):
        return str(self.dane)

class Fifo_dowiazane:
    def __init__(self):
        self.dl = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.dl == 0

    def enqueue(self, el):
        old_tail=self.tail
        self.tail = Node(el)
        if self.is_empty() :
            self.head = self.tail
        else:
            old_tail.next_node = self.tail
        self.dl += 1

    def dequeue(self):
        if self.is_empty() == True:
            return False
        self.head = self.head.next_node
        self.dl -= 1

    def first(self):
        if self.is_empty():
            return False
        return self.head.dane


