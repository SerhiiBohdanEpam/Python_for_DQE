# Refactor homework from module 2
# 1 create a list of random number of dicts (from a to b)
# add library 'random'
import random
# add library 'string'
import string
# import libraly for RegEx
import re


# define the function with 6 attributes
def generate_dicts(min_dicts=2, max_dicts=10, min_keys=1, max_keys=10, min_value=0, max_value=100):
    """
    Generates a list of dictionaries. Each dictionary will have a random number of entries,
    with keys being letters and values being numbers within the specified range.

    Args:
    min_dicts (int): Minimum number of dictionaries in the list.
    max_dicts (int): Maximum number of dictionaries in the list.
    min_keys (int): Minimum number of keys in each dictionary.
    max_keys (int): Maximum number of keys in each dictionary.
    min_value (int): Minimum value for dictionary values.
    max_value (int): Maximum value for dictionary values.

    Returns:
    List[Dict]: The list of dictionaries.
    """
    # Create a list of random number of empty dicts
    random_dicts = [{} for _ in range(random.randint(min_dicts, max_dicts))]

    # For each dict in the list
    for d in random_dicts:
        # Assign a random number of keys
        for _ in range(random.randint(min_keys, max_keys)):
            # The key is a random letter, the value is a random number within the specified range
            d[random.choice(string.ascii_lowercase)] = random.randint(min_value, max_value)

    return random_dicts


# Test the function
# print(generate_dicts(3, 5, 0, 3, 0, 5))


# The second task from the module 2
def merge_dicts(dicts_to_work):
    """
    Merge a list of dictionaries into a single one.

    Args:
    dicts : List[dict]
      List of dictionaries to merge.

    Returns:
    dict
      The merged dictionary.
    """

    # Initialize an empty dictionary to hold the final result
    final_dict = {}

    # Enumerate over the list of dictionaries
    for i, d in enumerate(dicts_to_work):
        # For each key, value pair in the current dictionary
        for k, v in d.items():
            # If the key is already in our final dict and the current value is higher
            if k in final_dict and v > final_dict[k]:
                # We remove the old key
                final_dict.pop(k)
                # And add the key with _dict_number as suffix and the new max value
                final_dict[k + f'_{i + 1}'] = v
            # If the key isn't in the final dict yet, we just add the key-value pair
            elif k not in final_dict:
                final_dict[k] = v
    return final_dict


# Test the function
dicts = generate_dicts(2, 10, 1, 10, 0, 100)
# print(merge_dicts(dicts))


# The task from Module 3
# Normalize sentences


# define the function
def normalize_sentences(text_to_correct):
    """
    Normalize all sentences in a block of text. Each sentence should start with a capital
    letter, with the rest of the sentence in lower case.
    """
    # Split the text into lines using '\n' as a separator
    lines = text_to_correct.split('\n')
    # Initialize an empty list to hold the normalized sentences
    normalized_lines = []

    # Iterate over each line
    for line in lines:
        # Further split each line into sentences using a regex pattern that matches '.', '!', '?' and ':'
        sentences = re.split('(?<=[.!?:]) ', line)
        # Normalize each sentence
        sentences = [sentence.capitalize() for sentence in sentences]
        # Combine the sentences back together and add the normalized line to our list
        normalized_lines.append(' '.join(sentences))

    # Join the lines back together with line breaks and return
    normalized_text = '\n'.join(normalized_lines)

    return normalized_text


# Text for testing
text = """homEwork:

tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# print(normalize_sentences(text))


# A sentence with the last words
def add_sentence_with_last_words(text_to_work):
    """
    This function creates a new sentence from the last word of each existing sentence in the text.
    The new sentence is added at the end of the text.
    """
    # Split the text into sentences using regex pattern matching '.', '!', '?' and ':'
    sentences = re.split(r'(?<=[.!?])\s', text_to_work)

    # create a translator to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Extract the last word from each sentence ensuring if a sentence has one or more words
    # Removing any punctuation from the word
    last_words = [s.split()[-1].translate(translator) for s in sentences if s.split()]

    # Create a new sentence from the last words
    new_sentence = ' '.join(last_words)

    # Add the new sentence at the end of the text
    text_to_work += '\n' + new_sentence.capitalize() + '.'

    return text_to_work


# Test the function
# print(add_sentence_with_last_words(text))


# 3 correct "IZ"

def fix_mistake(text_to_work):
    """
    This function replaces incorrect "iz" with "is". Only those "iz" that occur as a separate word are replaced.
    """
    # Use regular expressions (re) to replace ' iz ' with ' is '
    # \b allows to perform a "whole words only" search
    fixed_text = re.sub(r'\biz\b', 'is', text_to_work)

    return fixed_text


# 4 number of whitespace characters

# Define a function that counts all whitespace characters in a string.
def count_whitespace(s):
    # Count all spaces in the text
    # Count all sequences of two newline characters in the text (which represent blank lines)
    # Count all periods in the text.
    return s.count(' ') + s.count('\n\n') * 2 + s.count('.')
