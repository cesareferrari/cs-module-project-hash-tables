d = {
    "foo": 1,
    "bar": 99,
    "qux": 42
    }

for pair in d.items():
    print(pair)

dict_list = list(d.items())


dict_list.sort() # sort in place by the first item in the tuple returned
sorted(dict_list) # not mutate in place


"""
# Python Lambda functions (anonymous functions)

some_numbers = [99, 7, 4, 1, 100, 10, 5]
map(lambda x: x + 1, some_numbers)
list(map(lambda x: x + 1, some_numbers))
"""

# sort based on second thing (value)
dict_list.sort(key=lambda pair: pair[1]) 
dict_list.sort(key=lambda pair: pair[1], reverse=True)  # reverse
