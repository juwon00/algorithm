s = input()
t = input()

while len(t) > len(s):
    print(t, t[-1])

    if t[-1] == 'A':
        t = t[:len(t) - 1]

    elif t[-1] == 'B':
        t = t[:len(t) - 1]
        t = t[::-1]

print(s, t)

if s == t:
    print(1)
else:
    print(0)
