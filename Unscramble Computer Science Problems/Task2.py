"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the
phone during September 2016.".
"""

# Dictionary to keep track of all calls
phone_time = {}  # O (1)

# Iterate through calls to calculate total time
for call in calls:  #O(n)
    incoming_call_number, answering_call_number, time_call, duration = call#O(1)
    time_parts = time_call.split(' ')#O(1)
    month, year = time_parts[0].split('/')  #O(1)
    
    if month == '09' and year == '2016':
        duration = int(duration)#O(1)
        
        # Update the total time for incoming call number
        if incoming_call_number in phone_time:
            phone_time[incoming_call_number] += duration#O(1)
        else:
            phone_time[incoming_call_number] = duration#O(1)

        # Update the total time for answering call number
        if answering_call_number in phone_time:
            phone_time[answering_call_number] += duration#O(1)
        else:
            phone_time[answering_call_number] = duration#O(1)

# Find the telephone number with the longest total time
max_time_number = max(phone_time, key=phone_time.get)#O(1)
total_time = phone_time[max_time_number]#O(1)

# Print the result
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_time_number, total_time))#O(1)
#Final O(n)