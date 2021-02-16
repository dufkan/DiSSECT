from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
ZZ1, ZZZ1, ZZ2, ZZZ2 = 1, 1, 1, 1
b2 = 2 * b
b4 = 4 * b
half = 1 / 2
Z1, Z2 = 1, 1
formula = {}
t0 = Y2 * Z1
formula['t0'] = t0
u = t0 - Y1
formula['u'] = u
uu = u ** 2
formula['uu'] = uu
t1 = X2 * Z1
formula['t1'] = t1
v = t1 - X1
formula['v'] = v
vv = v ** 2
formula['vv'] = vv
vvv = v * vv
formula['vvv'] = vvv
R = vv * X1
formula['R'] = R
t2 = 2 * R
formula['t2'] = t2
t3 = uu * Z1
formula['t3'] = t3
t4 = t3 - vvv
formula['t4'] = t4
A = t4 - t2
formula['A'] = A
X3 = v * A
formula['X3'] = X3
t5 = R - A
formula['t5'] = t5
t6 = vvv * Y1
formula['t6'] = t6
t7 = u * t5
formula['t7'] = t7
Y3 = t7 - t6
formula['Y3'] = Y3
Z3 = vvv * Z1
formula['Z3'] = Z3