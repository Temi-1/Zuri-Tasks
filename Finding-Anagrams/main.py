# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

import string 

str1 = input("Enter 1st word: ").lower()
str2 = input("Enter 2nd word: ").lower()


def find_anagram(word, anagram):
    punct = string.punctuation
    punct = punct + ' '
    for i in punct:
        word = word.replace(i, '')
        anagram = anagram.replace(i, '')
    if sorted(word) == sorted(anagram):
        print("They're anagrams!")
        return True
        
find_anagram(word=str1, anagram=str2)