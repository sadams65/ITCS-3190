# %% [markdown]
# # Part 1: Declaring Variables and Printing

# %% [markdown]
# #### You may be familiar with the conventional way of initializing variables, shown below:

# %%
x = "ITCS 3190"

# %%
print(x)

# %% [markdown]
# #### Python, however, offers another way of initializing variables, in which you can do it in one line. To do this, delimit the variable names and the variable values as shown below

# %%
a,b = "Python", 3

# %%
print(a)

# %%
print(b)

# %% [markdown]
# #### Now try and initialize three variables, "FirstName", "LastName", and "StudentIDNumber" using a similar method. Make sure to use your name and student ID number for this part.

# %%
FirstName = "Seth"
LastName = "Adams"
StudentIDNumber = 101

# %% [markdown]
# #### Now, let's try and print it all on one line, saying "My name is (FirstName) (LastName), and my Student ID number is (StudentIDNumber)." using Python's simple "print" statement. One thing to note is that Python does not support concatenating strings and ints, so you may have to figure out how to cast age to a string value to get this to work successfully.

# %%
print("My name is " + FirstName + " " + LastName + " and my ID is " + StudentIDNumber)

# %% [markdown]
# # Part 2: Importing Libraries

# %% [markdown]
# #### We will be using a variety of libraries this semester, including numpy, pandas, and sklearn, so it is necessary to know how to import modules, and can be done as seen below.

# %%
import pandas
import numpy as np
from random import randint

# %% [markdown]
# #### Now, import the "statistics" module as "stats" and use the median method to find the median of the list below in the empty cell

# %%
numList = [24,84,28,55,58,82,98,12,14,8,64,30,78]

# %%
print(stats.median(numList))

# %% [markdown]
# # Part 3: Lists

# %% [markdown]
# #### First let's explore how to declare a list, and then the operations we can do upon a list

# %%
fruits = ["apple", "banana", "pineapple", "mango", "watermelon"]

# %% [markdown]
# #### We can find the length of the list

# %%
len(fruits)

# %% [markdown]
# #### We can index the items in a list, and even index a particular item

# %%
fruits[2]

# %%
fruits[2][5]

# %% [markdown]
# #### We can also slice lists, and we do so using the format below

# %%
fruits[2:]

# %%
fruits[:3]

# %%
fruits[2:4]

# %%
fruits[::2]

# %% [markdown]
# #### The general format for the slicing is [start:stop:step], with step being 1 by default. The start is inclusive, and the stop is exclusive, meaning if you go from index 1 to index 4, it will include index 1 up through the index immediately before index 4, which would be index 3. The step value tells us how big steps should be from one item to the next in the slice. Whether we should include every item, every other item, every 3rd item, etc.

# %% [markdown]
# #### You can also add items to the end of the list

# %%
fruits.append('peach')
fruits

# %% [markdown]
# #### You can add items in at a specific index

# %%
fruits.insert(1, 'plum')
fruits

# %% [markdown]
# #### You can delete items at specific index

# %%
del fruits[1]
fruits

# %% [markdown]
# #### You can delete items by name as well

# %%
fruits.remove('peach')
fruits

# %% [markdown]
# #### Now, take the below list named alphabet, and use the above operations to follow the instructions in each step. Make sure to write the list name on a new line after the operation to print the list in Jupyter and ensure you are doing the right thing as I have done above with the fruits list.

# %%
alphabet = ['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']

# %% [markdown]
# #### Use a function to find the length of the list and make sure it is the correct length

# %%
print(len(alphabet))

# %% [markdown]
# #### If the list is not the correct length, use the add operations above to correct the alphabet

# %%
alphabet.insert(6, 'g')
alphabet.insert(25, 'z')

# %% [markdown]
# #### Print every other item in the list from item 2 to item 15

# %%
print(alphabet[2:16])

# %% [markdown]
# #### Remove the first three alphabetically occuring vowels by their indices

# %%
del alphabet[0]
del alphabet[3]
del alphabet[6]

# %% [markdown]
# #### Remove the remaining vowels by their value

# %%
alphabet.remove('o')
alphabet.remove('u')

# %% [markdown]
# #### Print the final list

# %%
print(alphabet)

# %% [markdown]
# #### You can also add lists together and make a new list using +. Use the + to make a new list called fruitAlphabet.

# %%
print(alphabet + fruitAlphabet)

# %% [markdown]
# # Part 4: Tuples

# %% [markdown]
# #### If you recall, tuples are immutable, so there are limited things we can do to them. We cannot add or remove items, but we can print them and find items at particular indices

# %%
fruits1 = ('apple','banana','mango')
fruits1

# %%
len(fruits1)

# %%
fruits1[1]

# %% [markdown]
# #### Tuples being immutable means that we can not alter the data inside of them. We can, however, still add tuples as we can add lists.

# %%
fruits2 = ('pineapple','watermelon')
fruits3 = fruits1 + fruits2
fruits3

# %% [markdown]
# #### As practice, create a tuple containing the list of days this class falls on called "classDays", and add it to another tuple with the weekdays that this class does not fall on called "daysOff". (It should create an out of order list of the 5 weekdays)

# %%
classDays = ('monday', 'wednesday', 'friday')
daysOff = ('tuesday', 'thursday')
allDays = classDays + daysOff
print(allDays)

# %% [markdown]
# # Part 5: Dictionaries

# %% [markdown]
# #### If you recall, dictionaries are used to store key-value pairs, and you can see them in action below

# %%
newDict = {"FirstName": "Gavin", "LastName": "Sidhu", "Age": 21}

# %% [markdown]
# #### If you want to access a particular value, you do it similar to lists, except you want to use the key name instead of the index

# %%
newDict["FirstName"]

# %% [markdown]
# #### If you want to add a new key-value pair to the dictionary, you can just use a new key name and assign it a value

# %%
newDict["Position"] = "Teaching Assistant"
newDict["Position"]

# %% [markdown]
# #### Here are some other functions with which you can retrieve the keys, values, and items from a dictionary

# %%
newDict.keys()

# %%
newDict.values()

# %%
newDict.items()

# %% [markdown]
# #### You may also delete a key-value pair by referencing the key name 

# %%
del newDict["Age"]
newDict

# %% [markdown]
# #### Now, create a dictionary that contains keys "FirstName", "LastName","ClassStanding" with values corresponding to you

# %%
newDict = {"FirstName": "Seth", "LastName": "Adams", "ClassStanding": "Senior"}
print(newDict)

# %% [markdown]
# #### Now, add 2 keys named "Age" and "StudentIDNumber" with the corresponding values

# %%
newDict["Age"] = "22"
newDict["StudentIDNumber"] = "801091940"

# %% [markdown]
# #### Finally, remove the ClassStanding key-value pair

# %%
del newDict["ClassStanding"]

# %% [markdown]
# #### Print the new dictionary

# %%
print(newDict)

# %% [markdown]
# # Part 6: Sets

# %% [markdown]
# #### Sets are unique and can only contain unique values. They are declared using curly braces as can be seen below

# %%
numSet = {1,2,3,4,5,6,6,6,6,6,6,6,7,7,8,8,8,8,9}
numSet

# %% [markdown]
# #### You can also add or remove values 

# %%
numSet.add(16)
numSet

# %%
numSet.remove(3)
numSet

# %% [markdown]
# #### Much like in stats you can also do union or intersection operations on sets

# %%
numSet2 = set(range(0,20,2))
numSet2

# %%
print(numSet.intersection(numSet2))

# %%
print(numSet & numSet2)

# %%
print(numSet.union(numSet2))

# %%
print(numSet | numSet2)

# %% [markdown]
# #### Figure out how to use the range() function above to make a set called "allNumbers" with numbers from 1 to 19 (inclusive)

# %%
allNumbers = set(range(1,20))

# %% [markdown]
# #### Now make another set with the range() function to make a set called "evenNumbers" with even numbers from 0 through 10 (inclusive)

# %%
evenNumbers = set(range(0,11,2))

# %% [markdown]
# #### Add the number 20 to the first set

# %%
allNumbers = set(range(1,21))

# %% [markdown]
# #### Remove 0 from the second set

# %%
evenNumbers = set(range(1,11,2))

# %% [markdown]
# #### Calculate the intersection of these sets

# %%
print(allNumbers.intersection(evenNumbers))

# %% [markdown]
# #### Calculate the union of these sets

# %%
print(allNumbers.union(evenNumbers))

# %% [markdown]
# # Part 7: Miscellanous

# %% [markdown]
# #### So far, we've seen how to do basic functions on the most common data structures, but soon, you may have to start using them in conjunction with other common programming concepts like loops, if statements, etc. When getting into Python that might require multiple lines, it is necessary to include colons. These colons indicate that the next block of code needs to be 1) indented and 2) that it is a smaller/more local block of code. It's similar to the difference between putting code inside and outside of a set of brackets in Java.

# %% [markdown]
# ### Part 7.1: For Loops

# %% [markdown]
# #### Here we have a regular for loop. You can set a variable name for the items in the iterable object you are trying to loop through. On each pass through the loop, that variable name holds a different value. In our case below, we named our variable "fruit", and we have it printed on each pass through the for loop as can be seen below.

# %%
for fruit in fruits:
    print(fruit)

# %% [markdown]
# #### Here we have another type of for loop, in which there are two variable names being kept track of. For simplicity sake, I have named them index and element so that you can see what each keeps track of in a particular loop. When using the enumerate, the first variable name keeps track of the index as you can see below, and the second keeps track of the value at that index, or that particular element.

# %%
for index,element in enumerate(fruits):
    print(str(index) + ": " + element)

# %% [markdown]
# #### One last way we can use a for loop is by setting a range. Note that the first argument is inclusive, and the second is exclusive

# %%
for num in range(0,5):
    print(num)

# %% [markdown]
# ### Part 7.2: Boolean Logic/If Statements

# %% [markdown]
# #### Here are a variety of boolean operations/statements. They are generally good to have in your back pocket in case you might need to use them.

# %%
className = "ITCS 3190"

# %%
className == "ITCS 3190"

# %%
className == "ITCS 3155"

# %%
className != "ITCS 3190"

# %%
className != "ITCS 3155"

# %%
"ITCS" not in className

# %%
"ITCS" in className

# %%
"3155" not in className and "ITCS" in className

# %% [markdown]
# #### Now you'll see an if else statement, with the classic example of setting a system that returns your grade

# %%
grade = 91
if grade < 60:
    print('Fail')
elif grade >= 60 and grade < 70:
    print('D')
elif grade >= 70 and grade < 80:
    print('C')
elif grade >= 80 and grade < 90:
    print('B')
else:
    print('A')

# %% [markdown]
# ### Part 7.3: Functions

# %% [markdown]
# #### If you want to define a function in Python, you must first use the keyword def, followed by the function name, followed by a set of parentheses with the arguments inside. Below is an example of a function that returns the product of two numbers a and b minus c

# %%
def productMinus(a,b,c):
    return (a*b)-c
productMinus(16,2,8)

# %% [markdown]
# ### Part 7.4: Convert time to seconds

# %% [markdown]
# #### For the following activity, write the function that will convert time into seconds. You will use multiple functions from python to accomplish the conversion. You shall not use any libraries or inbuilt tools. Also do not try searching google as you may end up wasting time. Just raise your hand and ask for help :)

# %%
# Input is a type of String in the format --> 2:10:33 
# 2 is the hour mark, 10 is the minute mark and 33 seconds --> timeToSeconds("2:10:33") should return 7866
def timeToSeconds(time):
    timeInSeconds = 0
    return timeInSeconds

# %% [markdown]
# ### Part 7.5: Find largest difference in a list

# %% [markdown]
# #### Given a list of Integer, return the difference between the largest and smallest integers in the list. Once again, raise your hand for any questions

# %%
# maxRange([10, 15, 20, 2, 10, 6]) ➞ 18
# maxRange([3, 6, -9, -4, -2, 15]) ➞ 24
def maxRange():
    x = [10, 15, 20, 2, 10, 6]
    y = min(x)
    z = max(x)

    difference = z-y
    return difference
print(maxRange())

    


