class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        # start at the head
        # loop through list
        # find value
        # return node
        cur = self.head

        # if cur is None we are at the end,
        # so we loop through a linked list
        # while cur is not None
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next

        return None

    def delete(self, value):
        cur = self.head

        if cur.value == value:
            self.head = cur.next
            return cur

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                return cur
            else:
                prev = cur
                cur = cur.next

        return None


    def insert_at_head(self, node):
        node.next = self.head
        self.head = node


