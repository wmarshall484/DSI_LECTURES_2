a = list()
b = list()
a.append(4)
a.append("natalie")
b.append("tim")
a.append(3.14)
b.append((1, 2))
print a             # a = [4, "ryan", 3.14]
print a.pop()
print b             # a = ["bob", (1, 2)]
print b.pop()


my_dict = dict()
my_dict["name"] = "ryan"
my_dict["age"] = 63
print my_dict.get("name")
print my_dict.items()     # my_dict = {'name': 'ryan', 'age': 63}
