# https://www.youtube.com/watch?v=MjW10t9ppok
# 진짜 설명 좋다

base = ['A', 'B', 'C']
arr = ['A', 'B', 'C']
total = len(arr)  # 전체 개수 혹은 길이
c2 = total  # 전체 중에서 몇개를 뽑을 것인지에 대해서


def perm(k):
    if k == c2:
        print(arr)
        return

    for i in range(k, total):
        swap(arr, k, i)
        perm(k + 1)
        # swap(arr, k, i)  # 다시 자리 원복한다


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


perm(0)
