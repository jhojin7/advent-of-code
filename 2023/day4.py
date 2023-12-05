lines = []
while 1:
    try:
        lines.append(input().strip())
    except:
        break


cards = [line.split(':')[1].split('|') for line in lines]
# points = []
# for card in cards:
#     win, has = card
#     win = list(map(int, win.split()))
#     has = list(map(int, has.split()))
#     # print(win, has)
#     point = 0
#     for h in has:
#         if h in win:
#             point = point*2 if point > 0 else 1
#     points.append(point)
# print(sum(points))

# part2
cardcnt = [1 for _ in range(len(cards))]
for i, card in enumerate(cards):
    win, has = card
    win = list(map(int, win.split()))
    has = list(map(int, has.split()))
    cnt = 0
    for h in has:
        if h in win:
            cnt += 1
    for j in range(i+1, min(i+1+cnt, len(cardcnt))):
        cardcnt[j] += cardcnt[i]
print(sum(cardcnt))
