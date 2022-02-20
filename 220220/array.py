# 열 우선 순회 ( N * M 행렬 )
N = 10
M = 10
arr = []

for r in range(N):
    for c in range(M):
        arr[r][c]

# 지그재그 순회
for r in range(N):  # row 길이
    for c in range(M):  # col 길이
        arr[r][c + (M - 1 - 2 * c) * (r % 2)] # r 이 짝수일 때 오른쪽에서 왼쪽으로

# 델타를 이용한 2차 배열 탐색
# 달팽이 쉨

dr = [0, 1, 0, -1]  # 우 하 좌 상
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    house = [[0] * num for _ in range(num)]
    r = c = 0
    d = 0  # direction
    for snail in range(1, num ** 2 + 1):
        house[r][c] = snail
        r += dr[d]
        c += dc[d]
        if r >= num or c >= num or house[r][c] != 0:
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
    print(f"#{tc}")
    for i in house:
        print(*i)
