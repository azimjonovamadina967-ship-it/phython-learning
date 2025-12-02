def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(7))   # True
print(is_prime(12))  # False


def sum_digits(n):
    total = 0
    for digit in str(n):      # sonni stringga aylantiramiz
        total += int(digit)   # har bir raqamni qo‘shamiz
    return total

print(sum_digits(1234))   # 10
print(sum_digits(560))    # 11

def powers_of_two(N):
    k = 1
    while k <= N:
        print(k, end=" ")
        k *= 2   # har safar 2 barobar oshiramiz

# Test
powers_of_two(10)
