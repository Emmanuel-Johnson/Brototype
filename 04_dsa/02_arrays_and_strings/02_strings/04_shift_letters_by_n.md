```python
def shift_letters_by_n(word, n):
    res = []
    for i in word:
        if i.isalpha():
            if i.islower():
                res.append(chr(97 + (ord(i) - 97 + n) % 26))
            else:
                res.append(chr(65 + (ord(i) - 65 + n) % 26))
        else:
            res.append(i)
    return "".join(res)
```
