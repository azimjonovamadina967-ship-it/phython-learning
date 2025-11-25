### 1. Sort a Dictionary by Value
sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}
sorted_dict = {key: value for key, value in sorted(sample_dict.items(), key=lambda item: item[1])}
print(sorted_dict)
### 2. Add a Key to a Dictionary
mydict ={10:1,20:2}
mydict [30] = 3
mydict
### 3. Concatenate Multiple Dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)
print(result)
### 4. Generate a Dictionary with Squares
n = 5
result = {x: x*x for x in range(1, n+1)}
print(result)
### 5. Dictionary of Squares (1 to 15)

result = {x: x*x for x in range(1, 15+1)}
print(result)
### 1. Create a Set
myset = {"apple", "banana", "cherry"}
print(myset)
### 2. Iterate Over a Set
myset = {10, 20, 30, 40}

for item in myset:
    print(item)
### 3. Add Member(s) to a Set
myset = {1, 2, 3}
myset.update([4, 5, 6])
print(myset)
### 4. Remove Item(s) from a Set
myset = {1, 2, 3, 4}
myset.remove(3)
print(myset)
### 5. Remove an Item if Present in the Set
myset = {1, 2, 3, 4, 5}

item = 3

myset.discard(item)

print(myset)
