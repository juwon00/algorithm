def make_uv(p):
    u, v = "", ""
    left, right = [], []
    for i in range(len(p)):
        if p[i] == "(":
            left.append(i)
        else:
            right.append(i)
        if len(left) == len(right):
            u = p[:i + 1]
            v = p[i + 1:]
            break
    return u, v


def check_u_correct(u):
    # print(u)
    stack = []
    for i in range(len(u)):
        if len(stack) == 0 and u[i] == ")":
            return False
        elif u[i] == "(":
            stack.append(u[i])

        elif u[i] == ")":
            stack.pop()
    return True


def solution(p):
    if len(p) == 0:
        return answer

    u, v = make_uv(p)

    print("u", u)
    print("v", v)
    print()

    if check_u_correct(u):
        return u + solution(v)
    else:
        print("u, v", u, v)
        print("last")
        tmp = "("
        tmp += solution(v)
        tmp += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        u = ''.join(u)
        u = tmp + u
        print(u)
        return u


p = "()))((()"
answer = solution(p)
print("answer:", answer)
