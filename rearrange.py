import sys
import random
#.1 define a function that will take argumentes from the command line 
def rearrange():
    new_list = []
    #.2 starting from the second argument to avoid files name
    command_line_arguments_list = sys.argv[1:]
    for item in range(len(command_line_arguments_list)):
        random_item = random.choice(command_line_arguments_list)
        new_list.append(random_item)
        command_line_arguments_list.pop(command_line_arguments_list.index(random_item))
    #.3 return the arguments arrange in alphabetical order
    return ' '.join(new_list)

if __name__ == "__main__":
    words = rearrange()
    print(words)