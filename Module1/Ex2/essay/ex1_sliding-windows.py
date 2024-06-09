def max_sliding_window(arr: list, k: int) -> list:
    res = []
    for i in range(len(arr) - k + 1):
        res.append(max(arr[i:i + k]))

    return res


if __name__ == "__main__":
    arr = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    max_windows = max_sliding_window(arr, k)
    print(max_windows)
