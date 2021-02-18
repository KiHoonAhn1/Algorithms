x, y, w, h = map(int, input().split())
if w - x <= h - y:
    if w - x >= y or w - x >= x:
        if x <= y:
            print(x)
        else:
            print(y)
    elif w - x <= x:
        print(w - x)
    else:
        print(x)
elif w - x > h - y:
    if h - y >= x or h - y >= y:
        if x <= y:
            print(x)
        else:
            print(y)    
    elif h - y <= y:
        print(h - y)
    else:
        print(y)
