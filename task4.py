N, M = map(int, input().split())
a = "-"
b = ".|."
c = "WELCOME"
for i in range(1, N, 2):
    print((a * ((M - (i * 3)) // 2)) + (b * i) + (a * ((M - (i * 3)) // 2)))
print("-" * ((M - 7) // 2) + c + "-" * ((M - 7) // 2))
for i in range(N - 2, - 1, - 2):
    print((a * ((M - (i * 3)) // 2)) + (b * i) + (a * ((M - (i * 3)) // 2)))
