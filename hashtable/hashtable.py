class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}: {self.value}>"

class HashTableList:
    def __init__(self):
        self.head = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=8):
        # Your code here
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity

        self.storage = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    # my simple hashing function for initial testing
    # don't use in production
    def my_hash(self, key):
        key_utf8 = key.encode()

        total = 0

        for char in key_utf8:
            total += char

        return total


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # implemented other hashing function


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381

        for char in key:
            hash = ( (hash << 5) + hash ) + ord(char)

        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.my_hash(key) % self.capacity
        # return self.fnv1(key) % self.capacity

        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # implementation with only the value
        # self.storage[self.hash_index(key)] = value

        entry = HashTableEntry(key, value)
        index = self.hash_index(key)
        head = self.storage[index]

        if head is None:
            self.storage[index] = entry
        else:
            current = head

            while current.next is not None:
                # overwrite value if key is present
                if current.key == key:
                    current.value = value
                    return None
                else:
                    current = current.next

            # add entry to tail
            current.next = entry


        """
        entry = HashTableEntry(key, value)
        i = self.hash_index(key)

        # when slot is empty, just add the entry and return
        if self.storage[i] is None:
            self.storage[i] = entry
            return entry

        # if slot is not empty, traverse the linked list until you find 
        # the next is none (list tail)
        while self.storage[i].next is not None:
            # if the element key is same as entry key
            # overwrite the value and return
            if self.storage[i].key == key:
                self.storage[i].value = value
                return entry
            else:
                # We have reached the end of the list, add the entry and return
                self.storage[i].next = entry
                return entry
        """
 


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.storage[self.hash_index(key)] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # return self.storage[self.hash_index(key)]

        index = self.hash_index(key)
        current = self.storage[index]

        while current is not None:
            if current.key == key:
                return current

            current = current.next

        return None




    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
