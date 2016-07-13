def merge_sort(m):
    mlen = len(m)
    if mlen <= 1:
        return m

    mhalf = mlen // 2
    left = merge_sort(m[:mhalf])
    right = merge_sort(m[mhalf:])

    merged = []

    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged += left + right
    return merged


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
                m[j], m[k] = r, l

    return m
