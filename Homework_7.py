import re
import collections
import csv

# define func for read the file and count the words
def read_and_create_word_counter(filename):
    with open(filename, 'r') as f:
        # Read the contents of the file
        contents = f.read()

        # Remove dates formatted like YYYY-MM-DD from the contents
        contents = re.sub(r'\b\d{4}[-]\d{2}[-]\d{2}\b', '', contents)

        # Remove non-alphabetic characters
        contents = re.sub(r'[^a-zA-Z\s]', '', contents)
        # Convert to lower case
        contents = contents.lower()
        # Split the contents into a list of words
        words_list = contents.split()

    # Count the number of occurrences of each word
    counter = collections.Counter(words_list)
    # Write the counts to a CSV file
    with open('word_counts.csv', 'w') as file:
        writer = csv.writer(file, delimiter="-", quotechar=" ", quoting=csv.QUOTE_ALL)
        for word, count in counter.items():
            writer.writerow([word, count])

# Define the func for letter's count

def letter_analizy(filename):
    with open(filename, 'r') as f:
        # Read the contents of the file
        contents = f.read()

        # Remove dates formatted like YYYY-MM-DD from the contents
        # contents = re.sub(r'\b\d{4}[-]\d{2}[-]\d{2}\b', '', contents)

        # Remove non-alphabetic characters
        contents = re.sub(r'[^a-zA-Z\s]', '', contents)

        # create conter variables
        total_chars = 0
        chars_counter = collections.defaultdict(int)
        uppercase_counter = collections.defaultdict(int)

        for char in contents:
            if char.isalpha():  # We count only letters
                total_chars += 1
                chars_counter[char.lower()] += 1  # Convert all to lowercase for counting
                if char.isupper():
                    uppercase_counter[char.lower()] += 1  # Count uppercase occurrences
        # Prepare data for csv
        csv_data = []
        for char in chars_counter:
            # create a dict
            row = {'Letter': char, 'Count': chars_counter[char], 'Uppercase Count': uppercase_counter[char],
                   'Percentage': str(round((chars_counter[char] / total_chars) * 100, 2)) + '%'}
            csv_data.append(row)

    # create a list with field
    fields = ['Letter', 'Count', 'Uppercase Count', 'Percentage']

    # Write data to csv file
    with open('letter_count.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()  # Write header
        for i in csv_data:
            writer.writerow(i)  # add each item from the list

# read_and_create_word_counter('my_news_feed.txt')
# letter_analizy('my_news_feed.txt')