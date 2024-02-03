# Import necessary modules
import csv
import re

# Read data from 'texts.csv' and 'calls.csv' files
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

###################### Part A ######################

# Create a list of calls made by Bangaloreans
blr_calls = [call for call in calls if call[0].startswith('(080)')]

# Create a list of dialed numbers by Bangaloreans
blr_dialed = [call[1] for call in blr_calls]

# Create a set to store unique area codes dialed by Bangaloreans
blr_dialed_areas = set()

# Iterate through dialed numbers to find area codes
for call in blr_dialed:
    if re.search(r'\(\w+\)', call):
        area_code = re.search(r'(\(.*?\))', call).group()
        blr_dialed_areas.add(area_code)
    elif re.search(r'(^[7|8|9])', call):
        area_code = call[:4]
        blr_dialed_areas.add(area_code)

print("The numbers called by people in Bangalore have codes:")

for blr_dialed_area in sorted(list(blr_dialed_areas)):
    print(blr_dialed_area)

###################### Part B ######################

# Create a list of calls made by Bangaloreans to other Bangaloreans
blr_dialed_blr = [call for call in blr_dialed if call.startswith('(080)')]

# Calculate the percentage of calls from fixed lines in Bangalore to other fixed lines in Bangalore
percentage = round((len(blr_dialed_blr) / len(blr_dialed) * 100), 2)

print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percentage))

# Algorithm Complexity:
# Part A:
# - Create the blr_calls list: O(n), where n is the number of calls in the 'calls.csv' file.
# - Create the blr_dialed list: O(n).
# - Create the blr_dialed_areas set: O(1).
# - Iterate through calls to find area codes: O(n).
#   - Find area code for fixed line calls with parentheses: O(m), where m is the length of a phone number.
#   - Find area code for mobile calls: O(m).
# - Sort and print the list of area codes: O(nlogn) for sorting and O(n) for printing.
# => Total complexity of Part A: O(nlogn).

# Part B:
# - Create the blr_dialed_blr list: O(n).
# - Calculate the percentage of calls from fixed lines in Bangalore to other fixed lines in Bangalore: O(1).
# => Total complexity of Part B: O(n).

# The overall complexity of the entire algorithm (Part A + Part B): O(nlogn).