def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            # 3.
            if not used[i] and (i == 0 or arr[i - 1] != arr[i] or used[i - 1]):   # 'AABC' 와 같이 중복된 값이 있을 경우
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)


permutation('ABCD',3)


