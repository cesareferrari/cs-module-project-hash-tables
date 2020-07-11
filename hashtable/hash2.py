hash_table = [None] * 8

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
    hash_table[index] = value

def get(key):
    index = my_hash(key)
    return hash_table[index]

def delete(key):
    index = my_hash(key)
    hash_table[index] = None


print(hash_table)
put("Hello", "World")
print(hash_table)
print(get("Hello"))
