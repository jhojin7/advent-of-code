import math
import collections
from tqdm import tqdm

lines = []
while 1:
    try:
        lines.append(input().strip())
    except:
        break

# times = list(map(int, lines[0].split()[1:]))
# dists = list(map(int, lines[1].split()[1:]))
# ans = 1
# for t, d in zip(times, dists):
#     m, M = 9999999999999, 0
#     for ti in range(t):
#         traveled = (t-ti)*(ti)
#         if d < traveled:
#             m, M = min(m, ti), max(M, ti)
#     ans *= M-m+1
# print(ans)

# part2
t = int(''.join(lines[0].split()[1:]))
d = int(''.join(lines[1].split()[1:]))
print(t, d)
m, M = 9*10**8, 0
for ti in tqdm(range(t)):
    traveled = (t-ti)*(ti)
    if d < traveled:
        m, M = min(m, ti), max(M, ti)
print(M-m+1)
