#Inbuilt functions/standard library functions

y=min(23,56,1000,5679)
print(y)

x=max(4756,567,56,23355)
print(x)

z=pow(5,3)
print(z)

#User defined functions
def school():
    print("eMobilis")
school() #This is calling a function

def multiply():
    num1=5
    num2=6
    print(num1*num2)
multiply()

#Parameters and arguments
def add(a,b):
    print(a+b)
add(2,3)

def employee(Fullname,age,salary,phoneno,position):
    print(Fullname,age,salary,phoneno,position)
employee("Fiona Nkatha",45,500000,789756437,"Managing director")
employee("Ian Mutwiri",20,45000,759214779,"Admin")
employee("Florence Gathiga",33,340000,789756437,"Managing director")
employee("Evans Mawira",25,60000,789756437,"security")
