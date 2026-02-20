from fractions import Fraction

#I made this not knowing the slope unit was done lol.

print("Python Slope Calculator")
print()
print("By Benjamin Milaazo")
print()
X1 = float(input("Enter X of first set:  "))
Y1 = float(input("Enter Y of first set:  "))
X2 = float(input("Enter X of second set:  "))
Y2 = float(input("Enter Y of second set:  "))

X = X2 - X1
Y = Y2 - Y1

if Y == 0:
    print("Slope: Undefined")
else:
    simplified = Fraction(Y/X).limit_denominator()
    decimal = Y/X
    print(f"Slope = {decimal} or {simplified}")