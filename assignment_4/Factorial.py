num=int(input("Enter  number: "))

if num>=0 and num<=2:
    print("true.")
elif num>2:
    n=1
    for i in range(1,num//2):
        if num%i==0:
            n*=i
            if n==num:
                print("true")
                break
        else:
            print("false")
            break


