def my_hash(s):
    # encode the string
    sb = s.encode()

    total = 0

    for b in sb:
        total += b

    return total % 8

def get_value(key):
    # hash "Hello"
    current_hash = my_hash(key)
    # retrieve value at the hash
    return hash_table[current_hash]

hash_table = [None] * 8

hello_hash = my_hash("Hello")
hash_table[hello_hash] = "World!"

print(hello_hash)
print(hash_table)

print(get_value("Hello"))

