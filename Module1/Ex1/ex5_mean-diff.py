import numpy as np


def md_nre_single_sample(y, y_hat, n, p):
    squared_y = np.power(y, 1 / n)
    squared_y_hat = np.power(y_hat, 1 / n)
    diff = squared_y - squared_y_hat
    return np.power(diff, p)


def main():
    print("Mean difference with y=100, y_hat=99.5, n=2, p=1: ",
          md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))
    print("Mean difference with y=50, y_hat=49.5, n=2, p=1: ",
          md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1))
    print("Mean difference with y=20, y_hat=19.5, n=2, p=1: ",
          md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1))
    print("Mean difference with y=0.6, y_hat=0.1, n=2, p=1: ",
          md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1))


if __name__ == "__main__":
    main()
