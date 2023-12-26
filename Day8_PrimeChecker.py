def fast_prime_checker(number):
    num = int(number)
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
        if is_prime == False:
            print(f"{num} is not a prime number. You can divide it by {i}.")
            break
    if is_prime == True:
        print(f"{num} is a prime number")

fast_prime_checker(637)

def detailed_prime_checker(number):
  num = int(number)
  divisors = []
  for i in range(1,num + 1):
    if num % i == 0:
      divisors.append(i)
  if len(divisors) == 2:
    print(f"{num} is a prime number. It's only divisible by {divisors}")
  elif len(divisors) >= 3:
    print(f"{num} is not a prime number. It's divisible by {divisors}")

detailed_prime_checker(8)

