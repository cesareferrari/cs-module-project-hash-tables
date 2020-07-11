def djb2(key):
    pass


hash_table = [None] * 8

def my_hash(s):
    s_utf8 = s.encode()

    total = 0
    for char in s_utf8:
        total += char

    return total % len(hash_table)

# inserts a value into hash table
def put(key, value):
    index = my_hash(key)
    hash_table[index] = value

def get(key):
    index = my_hash(key)
    return hash_table[index]


print(hash_table)
put("Hello", "World")
print(hash_table)
print(get("Hello"))
