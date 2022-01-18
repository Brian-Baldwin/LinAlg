def gram():
    v1 = float(input("Enter 1st component: "))
    v2 = float(input("Enter 2nd component: "))
    v3 = float(input("Enter 3rd component: "))
    u1 = float(input("Enter 1st component: "))
    u2 = float(input("Enter 2nd component: "))
    u3 = float(input("Enter 3rd component: "))
    inner = v1 * u1 + v2 * u2 + v3 * u3
    print(v1 - inner * u1)
    print(v2 - inner * u2)
    print(v3 - inner * u3)


gram()
