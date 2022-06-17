pos = -1

def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            global pos
            pos = i
            return True
        i += 1
    return False

list = [8,3,2,5,1,9]

n = 9

if search(list,n):
    print("Found at: ", pos)
else:
    print("Not Found")
