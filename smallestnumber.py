# To determine the smallest number among four numbers
first=input("Enter first number:")
second=input("Enter second number:")
third=input("Enter third number")
fourth=input("Enter fourth number:")

if first<second and first<third and first<fourth:
    print(first,"is the smallest number")
elif second<first and second<third and second<fourth:
    print(second,"is the smallest number")
elif third<first and third<second and third<fourth:
    print(third,"is the smallest number")
else:
    print(fourth,"is the smallest number")
