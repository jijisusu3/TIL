# for문으로 부분집합 생성하기(3개 짜리)

lst = [2, 4, 5, 7, 8]
N = len(lst)
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            print(lst[i], lst[j], lst[k])

# bit 연산자로 부분집합 생성하기 (모든 경우의 수)
for i in range(1 << N):
    temp = []
    for j in range(N):
        if i & (1 << j):
            temp.append(lst[j])
    print(temp)