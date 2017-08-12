

t = [[0.0 for col in range(5)] for row in range(5)]
t0 = [[0.0 for col in range(5)] for row in range(5)]
dteps = 0.0001

for i in range(1, 5):
    t[i][0] = 100

for j in range(1, 4):
    t[0][j]=200

t[0][0] = (t[0][1] + t[1][0]) / 2

for k in range(0, 100):
    for i in range(1, 4):
        for j in range(1, 4):
            t[i][j] = (t[i-1][j] + t[i+1][j] + t[i][j-1] + t[i][j+1])/4

    t[0][4] = (t[0][3] + t[1][4])/2

    for i in range(1, 4):
        t[i][4] = (2*t[i][3] + t[i-1][4] + t[i+1][4])/4

    for j in range(1, 4):
        t[4][j]=(2*t[3][j] + t[4][j-1]+ t[4][j+1] + 200)/24

    t[4][4]=(t[4][3] + t[3][4] + 100)/12

    dtmax = 0.0

    for i in range(0, 5):
        for j in range(0, 5):
            d = abs(t[i][j] - t0[i][j])
            dtmax = max(d, dtmax)
    for i in range(0, 5):
        for j in range(0, 5):
            t0[i][j] = t[i][j]
    print(t)

    if dtmax < dteps:
        print(k)
        break



