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
# Extract information from the "texts.csv" file
first_text = texts[0]
# Get information from the first record
incoming_text_number, answering_text_number, time_text = first_text

# Extract information from the "calls.csv" file
last_call = calls[-1]
# Get information from the last record
incoming_call_number, answering_call_number, time_call, duration = last_call

# Print the results
print("First record of texts, {} texts {} at time {}".format(incoming_text_number, answering_text_number, time_text))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming_call_number, answering_call_number, time_call, duration))
