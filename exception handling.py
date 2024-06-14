try:
    x=5
    print(x)

except:
    print("An error occured")
finally:
    print("Success")

num1=67
num2=0
try:
    print(num1/num2)
except:
    print("Zero division error occured")
finally:
    print("success")