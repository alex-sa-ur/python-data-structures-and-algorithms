"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Solution by:    Alejandro Sanchez Uribe
Date:           7 Dec 2019
"""

numbers_texting = set()
numbers_texted = set()
numbers_calling = set()
numbers_called = set()

potential_telemarketers = set()

for text in texts:
    numbers_texting.add(text[0])
    numbers_texted.add(text[1])

for call in calls:
    numbers_calling.add(call[0])
    numbers_called.add(call[1])

potential_telemarketers = numbers_calling.difference(numbers_texting).difference(numbers_texted).difference(
    numbers_called)

lst = list(potential_telemarketers)
lst.sort()

print('These numbers could be telemarketers: ')

for item in lst:
    print(item)
