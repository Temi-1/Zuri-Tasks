# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string

def read_file_content():
    with open ('story.txt', 'r') as file:        
        content = file.read()
        return content

def count_words():
    text = read_file_content()

    #remove punctuation
    for i in string.punctuation:
        text = text.replace(i, '')
    
    text_list = text.split()
    count_dict = {}

    for word in text_list:
        if word in count_dict.keys():
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    print(count_dict)

count_words()