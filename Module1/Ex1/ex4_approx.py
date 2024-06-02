import numpy


def approx_sin(x, n):
    result = 0
    factorial = 1
    for i in range(n):
        result += ((-1)**i) * (x**(2 * i + 1)) / factorial
        factorial *= (2 * i + 2) * (2 * i + 3)
    return result


def approx_cos(x, n):
    result = 0
    factorial = 1
    for i in range(n):
        result += ((-1)**i) * (x**(2 * i)) / factorial
        factorial *= (2 * i + 1) * (2 * i + 2)

    return result


def approx_sinh(x, n):
    result = 0
    factorial = 1
    for i in range(n):
        result += x**(2 * i + 1) / factorial
        factorial *= (2 * i + 2) * (2 * i + 3)
    return result


def approx_cosh(x, n):
    result = 0
    factorial = 1
    for i in range(n):
        result += x**(2 * i) / factorial
        factorial *= (2 * i + 1) * (2 * i + 2)
    return result


def main():
    print("Approximation of sin(3.14) with n=10: ", approx_sin(3.14, 10))
    print("Approximation of cos(3.14) with n=10: ", approx_cos(3.14, 10))
    print("Approximation of sinh(3.14) with n=10: ", approx_sinh(3.14, 10))
    print("Approximation of cosh(3.14) with n=10: ", approx_cosh(3.14, 10))


if __name__ == "__main__":
    main()
