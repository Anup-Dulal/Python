
# def fact(a):
#     f = 1
#     for i in range(1,a+1):
#         f = f*i
#     return f
#
#
# x = int(input("Enter the number for factorial: "))
#
# result = fact(x)
# print(result)

#Factorial using recurrsion


def fact(n):

    if(n == 0):
        return 1

    return n * fact(n-1)


result = fact(5)

print(result)