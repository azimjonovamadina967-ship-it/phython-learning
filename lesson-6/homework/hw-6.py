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
number = 10
sum = 0
for i in range(1, number + 1):
    sum += i
print(sum)





