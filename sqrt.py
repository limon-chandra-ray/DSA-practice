def sqrt(num):
    if num == 1:
        return 1
    left = 0
    rigth = num//2

    while rigth-left > 1:
        mid = (rigth+left)//2
        if mid*mid > num:
            rigth = mid -1
        else:
            left = mid
    if left == rigth:
        return left
    else:
        if rigth*rigth > num:
            return left
        else:
            return rigth

num = 15


x = sqrt(num)
print(x)