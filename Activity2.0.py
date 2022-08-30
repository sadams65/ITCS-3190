

from os import remove
from re import X


def removeDuplicates(list): 
    x = []
    for element in list:
        if element not in x:
            x.append(element)
    return x

new_list = [1, 2, 2]
print(removeDuplicates(new_list))

