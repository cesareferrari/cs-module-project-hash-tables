# write a function that takes a string
# and returns each letter, aling with how many times
# it occurs in the string

def letter_count(s):
    counts = {}

    for char in s:
        # ensure the char is a letter
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else: 
                counts[char] = 1

    return counts


print(letter_count('Hello'))
print(letter_count('The quick brown forx jumped over the lazy dog'))



def print_sorted_letter_count(s):
    letters = letter_count(s)
    letters_list = list(letters.items())
    letters_list.sort(key=lambda pair: pair[1], reverse=True)

    for pair in letters_list:
        print(f"Letter: {pair[0]}, count {pair[1]}")


print_sorted_letter_count('Hello')
print_sorted_letter_count('The quick brown forx jumped over the lazy dog')

