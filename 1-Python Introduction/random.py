import random
array = []
random_number = 0
num = int(input("enter number of array :"))

while len(array) < num :
    random_number = random.randint(0 , 100)
    if random_number not in array :
        array.append(random_number)

print(array)
