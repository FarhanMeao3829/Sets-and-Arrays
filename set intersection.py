setx = {"green","blue" }
sety = {"blue", "yellow"}

print("Original set elements:")
print(setx)
print(sety)
print()

print("\nIntersection of two said sets: ")
setz = setx.intersection(sety)
print(setz)

print("\nUnion of two said sets: ")
setv = setx.union(sety)
print(setv)

print("\nDifference of two said sets: ")
setk = setx.difference(sety)
print(setk)
