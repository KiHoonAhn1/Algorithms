T = int(input())
for tc in range(1, T+1):
    bus_station = [0] * 5001
    N = int(input())
    for n in range(1, N+1):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus_station[i] += 1
    station = []
    P = int(input())
    for _ in range(P):
        C = int(input())
        station.append(str(bus_station[C]))
    result = ' '.join(station)
    print(f'#{tc} {result}')
