def happy(pers):
    print("testing " + pers )



def sumP(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)


def f(x):
    return x*x





def main():
    happy('gholi')
    sumP(7, 8)

#main()

def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('Benjamin', 'Franklin'))
print(lastFirst('Andrew', 'Harrington'))


print(f(3))
print(f(3) + f(4))

print(f(3))

print(9)

print(4 + 4)