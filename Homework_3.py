
#import libraly for RegEx
import re
#copy the text to the variable
text = """homEwork:
tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# 1 letter normalize
# Cut the first word with colon
Homework_word = re.search(r'h.*?:', text).group()

# divide the text into two parts by the colon
sentences = text.split(':')

#select the sentences without Homework
sentences_without_Homework = sentences[1].split('.')

# create the list for the text with correct capitalize
All_sentences = []

# Add the Homework word
All_sentences.append(Homework_word)
# add other sentences without the last
for i in range(len(sentences_without_Homework)-1):
    All_sentences.append(sentences_without_Homework[i] + ".")

#capitalize all sentences
capitalized_sentences = [s.strip().capitalize() for s in All_sentences]

# join all sentences to one text
capitalized_text = '\n \n'.join(capitalized_sentences)
print(capitalized_text)

# 2 A sentence with the last words
# Get last words of each sentence
last_words = [s.split()[-1] for s in capitalized_sentences]

#Delete Homework word
last_words.pop(0)

#Delete the dot symbol
#New empty list
New_List_without_dots = []
#Traverse through all sentence from the list
for i in range(len(last_words)):
    #all elements except the last one are added without dot
    if i != len(last_words) - 1:
        New_List_without_dots.append(last_words[i][:-1])
    else:
    #The last element is added with dot
        New_List_without_dots.append(last_words[i])

#Generate the sentence
text_with_last_words = " ".join(New_List_without_dots).capitalize()

# Add the new sentences to the text
New_text = capitalized_sentences + [text_with_last_words]

#Generate the new text
New_capitalized_text = '\n \n'.join(New_text)


# 3 correct "IZ"
# create an empty list
fixed_sentences = []

#Traverse through all sentence from the list
for s in New_text:
    # Correct "iZ" to "is" in the right context
    sentence = re.sub(r'\biz\b', 'is', s, flags=re.IGNORECASE)
    #add correct sentences
    fixed_sentences.append(sentence)

#Generate the new text
New_correct_text = '\n \n'.join(fixed_sentences)
print(New_correct_text)

# 4 number of whitespace characters

# Define a function that counts all whitespace characters in a string.
def count_whitespace(s):
    # Count all spaces in the text
    # Count all sequences of two newline characters in the text (which represent blank lines)
    # Count all periods in the text.
    return s.count(' ') + s.count('\n\n')*2 + s.count('.')
print(count_whitespace(text))





