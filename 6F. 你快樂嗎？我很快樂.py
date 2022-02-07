num=input()
while len(num)!=1:
    tot=0
    for i in num:
        tot+=int(i)**2
    num=str(tot)
if int(num)==1:
    print("Happy")
else:
    print("Unhappy")