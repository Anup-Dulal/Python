
a = 5
b = 2

try:
    print("Resource Open")
    print(a/b)
    k= int(input("Enter the number: "))
    print(k)
except ZeroDivisionError as e:
    print("You cannot divide number by zero",e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print(e)
finally:
    print("Resource closed")

print("Bye")



