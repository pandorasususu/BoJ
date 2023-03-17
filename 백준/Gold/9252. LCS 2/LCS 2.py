import sys
input = sys.stdin.readline

first_word, second_word = input(), input()
fw_len, sw_len = len(first_word), len(second_word)

def sol():
    dp = [[0] * (sw_len + 1) for _ in range(fw_len + 1)]
    for i in range(1, fw_len + 1):
        for j in range(1, sw_len + 1):
            if first_word[i - 1] == second_word[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    ans = ''
    i, j = fw_len, sw_len
    while i > 0 and j > 0:
        if first_word[i - 1] == second_word[j - 1]:
            ans = first_word[i - 1] + ans
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print(dp[fw_len - 1][sw_len - 1])
    print(ans)
sol()