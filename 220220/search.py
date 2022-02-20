# 순차 검색
# 장점 : sorted가 안 되어 있을 때 쓸 수 있다.
# 단점 : 시간이 오래 걸린다.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
target = 8


for i in range(len(lst)):
    if lst[i] == target:
        print(i)
        break
else:
    print(f'{target}을 찾을 수 없습니다.')

# binary search

def binary_search(l, start, end, key):
    if start > end:
        return False
    else:
        mid = int((start + end) // 2)
        if l[mid] == key:
            return mid
        if key > l[mid]:
            return binary_search(l, mid, end, key)
        if key < l[mid]:
            return binary_search(l, start, mid, key)


s = 0
e = len(lst) - 1
target_count = binary_search(lst, s, e, target)
print(target_count)

# selection search
lst2 = [3, 4, 56, 2, 6, 1, 5, 8, 9, 32]


def selection(l2, k):
    for i in range(0, k):
        minindex = i
        for j in range(i + 1, len(l2)):
            if l2[minindex] > l2[j]:
                minindex = j
        l2[i], l2[minindex] = l2[minindex], l2[i]
    return l2[k - 1]


print(selection(lst, 4))
