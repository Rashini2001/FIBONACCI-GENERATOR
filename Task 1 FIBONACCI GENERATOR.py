from functools import lru_cache


@lru_cache(maxsize=None)  # caches computations for future computations
def fibonacci(n: int) -> int:
    """
    Calculate the Fibonacci number for the given index.

    Parameters:
    - n (int): The index of the Fibonacci number to calculate.

    Returns:
    - int: The Fibonacci number at the given index.

    Notes:
    - The Fibonacci sequence starts with 0 and 1. Each subsequent number is the sum of the two preceding numbers.
    - The Fibonacci numbers for indices 0 and 1 are 0 and 1, respectively.
    - The function uses memoization to cache previous computations for efficiency.
    """
    if n <= 1:  # fibonacci(0) = 0, and fibonacci(1) = 1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main(_input):
    try:  # try used in the case that the input isn't an int
        nterms = int(_input)
        if nterms < 0:  # conditional checking if input is negative
            print("Invalid input! Enter a positive Integer")
        else:
            print("Fibonacci sequence:")  # printing fibonacci sequence
            [print(fibonacci(n)) for n in range(nterms + 1)]  # iterating in the number of given input

    except ValueError:  # only possible ValueError is in int parsing func
        print("Invalid input! Enter an Integer")


if __name__ == "__main__":
    main(input("How many terms? "))
