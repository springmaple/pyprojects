def bubble_sort(m):
    """a.k.a sinking sort, keeps carry larger value from left to right."""
    for i in reversed(range(len(m))):
        for j in range(i):
            k = j + 1
            l, r = m[j], m[k]
            if l > r:
                m[j], m[k] = r, l

    return m


def selection_sort(m):
    """From left to right, replace each element with element with larger index
    and smallest value."""
    for i in range(len(m)):
        min_pos = i  # assume i has the smallest value.
        for j in range(i + 1, len(m)):  # compare with the rest of elements.
            if m[min_pos] > m[j]:
                min_pos = j
        if min_pos != i:
            m[i], m[min_pos] = m[min_pos], m[i]

    return m


def insertion_sort(m):
    """Takes value from right-most, and keep move on to the left
    until the value is larger than its left neighbour."""
    for i, x in enumerate(m):
        for j in reversed(range(i)):
            y = m[j]
            if x < y:
                m[j], m[j + 1] = x, y
                continue
            break

    return m


def quick_sort(m):
    """Select a random number (pivot), then divide the array into 3
    arrays of [smaller than pivot], [equal to pivot], and [larger than pivot],
    and merge them again in quick_sort([small])-[equal]-quick_sort([large])
    order"""
    if len(m) <= 1:
        return m
    pivot = m[0]  # random pivot
    less, equal, more = [], [], []
    for x in m:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            more.append(x)
        else:
            equal.append(x)
    return quick_sort(less) + equal + quick_sort(more)


def tim_sort(m):
    ...


def bucket_sort(m):
    """
    bucketSort(arr[], n)
    1) Create n empty buckets (Or lists).
    2) Do following for every array element arr[i].
    .......a) Insert arr[i] into bucket[n*array[i]]
    3) Sort individual buckets using insertion sort.
    4) Concatenate all sorted buckets.
    """
    n = 4  # number of buckets to use
    buckets = [[] for _ in range(n)]
    for x in m:
        pos = (x // n) - 1
        if pos > n:
            pos = n - 1
        elif pos < 0:
            pos = 0
        buckets[pos].append(x)

    result = []
    for bucket in buckets:
        result += sorted(bucket)
    return result


def radix_sort(m):
    ...


def merge_sort(m):
    """Always breaks the array into arrays of not more than 2 elements, and
    sort all of them, then merge the arrays (sort each elements again when
    merging)."""
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

    return merged + l + r


print(merge_sort([2, 1, 4, 5, 3, 3, 10000, 34012, 1231512, 1123, -1223]))
