n = int(input().strip())
if n % 2 != 0:
    print("Weird")
else :
    if n in range(2,6):print("Not Weird")
    elif n in range(6,21):print("Weird")
    elif n > 20:print("Not Weird")
#print Weird if odd
#print Not Weird if even and < 6
#Weird if even and < 20
#Not Weird if even > 20