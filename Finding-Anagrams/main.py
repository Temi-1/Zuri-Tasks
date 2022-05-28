# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

import string 

#accept and convert user input to lowercase
str1 = input("Enter 1st word: ").lower()
str2 = input("Enter 2nd word: ").lower()


def find_anagram(word, anagram):
    punct = string.punctuation
    #add whitespace to punctuation list
    punct = punct + ' '
    #eliminate punctuation and whitespace
    for i in punct:
        word = word.replace(i, '')
        anagram = anagram.replace(i, '')
    if sorted(word) == sorted(anagram):
        print("They're anagrams!")
        return True
    else:
        print("Oops! not anagrams.")
        return False
        
find_anagram(str1, str2)


