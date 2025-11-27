def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
print(is_leap(20000))

n = int(input())

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

a = int(input())
b = int(input())

# Agar a toq bo'lsa, uni birga oshirib juft qilamiz
if a % 2 != 0:
    a += 1

evens = list(range(a, b + 1, 2))
print(evens)
