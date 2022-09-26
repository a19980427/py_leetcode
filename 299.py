class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        maps = {}
        length = len(secret)
        bull_mask = [False] * length
        A = 0
        B = 0
        for i in range(length):
            key = secret[i]
            if key in maps:
                maps[key].append(i)
            else:
                maps[key] = [i]

        # bulls
        for i in range(length):
            guess_ch = guess[i]
            if guess_ch in maps and i in maps[guess_ch]:
                A += 1
                maps[guess_ch].remove(i)
                bull_mask[i] = True

        # cows
        for i in range(length):
            guess_ch = guess[i]
            if not bull_mask[i] and guess_ch in maps and maps[guess_ch]:
                B += 1
                maps[guess_ch].pop()
        return format(f"{A}A{B}B")


class Solution2:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        cnt_secret = [0] * 10
        cnt_guess = [0] * 10

        for i in range(len(secret)):
            guess_ch = guess[i]
            secret_ch = secret[i]
            # bulls
            if guess_ch == secret_ch:
                A += 1
            # cows
            else:
                cnt_secret[ord(secret_ch) - ord('0')] += 1
                cnt_guess[ord(guess_ch) - ord('0')] += 1
        for s, g in zip(cnt_secret, cnt_guess):
            B += min(s, g)
        return f"{A}A{B}B"


a = Solution()
res = a.getHint("11", "11")
print(res)
