name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - birth_year

# Natijani chiqaramiz
print(f"Hello {name}, you are {age} years old.")
## 2. Extract Car Names
txt = 'LMaasleitbtui'
cars = ["Malibu", "Mazda", "BMW", "Audi", "Tesla"]

txt_low = txt.lower()

for car in cars:
    if car.lower() in txt_low:
        print(car)
## 3. Extract Car Names
txt = 'MsaatmiazD'
cars = ["Malibu", "Mazda", "BMW", "Audi", "Tesla"]

txt_low = txt.lower()

for car in cars:
    if car.lower() in txt_low:
        print(car)
## 4. Extract Residence Area
txt = "I'am John. I am from London"

parts = txt.split("from")
area = parts[1].strip()

print(area)   # London

## 6. Count Vowels
string = input('enter string')
vowels = "aeiouAEIOU"
found_vowels = [char for char in string if char in vowels]
print("Vowels found:", found_vowels)
## 7. Find Maximum Value
numbers = input('enter list of numbers')
max_value = max(numbers)
print(max_value)
## 8. Check Palindrome
s = input('enter a word')
if s == s[::-1]:
    print("Yes")
else:
    print("No")
print("Domain:", domain)

## 10. Generate Random Password
import random
import string

# Parol uzunligini belgilaymiz
length = int(input("Enter password length: "))

# Belgilar to'plami
letters = string.ascii_letters      # a-z, A-Z
digits = string.digits              # 0-9
specials = string.punctuation       # !@#$%^&*() va h.k.

all_chars = letters + digits + specials

# Tasodifiy parol yaratish
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Your random password is:", password)
