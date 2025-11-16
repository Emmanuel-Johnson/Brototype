# ✅ Method 1: Dictionary comprehension (recommended)

data = {"apple": 1, "banana": 2, "orange": 3, "grape": 4, "umbrella": 5, "kiwi": 6}

result = {k: v for k, v in data.items() if k[0].lower() not in "aeiou"}

print(result)



# ✅ Method 2: Using a for loop

data = {"apple": 1, "banana": 2, "orange": 3, "grape": 4, "umbrella": 5, "kiwi": 6}

for key in list(data.keys()):
    if key[0].lower() in "aeiou":
        del data[key]

print(data)



# ✅ Method 3: Functional style using filter()

data = {"apple": 1, "banana": 2, "orange": 3, "grape": 4, "umbrella": 5, "kiwi": 6}

result = dict(filter(lambda item: item[0][0].lower() not in "aeiou", data.items()))

print(result)
