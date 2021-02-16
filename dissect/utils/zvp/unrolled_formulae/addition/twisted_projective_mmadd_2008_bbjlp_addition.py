from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'd', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, d, X1, X2, Y1, Y2 = pr.gens()
k, d2 = 2 * d, 2 * d
Z1, Z2 = 1, 1
formula = {}
C = X1 * X2
formula['C'] = C
D = Y1 * Y2
formula['D'] = D
t0 = C * D
formula['t0'] = t0
E = d * t0
formula['E'] = E
t1 = X1 + Y1
formula['t1'] = t1
t2 = X2 + Y2
formula['t2'] = t2
t3 = t1 * t2
formula['t3'] = t3
t4 = 1 - E
formula['t4'] = t4
t5 = t3 - C
formula['t5'] = t5
t6 = t5 - D
formula['t6'] = t6
X3 = t4 * t6
formula['X3'] = X3
t7 = a * C
formula['t7'] = t7
t8 = 1 + E
formula['t8'] = t8
t9 = D - t7
formula['t9'] = t9
Y3 = t8 * t9
formula['Y3'] = Y3
t10 = E ** 2
formula['t10'] = t10
Z3 = 1 - t10
formula['Z3'] = Z3