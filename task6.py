i, N = input(), set(map(int, input().split()))
i, M = input(), set(map(int, input().split()))
print(*sorted(N.difference(M)), sep='\n')
print(*sorted(M.difference(N)), sep='\n')
