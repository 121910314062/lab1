#LCM of two numbers

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
if (x > y):
    greater = x
else:
    greater = y

while(True):
    if((greater % x ==0) and (greater % y ==0)):
        lcm = greater
        break
    greater +=1

print("The LCM is", lcm)
