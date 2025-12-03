def area_circle(r):
    s = 3.14159 * r**2
    return s
print(area_circle(10))

def area_square(a):
    return a ** 2
print(area_square(10))

def area_trapez(a, b,h):
    S_t = 0.5 * (a + b) *h
    return S_t
print(area_trapez(5, 10,5))
print("yes")