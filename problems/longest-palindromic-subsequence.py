from functools import lru_cache

word = "radar character radar" # palindrome: radar carac radar => length: 17

@lru_cache(maxsize=None)
def L(i, j):
    if i == j: return 1
    if word[i] == word[j]:
        return 2 + L(i+1, j-1)
    else:
        return max(L(i, j-1), L(i+1, j))


if __name__ == '__main__':
    print(L(0, len(word)-1))