def is_inside(a, b):
    if a[0] < b[0] or a[1] < b[1]:
        return False
    elif a[0] > b[0] and a[1] > b[1]:
        return True

check = is_inside([200, 120], [140, 60, 100, 200])
