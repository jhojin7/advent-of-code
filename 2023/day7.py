import collections
lines = []
while 1:
    try:
        lines.append(input().strip())
    except:
        break

# Part1
labels = "23456789TJQKA"


def convert(s):
    arr = ['%02d' % (labels.index(a)) for a in s.strip()]
    return '-'.join(map(str, arr))


hands = []
for line in lines:
    a, b = line.split()
    kind = ""
    # cnt = list(collections.Counter(a).items())
    # cnt.sort(key=lambda x: (-x[1], x[0]))
    cnt = collections.Counter(a)
    vals = sorted(cnt.values(), reverse=True)
    if vals == [5]:
        kind = 1
    elif vals == [4, 1]:
        kind = 2
    elif vals == [3, 2]:
        kind = 3
    elif vals == [3, 1, 1]:
        kind = 4
    elif vals == [2, 2, 1]:
        kind = 5
    elif vals == [2, 1, 1, 1]:
        kind = 6
    else:
        kind = 7

    hands.append((kind, int(b), convert(a)))
# hands.sort(key=lambda x: (-x[0], -x[1], x[2]))
hands.sort(key=lambda x: (-x[0], x[2]))
# print(hands)


ans = 0
for i, x in enumerate(hands, 1):
    ans += i*x[1]
print(ans)
# 236632936
# 251545216

# Part2
labels = "J23456789TJQKA"


def convert(s):
    arr = ['%02d' % (labels.index(a)) for a in s.strip()]
    arr = []
    cnter = collections.Counter(s.strip())
    for a in s.strip():
        if labels.index(a) == 0:
            mostcommon = cnter.most_common(1)[0]
            arr.append('%02d' % (mostcommon[1]))
        else:
            arr.append('%02d' % (labels.index(a)))
    return '-'.join(map(str, arr)), cnter
