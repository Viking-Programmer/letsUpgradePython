# Make a function prime numbers and use filter to filter out all the prime numbers from 1-2500

def find_prime(num):
    for i in range(2,num):
       if (num % i) == 0:
           return False
    return False


filtered_prime_nos = filter(find_prime, range(2, 2501))

for numbers in filtered_prime_nos:
    print(numbers)