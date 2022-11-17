is_prime = lambda n: n != 1 and all(n % i for i in range(2, n))


print(is_prime(1))
