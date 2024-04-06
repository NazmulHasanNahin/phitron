from collections import Counter
def min_removal(nmbr):
    removal = 0
    frequency = Counter(nmbr)
    for num, freq in frequency.items():
        if freq > num:
            removal += freq - num
        elif freq < num:
            removal += freq
    return removal

N = int(input())
nmbr = list(map(int, input().split()))
result = min_removal(nmbr)
print(result)