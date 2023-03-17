import sys
input = sys.stdin.readline

first_word, second_word, third_word = input(), input(), input()
len_1, len_2, len_3 = len(first_word), len(second_word), len(third_word)

def sol():
    dp = [[[0] * (len_3 + 1) for j in range(len_2 + 1)] for i in range(len_1 + 1)]
    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            for k in range(1, len_3 + 1):
                if first_word[i - 1] == second_word[j - 1] and second_word[j - 1] == third_word[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    print(dp[len_1 - 1][len_2 - 1][len_3 - 1])
sol()