from collections import deque


def solution(n, k, cmd):
    answer = ['O'] * n
    pointer = k
    dic = dict()
    stack = deque()

    for i in range(n):
        dic[i] = [i - 1, i + 1]
    dic[0] = [None, 1]
    dic[n - 1] = [n - 2, None]
    print(dic)

    print()
    print("start:", k)
    print()
    for c in cmd:
        print(c)
        print("pointer:", pointer)

        if c[0] == 'U':
            p = int(c.split(" ")[1])
            for _ in range(p):
                pointer = dic[pointer][0]

        elif c[0] == 'D':
            p = int(c.split(" ")[1])
            for _ in range(p):
                pointer = dic[pointer][1]

        elif c[0] == 'C':
            answer[pointer] = "X"
            front, back = dic[pointer]
            stack.append([front, pointer, back])

            if back is None:
                pointer = dic[pointer][0]
            else:
                pointer = dic[pointer][1]

            if front is None:
                dic[back][0] = None
            elif back is None:
                dic[front][1] = None
            else:
                dic[front][1] = back
                dic[back][0] = front

        elif c[0] == 'Z':
            front, now, back = stack.pop()
            answer[now] = "O"

            if front is None:
                dic[back][0] = now
            elif back is None:
                dic[front][1] = now
            else:
                dic[front][1] = now
                dic[back][0] = now

        print(dic)
        print(stack)
        print("pointer:", pointer)
        print()

    return "".join(answer)


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
answer = solution(n, k, cmd)
print("answer:", answer)
