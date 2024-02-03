# Import necessary modules
import csv

# Read data from 'texts.csv' and 'calls.csv' files
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts, or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be printed out one per line in lexicographic order
with no duplicates.
"""

# Create sets for outgoing and incoming calls
outgoing_calls = set([call[0] for call in calls])
incoming_calls = set([call[1] for call in calls])

# Create sets for outgoing and incoming texts
outgoing_texts = set([text[0] for text in texts])
incoming_texts = set([text[1] for text in texts])

possible_telemarketers = []

# Identify possible telemarketers
for phone in outgoing_calls:
    if (phone not in outgoing_texts) and (phone not in incoming_texts) and (phone not in incoming_calls):
        possible_telemarketers.append(phone)

# Print the possible telemarketers in lexicographic order
print('These numbers could be telemarketers:')
for possible_telemarketer in sorted(possible_telemarketers):
    print(possible_telemarketer)
    
# Algorithm Complexity:
# - Create sets for outgoing_calls and incoming_calls: O(n) with n being the number of call records.
# - Create sets for outgoing_texts and incoming_texts: O(n) with n being the number of text records.
# - Create an empty list possible_telemarketers: O(1).
# - Iterate through the outgoing_calls: O(n).
#   - Inside the loop, check if the phone number meets the telemarketer criteria: O(1).
#   - If the criteria are met, add the phone number to the possible_telemarketers list: O(1).
# - Sort the possible_telemarketers list: O(nlogn).
# - Print the list of possible telemarketers: O(n).
# => Total complexity of the algorithm: O(nlogn).

# The overall complexity is primarily determined by the sorting of the list of possible telemarketers.