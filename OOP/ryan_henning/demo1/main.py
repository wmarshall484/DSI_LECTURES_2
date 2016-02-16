from fraction import Fraction

a = Fraction(2, 4)   # <-- the fraction 2/4
print a              # <-- should print "1/2"
print -a             # <-- should print "-1/2"

x = Fraction(5, 9)
print x

y = Fraction(3, 4)
print y

print x + y   # <-- prints "47/36"
print x - y   # <-- prints "-7/36"

print x == Fraction(10, 18)  # True
print x == y  # False
print x < y   # True
print x > y   # False
