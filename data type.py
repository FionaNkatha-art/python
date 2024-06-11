# Datatype

number =78  #Int
num =45.09 #float
greeting="How are you doing" #str
isprograminginteresting= True #bool
devices =["laptop","computer","tablet","phone"] #LIST
browser =("opera","firefox","safari","chrome") #Tuple
contries ={"Kenya","Uganda","Tanzania"} #set
employee ={
    "firstname":"Jane",
    "Age": 29,
    "Nationality":"Kenyan",
    "email":"janedoe@gmail.com",
} #Dictionary

print(isprograminginteresting)
print(num)
print(contries)
print(employee["firstname"])

#Determining a data type
print(type(contries))
print(type(employee))

#Typecasting is the process of converting one datatype to another
print(int(num))
print(float(number))
