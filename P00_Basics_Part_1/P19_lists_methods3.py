#List Method
li = [1, 2, 5, 6, 7, 4, 56, 38, 0]
print(li.sort())
print(li)

print(li.reverse())
print(li)

print("Sorted function")
# its a function which sort the list, but it does not modify the list permanently.
print(sorted(li))
print(li)

new_li = li.copy()   # same as doing new_li = li[:]
print(new_li)
