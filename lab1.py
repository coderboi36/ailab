tot=int(input('Enter no. of bananas at starting '))
dist=int(input('Enter distance you want to cover '))
cap=int(input('Enter max load capacity of your camel '))
lose=0
start=tot
for i in range(dist):
    while start>0:
        start=start-cap
        if start==1:
            lose=lose-1
        lose=lose+2
    lose=lose-1
    start=tot-lose
    if start==0:
        break
print(start)