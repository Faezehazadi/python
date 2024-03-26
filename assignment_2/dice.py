import random

dice = random.randint(1, 6)
print("🎲", dice)
if dice == 6:
    print("You have a new chance:")
    x=random.randint(1,6)
    print("🎲", dice)