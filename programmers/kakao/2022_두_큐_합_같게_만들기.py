from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    count = 0
    print(queue1, queue2)
    queue_sum = int((queue1_sum + queue2_sum) / 2)
    print(queue_sum)

    for q in queue1:
        if q > queue_sum:
            return -1

    for q in queue2:
        if q > queue_sum:
            return -1

    # 처음에 len(queue1)을 while 안에 적었었음 -> 오류: [1,1,1,1][1,1,7,1] queue의 len()이 계속 바뀜 - 처음에 지정해야함
    maximum = len(queue1) * 4

    while True:

        # 처음에 생각하지 못한 코드 계속해서 swap (queue1이 queue2되고, queue2가 queue1되고, 다시 이걸 반복하면 원상태)
        if count > maximum:
            return -1

        if queue1_sum == queue2_sum:
            break

        if queue1_sum > queue2_sum:
            pop = queue1.popleft()
            queue2.append(pop)
            queue1_sum -= pop
            queue2_sum += pop

        else:
            pop = queue2.popleft()
            queue1.append(pop)
            queue1_sum += pop
            queue2_sum -= pop

        count += 1
        print(count)
        print(queue1, queue2)

    return count


queue1 = [1, 1, 1, 1]
queue2 = [1, 1, 7, 1]
answer = solution(queue1, queue2)
print("answer:", answer)
