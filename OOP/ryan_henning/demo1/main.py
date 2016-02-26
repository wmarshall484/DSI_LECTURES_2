from fraction import Fraction

x = Fraction(5, 9)
print x

y = Fraction(3, 4)
print y

print x + y   # <-- prints "47/36"; WE NEED TO IMPLEMENT Fraction.__add__()
