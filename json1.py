book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 989459845
}

book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 9894592342
}


import json
s = json.dumps(book)
with open ("c://data/book.txt","w") as f:
    f.write(s)

# using Json data into dictionary

import json
book =json.loads(s)
print(book)
print(type(book))

print(book['bob'])
print(book['bob']['phone'])

# using for loop in json data

for person in book:
    print(book[person])