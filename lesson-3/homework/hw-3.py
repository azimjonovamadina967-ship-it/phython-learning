## Lists and Tuples
## 1. Create and Access List Elements
##Create a list containing five different fruits and print the third fruit.
my_list = ['pineapple','kiwi','orange','strawberry','lemon']
print (my_list [2] )
## 2. Concatenate Two Lists
##Create two lists of numbers and concatenate them into a single list.
mylist1 = [33,456,687]
mylist2 =[78,98,645]
result = mylist1 + mylist2
print (result)
 numbers = [146,345,789,563,678,100,980]
first = numbers[0]
middle = numbers[len(numbers)//2]   
last = numbers[-1]
new_list = [first, middle, last]
print(new_list)
## 4. Convert List to Tuple
##Create a list of your five favorite movies and convert it into a tuple.
favmovie = ['interstellar','harry potter','horror','taxi1','payment']
favmovies = tuple(favmovie)
print(favmovies)
## 5. Check Element in a List
##Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['Paris','America','Istanbul','Turkey']
if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")

## 6. Duplicate a List Without Using Loops
##Create a list of numbers and duplicate it without using loops.
nums = [345,567,428,333]
duplicats = nums * 2
print (duplicats)


## 7. Swap First and Last Elements of a List
##Given a list of numbers, swap the first and last elements.
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

## 8. Slice a Tuple
##Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
tnumbers = (1,2,3,4,5,6,7,8,9,10)
print (tnumbers [3:7])
## 9. Count Occurrences in a List
##Create a list of colors and count how many times "blue" appears in the list.
colours = ['blue','pink','orange','blue','blue','blue']
print (colours.count ('blue'))

## 10. Find the Index of an Element in a Tuple
##Given a tuple of animals, find the index of "lion".
tanimal = ('lion','dog','cat','cow')
print (tanimal.index('lion'))
## 11. Merge Two Tuples
##Create two tuples of numbers and merge them into a single tuple.
numbrs1 = (1,2,3,4,5)
numbrs2 = (6,7,8,9,10)
single = numbrs1 + numbrs2
print (single)
 
## 12. Find the Length of a List and Tuple
##Given a list and a tuple, find and print their lengths.
liis = [32,445,46.78]
tuupl = (213,34,23,22)
print(len(liis), len(tuupl))


## 13. Convert Tuple to List
##Create a tuple of five numbers and convert it into a list.
tuuple = (4,7,8,9,0)
tuuples = list(tuuple)
print (tuuples)
## 14. Find Maximum and Minimum in a Tuple
##Given a tuple of numbers, find and print the maximum and minimum values.
number = (23,56,75,64,332)
print (max(number))
print (min(number))

## 15. Reverse a Tuple
##Create a tuple of words and print it in reverse order.
word = ('car','machine','sql','handsoome')
print(word[::-1])
