my_arr = ["hello", "world", "how", "are", "you"]
my_arr[4]

# takes a string
# returns a number

my_alphabet = {'a': 0, 'b': 1}

def my_hash(s):
    total = 0
    for char in s:
        total += my_alphabet[char]

    return total

# ASCII assigns numbers to letters

ord('a')  # 97
ord('b')  # 98


'a'.encode()


def my_hash(s):
    s_utf8 = s.encode()

    total = 0

    for c in s_utf8:
        total += c

    return total

hello_index = my_hash("hello")

my_arr = [None] * 5

hello_index = hello_index % len(my_arr)

my_arr[hello_index] = "hello"
