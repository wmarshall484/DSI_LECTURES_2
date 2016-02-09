array1 = [1,2,3,2,1]

for number in array:
    if number == 2:
        print "It's a 2"
    else:
        print "It's not a 2"

array2 = [1,2,2,3,3,4,4]

for number in array2:
    if number == 3:
        print "It's a 3"
    else:
        print "It's not a 3"


array3 = [1,2,3,4,5,5,5]
for number in array3:
    if number == 5:
        print "It's a 5"
    else:
        print "It's not a 5"











def check_numbers(array, target):
    for number in array:
        if number == target:
            print "It's a {target}".format(target=target)
        else:
            print "It's not a {target}".format(target=target)
