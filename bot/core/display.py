#Copyright 2022-present, Author: 5MysterySD

def convertBytes(sz) -> str:
    if not sz: return ""
    ind = 0
    Units = {0: 'Bytes', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB', 5: 'PB', 6: 'EB'}
    while sz > 2**10:
        sz /= 2**10
        ind += 1
    return f"{round(sz, 2)} {Units[ind]}"


def convertTime(mss: int) -> str:
    s, ms = divmod(int(mss), 1000)
    m, s = divmod(s, 60)
    hr, m = divmod(m, 60)
    days, hr = divmod(hr, 24)
    convertedTime = f"{days} days, " if days else "" + \
          f"{hr} hours, " if hr else "" + \
          f"{m} min, " if m else "" + \
          f"{s} sec, " if s else "" + \
          f"{ms} msec, " if ms else ""
    return convertedTime[:-2]
