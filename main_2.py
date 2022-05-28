# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from importlib.resources import contents
from itertools import count
from pyparsing import line


def read_file_content(filename):
    # [assignment] Add your code here 
    with open('./story.txt', 'r') as f:
        contents = f.read()
        #print(contents)
    
    return contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count = dict()
    words = text.split()
    for word in words:
        if word in count:
            count[word] =+ 1
        else:
            count[word] = 1
    return (count)
print(count_words())






    #/Users/mode007/Downloads/Reading-Text-Files