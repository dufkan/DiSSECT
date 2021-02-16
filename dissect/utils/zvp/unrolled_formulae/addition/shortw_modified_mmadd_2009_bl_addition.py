from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
ZZ1, ZZZ1, ZZ2, ZZZ2 = 1, 1, 1, 1
b2 = 2 * b
b4 = 4 * b
half = 1 / 2
Z1, Z2 = 1, 1
formula = {}
H = X2 - X1
formula['H'] = H
HH = H ** 2
formula['HH'] = HH
HHHH = HH ** 2
formula['HHHH'] = HHHH
Z3 = 2 * H
formula['Z3'] = Z3
ZZ3 = 4 * HH
formula['ZZ3'] = ZZ3
t0 = H + HH
formula['t0'] = t0
t1 = t0 ** 2
formula['t1'] = t1
t2 = t1 - HH
formula['t2'] = t2
t3 = t2 - HHHH
formula['t3'] = t3
J = 2 * t3
formula['J'] = J
t4 = Y2 - Y1
formula['t4'] = t4
r = 2 * t4
formula['r'] = r
V = X1 * ZZ3
formula['V'] = V
t5 = r ** 2
formula['t5'] = t5
t6 = 2 * V
formula['t6'] = t6
t7 = t5 - J
formula['t7'] = t7
X3 = t7 - t6
formula['X3'] = X3
t8 = V - X3
formula['t8'] = t8
t9 = Y1 * J
formula['t9'] = t9
t10 = 2 * t9
formula['t10'] = t10
t11 = r * t8
formula['t11'] = t11
Y3 = t11 - t10
formula['Y3'] = Y3
t12 = a * HHHH
formula['t12'] = t12
T3 = 16 * t12
formula['T3'] = T3