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
    for i, x in enumerate(m):
        for j in reversed(range(i)):
            y = m[j]
            if x < y:
                m[j], m[j + 1] = x, y
                continue
            break

    return m


def bubble_sort(m):
    """a.k.a sinking sort"""
    for i in reversed(range(len(m))):
        for j in range(i):
            k = j + 1
            l, r = m[j], m[k]
            if l > r:
                m[j], m[k] = l, r

    return m

if __name__ == '__main__':
    test = [2, 4, 5, 3, 2, 4, 5, 1, 220, 123, 12, 125, 124, 12423, 2.2, 3.4, 2]
    res = sorted(test)
    assert merge_sort(test) == res
    assert insertion_sort(test) == res
    assert bubble_sort(test) == res