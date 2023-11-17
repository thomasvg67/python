print("To find area of Rectangle")
l=int(input("Length:"))
b=int(input("Breadth:"))
c=lambda x,y: x*y
print("Area of Rectangle="+str(c(l,b)))
print("To find area of Square")
s=int(input("Side of Square"))
c=lambda x:x*x
print("Area of square="+str(c(s)))
print("To find area of Triangle")
l=int(input("Base"))
b=int(input("Height"))
c=lambda x,y:.5*x*y
print("Area of Triangle="+str(c(l,b)))