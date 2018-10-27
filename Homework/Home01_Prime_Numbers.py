__author__ = 'stanislav-kuhtinski'
print("Hi, I will help you print all the prime numbers between 0 and your number.\n")
while True:
    number = input("Please choose an integer: ")
    if number.isdigit():
        break
    else:
        print("%s is not an integer, please try again" % number)
        continue

number = int(number)

for possiblePrime in range(2, number):
    # Assume number is prime until shown it is not.
    isPrime = True
    if possiblePrime > 1:
        for i in range(2, possiblePrime):
            if possiblePrime % i == 0:
                isPrime = False
    if isPrime:
        print(possiblePrime)
