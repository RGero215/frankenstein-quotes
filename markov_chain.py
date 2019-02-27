from dictogram import *
from histogram_dictionary import sample, word_list

# To run: python3 markov_chain.py

def markov_chain(word_list):
    """Takes a word_list and number_of_words to generate a 
    sentence with a range of words between 5 and number_of_words or a shorter sentence if the no more words to 
    follow the markov chain"""
    ended = False
    sentence = []
    new_list = []
    histogram = Dictogram(word_list)
    current_word = sample(histogram)
    sentence.append(current_word)
    if current_word is None: 
            print("Try running: python3 markov_chain.py")
            ended = True
    else:
        while not ended:
            print("Selected word: ", current_word)
            print("******************************")
            for index, word in enumerate(word_list):
                try:
                    if word == current_word:
                        print("Word after {}: ".format(word), word_list[index + 1])
                        new_list.append(word_list[index + 1])
                except IndexError:
                    ended = True
                    break
        
            if ended == False:
                histogram = Dictogram(new_list)
                current_word = sample(histogram)
                print(histogram)
                print('----------------------------')
                sentence.append(current_word)
                new_list = []
            else:
                break
        print(' '.join(sentence))

if __name__ == "__main__":
    # markov_chain(word_list("Frankenstein.txt"))
    # markov_chain('how to find keys by value in dictionary and how to look if certain value exists'.split())
    stats = ["curveball", "single", "fastball", "double", "changeup", "home run", "slider", "triple", "fastball", "out", "fastball", "out", "curveball", "home run", "fastball", "triple", "changeup", "out"]
    markov_chain(stats)

