def solution(sizes):
    max_w = 0
    max_h = 0

    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
        max_w = max(max_w, sizes[i][0])
        max_h = max(max_h, sizes[i][1])
    print(max_w, max_h)
    return max_w * max_h


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
solution(sizes)
