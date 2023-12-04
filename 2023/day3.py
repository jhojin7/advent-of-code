import collections
lines = []
while 1:
    try:
        lines.append(input().strip())
    except:
        break


for i in range(len(lines)):
    lines[i] = list(lines[i].strip())
# print(lines)


def check(x, y):
    dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1)]
    N, M = len(lines), len(lines[0])
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        c = lines[nx][ny]
        if c not in list("1234567890.".strip()):
            # if c not in ['.']:
            return True
    return False


# # part 1
# nums = []
# n = []
# for i in range(len(lines)):
#     for j in range(len(lines[0])):
#         # print(i, j, check(i, j))
#         if lines[i][j] in "1234567890":
#             n.append((i, j, lines[i][j]))
#         else:
#             if n:
#                 nums.append(n)
#             n = []

# # print(*nums, sep='\n')
# ans = 0
# for n in nums:
#     flag = False
#     x = ""
#     for i, j, c in n:
#         # print(i, j, c, check(i, j))
#         x += c
#         flag = flag or check(i, j)
#     # print(int(x), flag)
#     if flag:
#         ans += int(x)

# print(ans)

# part 2

def get_num(n):
    x = ""
    for i, j, c in n:
        x += c
    return int(x)


gears = []
nums = []
n = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        # print(i, j, check(i, j))
        if lines[i][j] == '*':
            gears.append((i, j, lines[i][j]))
        if lines[i][j] in "1234567890":
            n.append((i, j, lines[i][j]))
        else:
            if n:
                nums.append(n)
            n = []

new_gears = collections.defaultdict(list)
for gear in gears:
    a, b, c = gear
    for num in nums:
        for x, y, _ in num:
            if abs(x-a) == 1 and abs(y-b) == 1:
                # if num not in new_gears[a, b]:
                new_gears[a, b].append(num)
            else:
                continue


ans = 0
for k, v in new_gears.items():
    # if len(v) != 2:
    #     continue

    # print([get_num(n) for n in v])
    if len(v) == 2:
        tmp = 1
        for n in v:
            tmp *= get_num(n)
        ans += tmp
print(ans)
