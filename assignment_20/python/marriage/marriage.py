from random import shuffle as sh

girls = [ "g1", "g2", "g3", "g4", "g5"]
boys = [ "b1", "b2", "b3", "b4", "b5"]

sh(girls)
sh(boys)

result = zip(girls, boys)
print(tuple(result))