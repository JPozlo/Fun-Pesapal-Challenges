import trafilatura
import nltk
import string
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Use the trafilatura module to fetch the page and extract text from it
downloaded = trafilatura.fetch_url('https://pesapal.freshteam.com/jobs/-z8xM8RCgTx7/junior-developer')
text = trafilatura.extract(downloaded)

# Use the word_tokenize method from nltk to get the word tokens from the extracted text
tokenized_words = word_tokenize(text)

# Filter out the punctuations eg '.' or ','
punctuations = list(string.punctuation)
filtered_word_tokens = []
for i in tokenized_words:
    if i not in punctuations:
        filtered_word_tokens.append(i)

word_dictionary = dict()

# Loop through all the filtered words and if they occur more than once, add 1 to their count of occurence
for word in filtered_word_tokens:
    word = word.strip()
    word = word.lower()


    if word in word_dictionary:
        word_dictionary[word] = word_dictionary[word] + 1
    else:
        word_dictionary[word] = 1

# Write the dictionary words in sorted order into a file
temp_file_dict_sorted = open('dict_unique_words_sorted.txt', 'w')
for word in sorted(word_dictionary):
    temp_file_dict_sorted.write(word + "\n")
temp_file_dict_sorted.close()

# Write the unique words together with their occurence count into a file
temp_file_dict = open('dict_unique_words.txt', 'w')
for key in list(word_dictionary.keys()):
    temp_file_dict.write(key + " : " + str(word_dictionary[key]) + "\n")
temp_file_dict.close()