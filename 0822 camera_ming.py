def solution(routes):
    touched = [0 for i in range(len(routes))]
    camera = 0
    while min(touched) == 0:
        carpass = [0 for i in range(60000)]
        for x in range(len(routes)):
            if touched[x] == 1:
                continue
            for i in range(routes[x][0] + 30000, routes[x][1] + 30000):
                carpass[i] = carpass[i] + 1
        maxvalue = max(carpass)
        for i in range(len(carpass)):
            if carpass[i] == maxvalue:
                car = i - 30000
                camera = camera + 1
                break

        for i in range(len(routes)):
            if routes[i][0] <= car and routes[i][1] >= car:
                touched[i] = 1

    return camera

routes = [[-20, 15], [-14, 5], [-18, -13], [-5, -3]]
