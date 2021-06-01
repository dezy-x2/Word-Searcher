#imports a randomizer to randomly select leters
import random
#imports something to delay functions for show
import time
#keeps track of time 
import datetime
#list of words
from english_words import english_words_lower_alpha_set

from tqdm import *

wordList = english_words_lower_alpha_set
#test
newWordList = []

#takes words out of wordlist that are bigger than 2 chars and makes it properly itteratable
for word in wordList:
    if len(word) > 2:
        newWordList.append(word)
# print(ord("b") - 97)

#creates a list with 26 sub lists
orgAlph = [[] for num in range(0, 26)]

#sorts each word into the proper sublist using the ord() function
for word in newWordList:
    orgAlph[ord(word[0]) - 97].append(word)

# print(len(orgAlph[0]))

# print(len(testArr) // 2)

#creates the binary search neccessary to properly itterate through the sub lists
def binarySearch(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        midIdx = (left + right) // 2

        if midIdx + 97 == ord(target):
            return midIdx

        elif ord(target) < midIdx + 97:
            right = midIdx
        
        elif ord(target) > midIdx + 97:
            left = midIdx + 1

# binarySearch(orgAlph, "t")

# minLen = 0
# idx = None
# for word in orgAlph:
#     if len(word) > minLen:
#         minLen = len(word)
#         idx = word
# print(minLen, idx)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

aphWNums = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']



#makes the statement that it searches for words in 

def createStatementOfficial(length, source):
    print(f"Started at approximatley {datetime.datetime.now()}")
    final = ""
    for _ in tqdm(range(length),desc="generating statement"):
        rand = random.randint(0,len(source) - 1)
        letter = source[rand]
        final += letter
    print(f"Finished selection at {datetime.datetime.now()}")
    return final

def createStatementFun(length, source):
    final = ""
    for _ in range(length):
        rand = random.randint(0, len(source) -1)
        letter = source[rand]
        final += letter
        time.sleep(0.01)
        print(final)

orgDict = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}

def searchStatement(given, reference):
    foundTotalUnique = 0
    foundTotal = 0
    foundWords = []
    for i in tqdm(range(len(given)), desc="searching statement"):
        #calls binary search on the given letter
        binaryResults = orgDict[given[i]]   #binarySearch(reference, given[i])
        for word in reference[binaryResults]:
            if given[i:len(word) + i] == word:
                foundWords.append(word)

    foundTotal = len(foundWords)
    foundWords = list(set(foundWords))
    foundTotalUnique = len(foundWords)

    return foundTotal, foundTotalUnique, foundWords

totalFound, totalUniqueFound, wordsFound = searchStatement(createStatementOfficial(1000000, alphabet), orgAlph)

print(f"The total amount of found words is: {totalFound}")
print(f"The total amount of unique words is: {totalUniqueFound}")
# print(f"I was able to find {wordsFound}") 
print(f"Finished up at {datetime.datetime.now()}")

# createStatementFun(1000, alphabet)