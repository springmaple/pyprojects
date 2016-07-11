def merge_sort(m):
    mlen = len(m)
    if mlen <= 1:
        return m

    mhalf = mlen // 2
    left = merge_sort(m[:mhalf])
    right = merge_sort(m[mhalf:])

    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left + right
    return result


def insertion_sort(m):
    for j, y in enumerate(m):
        for i in reversed(range(j)):
            x = m[i]
            if x > y:
                m[i + 1], m[i] = x, y
                continue
            break

    return m


if __name__ == '__main__':
    test = [2, 4, 5, 3, 2, 4, 5, 1, 220, 123, 12, 125, 124, 12423, 2.2, 3.4, 2]
    res = sorted(test)
    assert merge_sort(test) == res
    assert insertion_sort(test) == res
