def karatsuba(x, y):
    if x < 10 or x < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * (10 ** (2 * m)) + ad_bc * (10 ** m) + bd

if __name__=="__main__":
    test_cases = [
        (1234, 5678),
        (123, 456),
        (99999, 9999),
        (12345678910, 2345678)
    ]

    for x, y in test_cases:
        result = karatsuba(x, y)
        expected = x * y
        print(f"{x} * {y} = {result}")
        print(f"验证：{result == expected}")
