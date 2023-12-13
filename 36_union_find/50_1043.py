import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
truth_line = list(map(int, input().split()))
truth_cnt = truth_line[0]
truth_people = truth_line[1:]

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i
print(parent)

check_party_people = []
for _ in range(m):
    party_line = list(map(int, input().split()))
    party_cnt = party_line[0]
    party_people = party_line[1:]
    check_party_people.append(party_people)
    print(party_cnt, party_people)

    if len(party_people) >= 2:
        for i in range(len(party_people) - 1):
            print(i, i + 1)
            union_parent(parent, party_people[i], party_people[i + 1])

    print("parent", parent)
print("truth", truth_cnt, truth_people)

for i in range(len(truth_people)):
    print(truth_people[i])
    truth_people[i] = find_parent(parent, truth_people[i])

can_lie_people = []
for i in range(1, len(parent)):
    print(find_parent(parent, i))
    if find_parent(parent, i) not in truth_people:
        print("in")
        can_lie_people.append(i)
print("can_lie_poeple", can_lie_people)

print(check_party_people)

count = 0
for party in check_party_people:
    can_lie = any(clp in party for clp in can_lie_people)
    if can_lie:
        count += 1
print(count)
