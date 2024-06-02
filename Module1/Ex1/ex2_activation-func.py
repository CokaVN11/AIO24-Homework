import numpy as np


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def elu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))


def main():
    x = input("Input x = ")
    if not is_number(x):
        print("x must be a number.")
        return

    activation_func = input("Input activation function (sigmoid, relu, elu): ")
    activation_func = activation_func.lower()
    result = None
    if activation_func == "sigmoid":
        result = sigmoid(float(x))
    elif activation_func == "relu":
        result = relu(float(x))
    elif activation_func == "elu":
        result = elu(float(x))
    else:
        print(f"{activation_func} is not supported")
        return

    if result is not None:
        print(f"{activation_func}: f({x}) = {result}")


if __name__ == "__main__":
    main()
