
# for i in range(4):
#     for j in range(4):
#         print("#", end="")
#
#     print()

for i in range(4):
    for j in range(4-i):
        print("*",end="")

    print()

for i in range(4):
    for j in range(1+i,5):
        print(j,end="")
    print()
