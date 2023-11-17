a=str(input("Enter a string : "))
fc=a[0]
a=a.replace(fc,'$')
a=fc+a[1:]
print("Replaced string : ",a)