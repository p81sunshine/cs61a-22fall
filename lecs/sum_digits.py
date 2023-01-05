def sum_digits(n):
    """ sum every single digit 
        <<< sun_digits(18117)
        <<< 18
    """
    if n == 0:
        return 0;
    else:
        return n % 10 + sum_digits(n // 10)


n = sum_digits(18117)
print(n)
