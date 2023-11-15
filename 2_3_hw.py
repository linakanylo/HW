def fizz_buzz(n):

    result = []

for i in range (1, n+1):

    if i % 2 == 0 and i % 3 == 0:
        print "fizzbuzz"
    elif i % 2 == 0:
        print "fizz"
    elif i % 3 == 0:
        print "buzz"
    else:
        print i

    print result

n = 21

result = fizz_buzz (n)

print (" ". join(result))



