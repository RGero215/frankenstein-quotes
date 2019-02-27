#!/usr/bin/env python3
import random
import re

def word_list(file_name):
    """Function takes a file and return a word list no puntuations"""
    words = {}                       
    file_object = open(file_name, "r", encoding="utf-8-sig")
    no_punctuation_file = file_object.read()
    #.3 Use regular expresion to remove puntuation
    no_punctuation_file = re.sub(r'[^\w\s]','',no_punctuation_file)
    #.4 Storage an array of words without puntuations
    word_list = no_punctuation_file.split()
    return word_list

def histogram(file_name):
    """ Function takes a file name as an argument and return an histogram of words and frequency """
    words = {}                       
    file_object = open(file_name, "r", encoding="utf-8-sig")
    no_punctuation_file = file_object.read()
    #.3 Use regular expresion to remove puntuation
    no_punctuation_file = re.sub(r'[^\w\s]','',no_punctuation_file)
    #.4 Storage an array of words without puntuations
    word_list = no_punctuation_file.split()
    for word in range(len(word_list)):
        if word_list[word] in words:
            words[word_list[word]] += 1
        else:
            words.update({word_list[word]: 1})
    return words
    



def unique_words(histogram):
    """ function that takes and histogram and return a unique word's count """
    number_of_unique_words = []
    for key, value in histogram.items():
        if value == 1:
            number_of_unique_words.append(key)

    return len(number_of_unique_words)
    

def frequency(word, histogram):
    """ function that takes a word and an histogram and return the frequency of the word """
    for key, value in histogram.items():
        if key == word:
            return value
    return "The word: {} is excluded in this histogram".format(word)


def random_word(histogram):
    """ function that takes a histogram and output a random word not taking under account the distributions of the words """
    word = random.choice(list(histogram.keys()))
    return word


def weighted_random(histogram):
    """ weighted random function with choice """
    my_list = []
    for key, value in histogram.items():
        my_list += [key] * value
    weighted_random_choice = random.choice(my_list)
    return weighted_random_choice

def sample(histogram):
    """ weighted random with uniform """
    total = 0
    cumulative_probability = 0

    for key, value in histogram.items():
        total += value
    random_num = random.uniform(0,1)
    for key, value in histogram.items():
        cumulative_probability += value / total
        if cumulative_probability >= random_num:
            return key



def multiple_runs(histogram):
    """ takes a histogram as an argument. Runs 1,000 times selecting a random work each time and return another histogram with the words selected and frequency selected """
    count_dict = dict()

    for item in histogram.items():
        count_dict[item[0]] = 0
    for i in range(0,1000):
        count_dict[sample(histogram)] += 1
    
    print(count_dict)







if __name__ == "__main__":
    # histogram("Frankenstein.txt")
    # unique_words(histogram("Frankenstein.txt"))
    # random_word(histogram("Frankenstein.txt"))
    # weighted_random(histogram("Frankenstein.txt"))
    # multiple_runs(weighted_random(histogram("Frankenstein.txt")))
    multiple_runs(histogram("Frankenstein.txt"))
    

    frequency("was", histogram("Frankenstein.txt"))
    frequency("the", histogram("Frankenstein.txt"))
    frequency("PG", histogram("Frankenstein.txt"))
    frequency("was", histogram("Frankenstein.txt"))

    
