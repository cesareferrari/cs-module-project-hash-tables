# exec(open("hashtable.py").read())


hash_table = [None] * 8

def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total += b
        total &= 0xffffffff

    return total

def hash_index(key):
    h = my_hash(key)
    return h % len(hash_table)

def put(key, value):
    i = hash_index(key)

    if hash_table[i] != None:
        print(f"Collision. Overwriting {hash_table[i]}")
    hash_table[i] = value

def get(key):
    i = hash_index(key)
    return hash_table[i]

def delete(key):
    i = hash_index(key)
    hash_table[i] = None


put("hello", "world")
put("good morning", "universe")
put("olleh", "space")

print(get("hello"))


