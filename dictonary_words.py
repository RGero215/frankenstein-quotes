#!/usr/bin/env python3
import random

# Define function that takes a number of words and output a sentence with those words
def words(number_of_words):
    #.0 Empty array to store words
    new_words_list = []
    #.1 Open and read file words 
    file_object = open("/usr/share/dict/words", "r")
    # str.rstrip() remove white space in both sides and .strip() removed at the end
    #.2 list of words in the file
    words = file_object.read().split()
    for i in range(0, number_of_words):
        #.3 Select random word
        random_number = random.randint(0, len(words) - 1)
        word = words[random_number]
        #.4 Random set of words list 
        new_words_list.append(word)
    #.5 Ouput the sentence
    print(' '.join(new_words_list))
    return ' '.join(new_words_list)




if __name__ == "__main__":
    words(5)
    