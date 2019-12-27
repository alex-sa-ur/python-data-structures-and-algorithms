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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
Solution by:    Alejandro Sanchez Uribe
Date:           7 Dec 2019

Assumption:     The Task 0 prompt required the inclusion of time, and while debating whether or not the date of the call
                is considered "time", I decided to include it as the record would not have any significance of first or
                last without the date
"""

first_record_texts = texts[0]

print('First record of texts, ' + first_record_texts[0] + ' texts ' + first_record_texts[1] + ' at time ' +
      first_record_texts[2])

last_record_calls = calls[-1]

print('Last record of calls, ' + last_record_calls[0] + ' calls ' + last_record_calls[1] + ' at time ' +
      last_record_calls[2] + ', lasting ' + last_record_calls[3] + ' seconds')
