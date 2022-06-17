#
# num = int(input("Enter the Number: "))
#
# if num>1:
#     for i in range(2,int(num/2)+1):
#         if num % i == 0:
#             print("Not prime")
#             break
#         else:
#             print(num,"is a prime number")
#             break
# else:
#     print(num," is not a prime number")

lower = 1
upper = 100

for i in range(lower,upper+1):
    if i>1:
        for j in range(2,(i//2)+1):
            if i % j == 0:
                break
        else:
            print(i)

