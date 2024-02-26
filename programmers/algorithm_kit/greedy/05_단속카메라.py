def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001
    print(routes)

    for route in routes:
        print(route)
        if camera < route[0]:
            print("camera")
            answer += 1
            camera = route[1]
    print(answer)

    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
solution(routes)
