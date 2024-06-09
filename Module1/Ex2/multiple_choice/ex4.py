def levenshtein_distance(token1: str, token2: str) -> int:
    dp = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    for i in range(len(token1) + 1):
        dp[i][0] = i
    for j in range(len(token2) + 1):
        dp[0][j] = j

    def calculate_dp(i, j):
        if token1[i - 1] == token2[j - 1]:
            return dp[i - 1][j - 1]
        else:
            return min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            dp[i][j] = calculate_dp(i, j)

    return dp[len(token1)][len(token2)]


if __name__ == "__main__":
    assert levenshtein_distance("hi", "hello") == 4.0
    print(levenshtein_distance("hola", "hello"))
