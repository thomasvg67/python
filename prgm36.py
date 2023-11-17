class Time:
    def __init__(self,hour,minute,second):
        self.h = hour
        self.m = minute
        self.s = second
    def __add__(self,x):
        sum1 = self.h + x.h
        sum2 = self.m + x.m
        sum3 = self.s + x.s
        if sum3 >= 60:
            sum3 = sum3 - 60
            sum2 = sum2 + 1
        if sum2 >= 60:
            sum2 = sum2 - 60
            sum1 = sum1 + 1
        print(sum1,":",sum2,":",sum3)
print("TIME 1")
h1 = int(input("Enter the hour in time1: "))
m1 = int(input("Enter the minute in time1: "))
s1 = int(input("Enter the second in time1: "))
obj1 = Time(h1,m1,s1)
print("TIME 2")
h2 = int(input("Enter the hour in time2:"))
m2 = int(input("Enter the minute in time2: "))
s2 = int(input("Enter the second in time2: "))
obj2 = Time(h2,m2,s2)
print("The sum of both time are:")
obj1 + obj2