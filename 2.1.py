
import numpy as np
from random import randint
import statistics as stats

# this was the best way I could turn this in as a python file

FirstName = "Seth"
LastName = "Adams"
StudentIDNumber = 101
print("My name is " + FirstName + " " + LastName + " and my ID is " + StudentIDNumber)


numList = [24,84,28,55,58,82,98,12,14,8,64,30,78]
print(stats.median(numList))

fruitAlphabet = ['apple', 'banana', 'pineapple', 'mango', 'watermelon', 'peach']

alphabet = ['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
print(len(alphabet))


alphabet.insert(6, 'g')
alphabet.insert(25, 'z')
print(len(alphabet))

print(alphabet[2:16])

del alphabet[0]
del alphabet[3]
del alphabet[6]
print(alphabet)

alphabet.remove('o')
alphabet.remove('u')
print(alphabet)

print(alphabet + fruitAlphabet)






classDays = ('monday', 'wednesday', 'friday')
daysOff = ('tuesday', 'thursday')
allDays = classDays + daysOff
print(allDays)




newDict = {"FirstName": "Seth", "LastName": "Adams", "ClassStanding": "Senior"}
print(newDict)
newDict["Age"] = "22"
newDict["StudentIDNumber"] = "801091940"
print(newDict)
del newDict["ClassStanding"]
print(newDict)

allNumbers = set(range(1,20))
print(allNumbers)

evenNumbers = set(range(0,11,2))
print(evenNumbers)

allNumbers = set(range(1,21))

print(allNumbers.intersection(evenNumbers))

print(allNumbers.union(evenNumbers))




# maxRange([10, 15, 20, 2, 10, 6]) ➞ 18
# maxRange([3, 6, -9, -4, -2, 15]) ➞ 24
def maxRange():
    x = [10, 15, 20, 2, 10, 6]
    y = min(x)
    z = max(x)

    difference = z-y
    return difference
print(maxRange())