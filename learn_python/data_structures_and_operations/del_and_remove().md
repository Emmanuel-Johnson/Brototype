# del

del is a Python statement used to delete elements by index, delete slices, delete dictionary key–value pairs, or delete entire variables. It raises an IndexError when deleting a list element using an invalid index (del lst[10]), and a KeyError if you try to delete a dictionary key that doesn’t exist (del d["x"]). Slice deletion (del lst[5:20]) never raises an error even if the range is out of bounds, and deleting a non-existent variable raises a NameError. del also works on many objects by removing attributes or references, but it cannot delete items from immutable types like strings or tuples. Overall, del is used when you know the index, the key, or the variable/attribute you want to remove.

# remove()

remove() is a method used mainly on lists to delete the first occurrence of a given value.
It removes items by value (not by index) and raises a ValueError if the value is not present.
It cannot delete slices, cannot delete by index, and cannot delete the whole list — it simply searches the list and removes the first matching value. remove() also exists for sets, where it removes the specified value from the set, and raises a KeyError if the value is not found. Unlike lists, sets do not have duplicates or order, so it just removes that single element.