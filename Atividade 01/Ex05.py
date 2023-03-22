num = [1, 3, 5, 14, 8, 56, 77, 9]

par = [x for x in num if x %2 == 0]
print(par)

impar = [x for x in num if x %2 != 0]
print(impar)
