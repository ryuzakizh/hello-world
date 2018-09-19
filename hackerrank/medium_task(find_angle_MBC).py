import math
AB = int(input())
BC = int(input())
degr = round(math.degrees(math.atan2(AB,BC)))
print(str(degr)+"°")
