def bubble_sort(m):
    """a.k.a sinking sort"""
    for i in reversed(range(len(m))):
        for j in range(i):
            k = j + 1
            l, r = m[j], m[k]
            if l > r:
                m[j], m[k] = r, l

    return m


def selection_sort():
    ...


def insertion_sort(m):
    for i, x in enumerate(m):
        for j in reversed(range(i)):
            y = m[j]
            if x < y:
                m[j], m[j + 1] = x, y
                continue
            break

    return m


def quick_sort(m):
    ...


def bucket_sort(m):
    ...


def radix_sort(m):
    ...


def merge_sort(m):
    mlen = len(m)
    if mlen <= 2:
        try:
            x, y = m[0], m[1]
            if x > y:
                m[0], m[1] = y, x
        except IndexError:
            pass
        return m

    mhalf = mlen // 2
    l = merge_sort(m[:mhalf])
    r = merge_sort(m[mhalf:])

    merged = []
    while l and r:
        merged.append(l.pop(0) if l[0] <= r[0] else r.pop(0))

    merged += l + r
    return merged
