h,m = input().split()
cook = input()
h = int(h)
m = int(m)
cook = int(cook)

ch = int(cook / 60)
cm = cook % 60


h = h + ch
m = m + cm



if m >= 60:
    m = m - 60
    h = h + 1

if h >= 24:
    h = h - 24

print(h,m)
