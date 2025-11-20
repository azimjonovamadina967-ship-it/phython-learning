
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
