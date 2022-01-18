import math
def norm():
    v1 = float(input("Enter 1st component: "))
    v2 = float(input("Enter 2nd component: "))
    v3 = float(input("Enter 3rd component: "))
    normal = math.sqrt(v1**2+v2**2+v3**2)
    norm1 = v1/normal
    norm2 = v2/normal
    norm3 = v3/normal
    print(norm1)
    print(norm2)
    print(norm3)

norm()