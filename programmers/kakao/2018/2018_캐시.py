from collections import deque


def solution(cacheSize, cities):
    answer = 0
    q = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        print(city)
        print(q)
        if city in q:
            answer += 1
            q.remove(city)  # LRU를 만족시키기 위한 코드
            q.append(city)  # LRU를 만족시키기 위한 코드
        else:
            answer += 5
            if len(q) == cacheSize:
                q.popleft()
                q.append(city)
            else:
                q.append(city)

    return answer


cacheSize = 5
citis = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
         "Rome"]
answer = solution(cacheSize, citis)
print("answer:", answer)
