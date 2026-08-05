from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

indices = list(range(n))

all_combinations = list(combinations(indices, k))

favorable = 0

for combo in all_combinations:
    if any(letters[i] == 'a' for i in combo):
        favorable += 1

print(favorable / len(all_combinations))
