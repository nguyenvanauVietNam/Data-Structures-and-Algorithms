# Read file into texts and calls.
# It's ok if you don't understand how to read files.
import csv

# Open and read the 'texts.csv' file
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Open and read the 'calls.csv' file
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# TASK 1:
# How many different telephone numbers are there in the records? 
# Print a message:
# "There are <count> different telephone numbers in the records."

# Create an empty set to store all unique telephone numbers
unique_numbers = set()

# Iterate through the 'texts' list to extract phone numbers from columns 0 and 1
# O(n)
for text in texts:
    unique_numbers.add(text[0])
    unique_numbers.add(text[1])

# Iterate through the 'calls' list to extract phone numbers from columns 0 and 1
# O(n)
for call in calls:
    unique_numbers.add(call[0])
    unique_numbers.add(call[1])

# Use the len function to count the number of unique phone numbers
count = len(unique_numbers)

# Print the message with the count
print("There are", count, "different telephone numbers in the records.")