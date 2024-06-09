def trace_back(dp, source, target):
    i, j = len(source), len(target)
    while i > 0 and j > 0:
        if source[i - 1] == target[j - 1]:
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j - 1] + 1:
                print(f"Replace {source[i - 1]} with {target[j - 1]}")
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + 1:
                print(f"Delete {source[i - 1]}")
                i -= 1
            else:
                print(f"Insert {target[j - 1]}")
                j -= 1


def calc_levenshtein_distance(source: str, target: str) -> int:
    dp = [[0] * (len(target) + 1) for _ in range(len(source) + 1)]

    for i in range(len(source) + 1):
        dp[i][0] = i
    for j in range(len(target) + 1):
        dp[0][j] = j

    def calculate_dp(i, j):
        if source[i - 1] == target[j - 1]:
            return dp[i - 1][j - 1]
        else:
            return min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            dp[i][j] = calculate_dp(i, j)

    trace_back(dp, source, target)

    print("Levenshtein distance:", dp[len(source)][len(target)])


if __name__ == "__main__":
    calc_levenshtein_distance("kitten", "fishing")
