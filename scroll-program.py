#imports a randomizer to randomly select leters
import random
#imports something to delay functions for show
import time
#keeps track of time 
import datetime
#list of words
from english_words import english_words_lower_alpha_set

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

print(f"Started at approximatley {datetime.datetime.now()}")

#makes the statement that it searches for words in 

def createStatementOfficial(length, source):
    final = ""
    for _ in range(length):
        rand = random.randint(0,len(source) - 1)
        letter = source[rand]
        final += letter
        # time.sleep(0.01)
        # print(final)
    return final

def createStatementFun(length, source):
    final = ""
    for _ in range(length):
        rand = random.randint(0, len(source) -1)
        letter = source[rand]
        final += letter
        time.sleep(0.01)
        print(final)

print(f"Finished selection at {datetime.datetime.now()}")

def progressBar(i, given, word, reference, binaryResults):
    if i == len(given) * 0.02 and word == reference[binaryResults][0]:
        print("2% of the way there! ========================")
        print(f"At {datetime.datetime.now()}")
    elif input == len(given) * 0.05 and word == reference[binaryResults][0]:
        print("5% of the way there! =================================")
        print(f"At {datetime.datetime.now()}")
    elif i == len(given) / 4 and word == reference[binaryResults][0]:
        print("25% of the way there! ==========================================")
        print(f"At {datetime.datetime.now()}")
    elif i == len(given) / 2 and word == reference[binaryResults][0]:
        print("50% of the way there! ===========================================================")
        print(f"At {datetime.datetime.now()}")
    elif i == len(given) * 0.75 and word == reference[binaryResults][0]:
        print("75% of the way there! ==================================================================================")
        print(f"At {datetime.datetime.now()}")

def searchStatement(given, reference):
    foundTotalUnique = 0
    foundTotal = 0
    foundWords = []
    for i in range(len(given)):
        #calls binary search on the given letter
        binaryResults = binarySearch(reference, given[i])
        for word in reference[binaryResults]:
            if given[i:len(word) + i] == word:
                foundTotal += 1
                if not word in foundWords:
                    #sifts through and decided if it is a new word or and old word and counts them as such
                    foundWords.append(word)
                    foundTotalUnique += 1
        
            #gives us the percentages that it is at (time consuming unfortunately)
            # progressBar(i, given, word, reference, binaryResults)

    return foundTotal, foundTotalUnique, foundWords

totalFound, totalUniqueFound, wordsFound = searchStatement(createStatementOfficial(1000, alphabet), orgAlph)

print(f"The total amount of found words is: {totalFound}")
print(f"The total amount of unique words is: {totalUniqueFound}")
print(f"I was able to find {wordsFound}") 
print(f"Finished up at {datetime.datetime.now()}")

# createStatementFun(1000, alphabet)