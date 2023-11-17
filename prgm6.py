a=[12,34,56]
b=[54,78,23]
print("list 1 : ",a)
print("list 2 : ",b)
print("length of first list : ",len(a))
print("length of second list : ",len(b))
if len(a) == len(b):
    print("Length of lists are same")
else:
    print("Length of lists are not same")

print("Sum of list 1 : ",sum(a))
print("Sum of list 2 : ",sum(b))
if sum(a) == sum(b):
    print("Sum of two lists are same")
else:
    print("Sum of two lists are not same")

check=any(item in a for item in b)
print("Any value occur in both : ",check)