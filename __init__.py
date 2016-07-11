def merge_sort(m):
    mlen = len(m)
    # Base case. A list of zero or one elements is sorted, by definition.
    if mlen <= 1:
        return m

    # Recursive case. First, divide the list into equal-sized sublists
    # consisting of the even and odd-indexed elements.
    mhalf = mlen // 2
    left = m[:mhalf]
    right = m[mhalf:]

    # Recursively sort both sublists.
    left = merge_sort(left)
    right = merge_sort(right)

    # === Func: merge(left, right)
    # Then merge the now-sorted sublists.
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # Either left or right may have elements left; consume them.
    # (Only one of the following loops will actually be entered.)
    result += left
    result += right
    return result


def insertion_sort(m):
    for i, x in enumerate(m):
        for j in reversed(range(i)):
            y = m[j]
            if y > x:
                m[j], m[j + 1] = x, y
                continue
            break

    return m


if __name__ == '__main__':
    test = [2, 4, 5, 3, 2, 4, 5, 1, 220, 123, 12, 125, 124, 12423, 2.2, 3.4, 1123]
    res = sorted(test)
    assert merge_sort(test) == res
    assert insertion_sort(test) == res
