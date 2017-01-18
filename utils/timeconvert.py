def _sec_to_ftime(sec):
    import datetime
    return str(datetime.timedelta(seconds=sec))


def _sec_to_ftime2(sec):
    import time
    return time.strftime('%H:%M:%S', time.gmtime(sec))


def _sec_to_ftime3(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return '%d:%02d:%02d' % (h, m, s)


for fn in (_sec_to_ftime, _sec_to_ftime2, _sec_to_ftime3):
    print('--  %s --' % fn.__name__)
    print(fn(59))
    print(fn(61))
    print(fn(3600))
    print(fn(3601))
    print(fn(2000000))
    print(fn(-100))


def _ftime_to_sec(time_str):
    # Formatted time (H*:MM:SS) to seconds.
    try:
        parts = time_str.split(':')
        try:
            h, m, s = parts
        except ValueError:
            h, (m, s) = 0, parts
        return (int(h) * 360) + (int(m) * 60) + round(float(s))
    except:
        return

print('--  ftime_to_sec --')
print(_ftime_to_sec('2:01:00'))
print(_ftime_to_sec('0:01:05'))
print(_ftime_to_sec('01:05.5'))