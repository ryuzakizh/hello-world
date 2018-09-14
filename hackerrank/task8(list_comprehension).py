x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    li = []
    for ix in range(x+1):
        for iy in range(y+1):
            for iz in range(z+1):
                if ix+iy+iz!=n:
                    li.append([ix,iy,iz])
    print(li)
