# https://gorakgarak.tistory.com/523?category=265216

# 순서없이 그냥 뽑을 때의 경우의 수 : 조합
# 순서있게 뽑을 때의 경우의 수 : 순열

# 조합공식
# nCr = n-1Cr-1 + n-1Cr
#     = n(n-1) / 2

# 첫 방정식을 그대로 옮기면 아래와 같다
# def comb(n,r):
#     return comb(n-1,r-1) + comb(n-1,r)


# 상세하게 정의
# def comb(arr, n, r):
#     if r == 0 :
#         return
#
#     return comb(n - 1, r - 1) + comb(n - 1, r)

def comb(arr, index, n, r, target):
    if r == 0:
        print(arr,index)
    elif target == n :
        return
    else:
        arr[index] = target
        comb(arr,index+1,n,r-1,target+1)
        comb(arr,index,n,r,target+1)




if __name__== '__main__':
    arr = ['A','B','C']

    arr =[] 
    comb(arr,0,5,3,0)





