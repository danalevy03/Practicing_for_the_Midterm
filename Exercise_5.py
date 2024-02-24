# Write a function that takes an integer as parameter
# and returns a list of all the divisors of that number

def divisors_of_number(number):
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

print(divisors_of_number(900))
