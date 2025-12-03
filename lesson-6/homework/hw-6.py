## 1. Modify String with Underscores
##Given a string `txt`, insert an underscore (`_`) after every third character. If a character is a vowel or already
#  has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.
txt = input("Enter text: ")
result = []
vowels = "aeiouAEIOU"

i = 0   
count = 0 
while i < len(txt):
    ch = txt[i]
    result.append(ch)
    count += 1

    if count == 3:
        if ch in vowels:
              count = 0 
        else:
            if i != len(txt) - 1:
                result.append("_")
            count = 0   # qaytadan 0 bo‘ladi

    i += 1

final = "".join(result)
print(final)

## 2. Integer Squares Exercise
n =(int(input('enter your number')))
for i in range(n):
    print(i**2)
### Exercise 1: Print first 10 natural numbers using a while loop
count = 1

while count<=10:
    print(count)
    count +=1
### Exercise 2: Print the following pattern
rows = 5
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

### Exercise 3: Calculate sum of all numbers from 1 to a given number
number =10
sum = 0
for i in range(1, number + 1):
    sum += i
print(sum)

### Exercise 4: Print multiplication table of a given number
num = 2
for i in range(1, 11):
    print(num * i)


### Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    if x > 500:
        break
    if x == 75:         
        print(x)
    elif x > 100 and x != 180:   # 100 dan katta va 180 ga teng bo‘lmasa
        print(x)


### Exercise 6: Count the total number of digits in a number
num = int(input('Enter numbers'))
print (len(str(num)))
### Exercise 7: Print reverse number pattern
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
### Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in reversed (list1):
 print(i)


### Exercise 9: Display numbers from -10 to -1 using a for loop
for i in range(-10,-0,1):
 print(i)
### Exercise 10: Display message “Done” after successful loop execution
for i in range(5):
    print(i)
else:
    print("Done")

### Exercise 11: Print all prime numbers within a range

for num in range(25, 51):  # 25 dan 50 gacha
    if num > 1:             # 1 dan katta sonlarni tekshiramiz
        for i in range(2, num):
            if num % i == 0:
                break       # bo‘linadigan son topildi → prime emas
        else:
            print(num)      # for loopni to‘liq tugatgan bo‘lsa → prime

### Exercise 12: Display Fibonacci series up to 10 terms
n = 10
a = 0
b = 1
next = b  
count = 1

while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()
### Exercise 13: Find the factorial of a given number
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 5


# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

## 14. Return Uncommon Elements of Lists
list1 = [1, 1, 2]
list2 = [2, 3, 4]
uncommon = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(uncommon)
