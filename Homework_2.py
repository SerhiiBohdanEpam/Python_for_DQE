
# The first task: create a list of random number of dicts (from 2 to 10)
# add library 'random'
import random
# add library 'string'
import string

# Create a list of random number of dicts
dicts = [{} for _ in range(random.randint(2, 10))]
# For each dict in the list
for d in dicts:
    # Assign a random number of keys
    for _ in range(random.randint(1, 10)):
        # The key is a random letter, the value is a random number
        d[random.choice(string.ascii_lowercase)] = random.randint(0, 100)

print(dicts)
# The second task:

# Initialize an empty dictionary to hold the final result
final_dict = {}

# Enumerate over the list of dictionaries (enumarate gives us index and value)
# Index is here if we need to suffix it to the keys with max value
for i, d in enumerate(dicts):
    # For each key, value pair in the current dictionary
    for k, v in d.items():
        # If the key is already in our final dict and the current value is higher
        if k in final_dict and v > final_dict[k]:
            # We remove the old key
            final_dict.pop(k)
            # And add the key with _dict_number as suffix and the new max value
            final_dict[k + f'_{i+1}'] = v
        # If the key isn't in the final dict yet, we just add the key-value pair
        elif k not in final_dict:
            final_dict[k] = v
# Print the dictionary
print(final_dict)

