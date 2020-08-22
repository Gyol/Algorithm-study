routes = [[-20, 15], [-14, 5], [-18, -13], [-5, -3]]
# print(len(routes))

carpass = [0 for i in range(60)]
camera = 0

while len(routes) != 0:
    carpass = [0 for i in range(60)]
    for x in routes:
        for i in range(x[0]+30, x[1]+31):
            carpass[i] = carpass[i]+1
    # print(carpass)

    print()
    for i in range(len(carpass)):
        if carpass[i] == max(carpass):
            # print(i)
            car = i-30
            print(car)
            camera = camera+1
            break

    for x in reversed(routes):
        print(x[0])
        if x[0] <= car and x[1] >= car:
            routes.remove(x)

    # print(routes)

print(camera)
