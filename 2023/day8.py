import collections
import sys


def input_as_str(fname="input.txt"):
    """
    sys.stdin = input_as_str()
    """
    import io
    import os
    fname = os.path.join(os.path.abspath(os.curdir), fname)
    with open(fname, 'r') as f:
        return io.StringIO(f.read())


def input_by_file(fname) -> list[str]:
    with open(fname, 'r') as f:
        return f.readlines()


def part1():
    sys.stdin = input_as_str("src/input.txt")
    rl = input()
    input()
    graph = collections.defaultdict(list)
    while 1:
        try:
            a, b = input().split(" = ")
            b, c = b.split(", ")
            b = b[1:]
            c = c[:-1]
            # nodes.append([a, b, c])
            graph[a] = [b, c]
        except:
            break
    # print(graph)

    cur = nxt = "AAA"
    i = 0
    while cur != "ZZZ":
        dir = rl[i % len(rl)]
        # print(dir, cur, nxt)
        cur = nxt
        i += 1
        if dir == 'L':
            nxt = graph[cur][0]
            continue
        else:
            nxt = graph[cur][1]
            continue
    print(i-1)


def part2():
    sys.stdin = input_as_str("src/input.txt")
    rl = input()
    input()
    graph = collections.defaultdict(list)
    while 1:
        try:
            a, b = input().split(" = ")
            b, c = b.split(", ")
            b = b[1:]
            c = c[:-1]
            graph[a] = [b, c]
        except:
            break

    ghost = [k for k in graph.keys() if k[-1] == 'A']
    cnts = [0 for _ in range(len(ghost))]
    print(ghost)
    i = 0
    while 1:
        for idx in range(len(ghost)):
            cur = ghost[idx]
            if cur[-1] == 'Z':
                continue
            dir = rl[i % len(rl)]
            # print(cur, graph[cur], dir)
            if dir == 'L':
                ghost[idx] = graph[cur][0]
                cnts[idx] += 1
                continue
            else:
                ghost[idx] = graph[cur][1]
                cnts[idx] += 1
                continue
        chkz = [k for k in ghost if k[-1] == 'Z']
        # print(i, chkz, cnts)
        if len(chkz) == len(ghost):
            break
        i += 1
    print(ghost, cnts)
    import math
    print(math.lcm(*cnts))


# part1()
part2()  # 9319259
