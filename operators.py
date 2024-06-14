#Arithmetic operators - simple calculations

num1=56
num2=8

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1 % num2) #Modulus returns the remainder after division

#Comparison operators -compares values
print(num1<num2)
print(num1>num2)
print(num1<=num2)
print(num1>=num2)
print(num1==num2) #Equal to
print(num1!=num2) #Not equal to

#Assignment operators -They are used to assign values to variables
a = 200
print(a)

a+=20
print(a)

#Logic operators -and,or,not
x=100
print(x<250 and x>1000) #Prints out a true if all the conditions are true
print(x<250 or x>1000) #Prints out a true if any of the conditions are true
print(not(x<250 or x>1000)) #Reverses

#Operator precedence -Order in which operations get executed
output =(100-4*3/1)
print(int(output))

#Write a simple python program that returns the area of a trapezium
# A=0.5(a+b)*h
a=20
b=40
h=4
sum=a+b
print(sum)
area=0.5*sum*h
print(area)



