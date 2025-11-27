def is_leap(year):
    # Input validation must be at the top
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    # Leap year rules
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True

    return False  # default case


# Test cases
print(is_leap(2000))   # True
print(is_leap(1900))   # False
print(is_leap(20000))  # False

n = int(input())

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

a = int(input("a = "))
b = int(input("b = "))

# if-else bilan birinchi juft sonni topamiz
if a % 2 != 0:
    a += 1

evens = list(range(a, b + 1, 2))

print("Even numbers:", *evens)
a = int(input("a = "))
b = int(input("b = "))

start = a + (a % 2)   # NO if-else

evens = list(range(start, b + 1, 2))

print("Even numbers:", *evens)
