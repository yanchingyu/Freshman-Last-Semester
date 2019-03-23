def month():
    print("Sun\tMon\tTue\tWed\tThr\tFri\tSat")
    
def Date(a,b):
    for i in range(1,b):
        print(i,"\t",end='')
        if i%7==a:
            print("\n")
    print("\n")

a=int(input("Enter the year(2018): "))
while(a!=2018):
    a=int(input("ERROR! try again: "))
    
print("January")
month()
print("\t",end='')
Date(6,32)

print("Febrary")
month()
print("\t\t\t\t",end='')
Date(3,29)

print("March")
month()
print("\t\t\t\t",end='')
Date(3,32)

print("April")
month()
Date(0,31)

print("May")
month()
print("\t\t",end='')
Date(5,32)

print("June")
month()
print("\t\t\t\t\t",end='')
Date(2,31)

print("July")
month()
Date(0,32)

print("August")
month()
print("\t\t\t",end='')
Date(4,32)

print("September")
month()
print("\t\t\t\t\t\t",end='')
Date(1,31)

print("October")
month()
print("\t",end='')
Date(6,32)

print("November")
month()
print("\t\t\t\t",end='')
Date(3,31)

print("December")
month()
print("\t\t\t\t\t\t",end='')
Date(1,32)
    