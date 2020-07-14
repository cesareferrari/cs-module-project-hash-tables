"""
Strategies for Handling Collisions

Open addressing or Linear probing: when it searches for the next empty slot to
put the value.

Quadrating probing: find empty spot after 2 or 4 next ones.

Double hashing: hash the hash (so it gives a different hash)

Disallow: no putting if already there

Chaining: array of linked lists



Index  Chain (linked list)
----   ---------------
0      ("qux", 54)  -> None
1      ("foo", 29)  -> None
2      ("bar", 99)  -> None
3      LL[self.head = Node(self.key = "fox", self.value = 101) -> Node("tree", 209) -> None]
4      -> None

put("foo", 42)   # hashed to index 1
put("foo", 29)   
put("bar", 99)   # hashes to index 2
put("baz", 38)   # hashes to index 1! collision!
put("qux", 54)   # hashes to 0
put("fox", 101)  # hashes 3
put("tree", 209) # hashes 3

get("qux")
get("foo")
get("fred")  # hashes to 0 --> return None


delete("baz")

"""

hash_table = [None] * 8

class HashTableItem:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next



def djb2(key):
    hash = 5381

    for char in key:
        hash = ( (hash << 5) + hash ) + ord(char)

    return hash


def hash_index(key):
    return djb2(key) % len(hash_table)


def my_hash(s):
    s_utf8 = s.encode()

    total = 0
    for char in s_utf8:
        total += char

    return total % len(hash_table)

def put(key, value):
    index = my_hash(key)
    # hash_table[index] = value
    hash_table[index] = HashTableItem(key, value)

def get(key):
    index = my_hash(key)
    return hash_table[index].value

def delete(key):
    index = my_hash(key)
    hash_table[index] = None


print(hash_table)
put("Hello", "World")
print(hash_table)
print(get("Hello"))



class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current

        current = current.next

        return None


    def insert_at_tail(self, value):
        node = ListNode(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = node

    def delete(self, value):
        current = self.head

        # nothing to delete
        if current is None:
            return None

        if current.value == value:
            # deleting the head
            self.head = current.next
            return current
        else:
            previous = current
            current = current.next

            while current is not None:
                if current.value == value:
                    previous.next = current.next
                    return current
                else:
                    previous = current
                    current = current.next

            return None

