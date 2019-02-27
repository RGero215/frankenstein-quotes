import random
import re



def histogram(file_name):
    #.0 Declear an empty dictionaries for words, frequency and merge
    words = []
    frequency = []
    merge = []
    # .1 Open on read mode  
    file_object = open(file_name, "r", encoding="utf-8-sig")
    # .2 Assigned file read to a variable
    no_punctuation_file = file_object.read()
    # .3 Use regular expresion to remove puntuation
    no_punctuation_file = re.sub(r'[^\w\s]','',no_punctuation_file)
    # .4 Storage an array of words without puntuations
    word_count = no_punctuation_file.split()
    #.5 Itinirate the array of words
    for word in word_count:
        #.6 If word not in words
        if word not in words:
            #.7 append word to words 
            words.append(word)
            #.8 append one to frequency
            frequency.append(1)
        else:
            #.9 else find the index of the word in words
            index = words.index(word)
            #.10 add one to the frequency index
            frequency[index] += 1
    #.11 merge list of words and list of frequency into a list of list according indexes ex: [1,2] and [a,b] = [[1,a],[2,b]]    
    merge = [(words[i], frequency[i]) for i in range(0, len(words))]
    # print(merge)
    #.12 Return words dictionary
    # print(type(merge[1]))
    return merge
    


# Define function that takes and histogram and return a unique word's count
def unique_words(histogram):
    #.1 Empty list to count the len
    number_of_unique_words = []
    #.2 Itinirate the dictionary
    for word, count in histogram:
        #.3 Words with value 1 or unique words
        if count == 1:
            #.4 Append unique words to the list
            number_of_unique_words.append(word)
    #.5 Return unique word's count
    print("Unique Words", len(number_of_unique_words))
    return len(number_of_unique_words)
    

# Define a function that takes a word and an histogram and return the frequency of the word
def frequency(input_word, histogram):
    #.1 Itinirate the dictionary
    for word, count in histogram:
        #.2 compare the word input to key
        if word == input_word:
            #.3 return the value or the frequency total
            print(count)
            return count
        
    #.4 return a message if the word is not in the histogram
    print("The word: {} is excluded in this histogram".format(input_word))
    return "The word: {} is excluded in this histogram".format(input_word)







if __name__ == "__main__":
    # histogram("one fish two fish red fish blue fish")
    histogram("Frankenstein.txt")
    # unique_words(histogram("Frankenstein.txt"))
    # frequency("Frankenstein", histogram("Frankenstein.txt"))




    