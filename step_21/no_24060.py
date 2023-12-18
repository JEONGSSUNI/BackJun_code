def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr

    mid = (len(arr) + 1) // 2
    low_arr = merge_sort(arr[:mid])
    hight_arr = merge_sort(arr[mid:])

    sorted_arr = []

    l = h = 0

    while l < len(low_arr) and h < len(hight_arr) :
        if low_arr[l] <= hight_arr[h] :
            sorted_arr.append(low_arr[l])
            ans.append(low_arr[l])
            l += 1
        else :
            sorted_arr.append(hight_arr[h])
            ans.append(hight_arr[h])
            h += 1

    while l < len(low_arr) :
        sorted_arr.append(low_arr[l])
        ans.append(low_arr[l])
        l += 1

    while h < len(hight_arr) :
        sorted_arr.append(hight_arr[h])
        ans.append(hight_arr[h])
        h += 1

    return sorted_arr

ans = []
n, k = map(int, input().split())
merge_sort(list(map(int, input().split())))
if k > len(ans) :
    print(-1)
else :
    print(ans[k-1])