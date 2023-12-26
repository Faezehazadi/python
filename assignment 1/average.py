name = input("enter your first and last name:")
a = float(input("Enter score1: "))
b = float(input("Enter score2: "))
c = float(input("Enter score3: "))

average = ((a+b+c)/3)

if average >= 17:
    print( "name:" , name , "," , "status:" , "Great")

elif average < 17 and average >= 12 :
    print( "name:" , name , "," , "status:" , "Normal")

elif average < 12 :
    print( "name:" , name , "," , "status:" , "Fail")