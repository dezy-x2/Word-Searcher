#imports a randomizer to randomly select leters
import random
#imports something to delay functions for show
import time
#keeps track of time 
import datetime
#list of words
from english_words import english_words_lower_alpha_set
#imports a progress bar
from tqdm import tqdm
#need this to plot graphs
from matplotlib import pyplot as plt 
#histograms expect a np array
import numpy as np
#WORDS
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

def statementAnalytics(statement):
    sortedStatement = [[] for _ in range(26)]
    percentages = []
    for letter in statement:
        sortedStatement[ord(letter) - 97].append(letter)
    # print(sortedStatement)
    for arr in sortedStatement:
        percentages.append((arr[0], len(arr)/len(statement)))
    #e,t,a,o,i
    frequencyAnalysis = percentages[0][1] + percentages[4][1] + percentages[19][1] + percentages[14][1] + percentages[8][1]
    return percentages, frequencyAnalysis

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

    stateAnalytics, frequency = statementAnalytics(given)

    # print(f"The total amount of found words is: {foundTotal}")
    # print(f"The total amount of unique words is: {foundTotalUnique}")
    # print(f"I was able to find {foundWords}") 
    print(f"Statement analytics: \n {stateAnalytics}")
    print(f"\nETAOI frequency is {frequency}")
    print(f"Finished up at {datetime.datetime.now()}")

    return foundTotal, foundTotalUnique, foundWords, stateAnalytics, frequency

# totalFound, totalUniqueFound, wordsFound, analytics, frqAnalytics = searchStatement(createStatementOfficial(1000, alphabet), orgAlph)



# etaoiTemp = [[] for _ in range(12)]
its = [[] for _ in range(12)]
for j in range(12):
    newStatement = createStatementOfficial(10000, alphabet)
    for i in range(50):
        start = time.time()
        print(f"Run {j+1}.{i+1}")
        searchStatement(newStatement, orgAlph)
        print("\n")
        end = time.time()
        # etaoiTemp = freq
        its[j].append(10000 / (end - start))

# etaoi = [etaoiTemp for _ in range(10)]

print(its)

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9), (ax10, ax11, ax12)) = plt.subplots(4,3)

ax1.hist(np.array(its[0]), range=(2000, 3500), bins=15)
ax2.hist(np.array(its[1]), range=(2000, 3500), bins=15)
ax3.hist(np.array(its[2]), range=(2000, 3500), bins=15)
ax4.hist(np.array(its[3]), range=(2000, 3500), bins=15)
ax5.hist(np.array(its[4]), range=(2000, 3500), bins=15)
ax6.hist(np.array(its[5]), range=(2000, 3500), bins=15)
ax7.hist(np.array(its[6]), range=(2000, 3500), bins=15)
ax8.hist(np.array(its[7]), range=(2000, 3500), bins=15)
ax9.hist(np.array(its[8]), range=(2000, 3500), bins=15)
ax10.hist(np.array(its[9]), range=(2000, 3500), bins=15)
ax11.hist(np.array(its[10]), range=(2000, 3500), bins=15)
ax12.hist(np.array(its[11]), range=(2000, 3500), bins=15)
plt.show()

# createStatementFun(1000, alphabet)