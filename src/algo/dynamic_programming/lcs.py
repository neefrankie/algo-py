# Given a sequence X = {1, 2, ..., m}, how many subsequences in it.
# This is a problem of Set theory. For each position in X, you can remove it or keep it.
# That's two choices. Use Multiplication rule to get the total: 
# 2 x 2 x ... x 2_m = 2^m
# Then how should we show all the subsequences?
# All elements in X make up a complete binary tres.
# The left branch means keep an element, while the right branch means remove an element.
# Use depth first search to traverse the tree, and you get a subsequence every time reaching a leaf.

from typing import List


def find_all_subsequences(s: str):
    result: List[str] = []
    x = list(s)

    def dfs(i: int, current_subseq: List[str]):
        # Reaching leaf.
        if i == len(x):
            result.append("".join(current_subseq))
            return
        
        # left branch, include current element
        current_subseq.append(x[i])
        dfs(i + 1, current_subseq)

        # right branch, exclude current element
        current_subseq.pop()
        dfs(i + 1, current_subseq)

    dfs(0, [])
    return result


def lcs_length(x: str, y: str):
    m = len(x)
    n = len(y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    solution = [[""] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                solution[i][j] = "↖"
            elif dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                solution[i][j] = "↑"
            else:
                dp[i][j] = dp[i][j-1]
                solution[i][j] = "←"

    return dp, solution


def print_lcs(solution: List[List[str]], x: str, i: int, j: int):
    if i == 0 or j == 0:
        return
    
    if solution[i][j] == "↖":
        print_lcs(solution, x, i-1, j-1)
        print(x[i-1], end="")
    elif solution[i][j] == "↑":
        print_lcs(solution, x, i-1, j)
    else:
        print_lcs(solution, x, i, j-1)


if __name__ == "__main__":
    print(find_all_subsequences("hello"))

    x = "ABCBDAB"
    y = "BDCABA"

    dp, solution = lcs_length(x, y)
    print_lcs(solution, x, len(x), len(y))