n=int(input("Enter a number:"))
list=[i for i in range(1,n+1)if n%i==0]
print("Factors of number=",list)