def prime(n: int) -> bool:
    if n == 0:
        return False
    if prime(n - 1) != 0 and n % prime(n - 1) == 0:
        return False
    else:
        return True


print(prime(33))
