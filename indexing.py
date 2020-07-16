# given a list of records, 
# be able to quickly report everyone
# in a particular category

records = [
    ("Corey", "iOS"),
    ("Tyler", "DS"),
    ("Anika", "DS"),
    ("Jenna", "web"),
    ("Nico", "web"),
    ("Carl", "web"),
    ("Michael", "iOS")
]

# iOS_folks = []
# for record in records:
#     if record[1] == 'iOS':
#         iOS_folks.append(record[0])

def build_index(records):
    index = {}

    # loop over records
    for record in records:
        name, track = record  # tuple unpacking

        ## key is track
        ### if key isn't in dictionary, add it
        if track not in index:
            index[track] = []

        ## value: list of names
        index[track].append(name)

    return index

index = build_index(records)

for track in index:
    print(track)

print(index["web"])
print(index["iOS"])
