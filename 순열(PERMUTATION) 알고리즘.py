# https://www.youtube.com/watch?v=MjW10t9ppok
# 진짜 설명 좋다

# 순열 공식
# n!


def perm(d):
    if d == k:
        print(arr)
        return

    for i in range(d, n):
        swap(arr, d, i)
        perm(d + 1)
        swap(arr, d, i)  # 다시 자리 원복한다 (필수임)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


if __name__ == '__main__':
    arr = ['A', 'B', 'C', 'D']
    n = len(arr)  # 전체 개수 혹은 길이
    k = n  # 전체 중에서 몇개를 뽑을 것인지에 대해서.  여기서는 4개로 4개의 결과 추출이라 이렇다

    # 만약 출력결과가 4개 중에 3개 구하기 같은거면 if k == c2 일때에 print문 위치에 조치
    r = []

    perm(0)
