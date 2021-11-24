def numbers(n: int) -> None:
    if n < 0:
        return
    print(n)
    return numbers(n - 1)


numbers(21)
numbers(-4)
numbers(0)
