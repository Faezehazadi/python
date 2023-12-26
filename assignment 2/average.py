sum=0
i=0
while 1<2:
    num = input("Enter the number and type •exit• to finish.:")
    if num=="exit":
        break
    i+=1
    sum+=float(num)
    avg=sum/i
        
print("Average=",avg)