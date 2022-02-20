# bubble sort

lst1 = [3, 1, 6, 7, 4, 3, 2, 9, 2, 1]
N = len(lst1)
for i in range(N - 1, 0, -1):
    for j in range(0, i):
        if lst1[j] > lst1[j + 1]:
            lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
print(lst1)

# counting sort

lst2 = [4, 2, 5, 1, 7, 3, 6, 3, 9, 1]  # 0~9사이
count = [0] * 10
for i in lst2:
    count[i] += 1

for j in range(10):
    for _ in range(count[j]):
        print(j, end=' ')


