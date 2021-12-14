n = int(input())
quat = [i * i for i in range(2, n + 1)]
for i in range(n - 1):
    for j in range(i, n - 1):
        if quat[i] + quat[j] in quat:
            print((i + 2, j + 2, quat.index(quat[i] + quat[j]) + 2))
