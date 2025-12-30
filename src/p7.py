def sqrt(x):
    if x == 0 or x == 1:
        return x

    left = 0
    right = x

    while left <= right:
        mid = (left + right)
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

print(sqrt(36))
