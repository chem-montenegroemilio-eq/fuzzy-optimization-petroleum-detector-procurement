from scipy.optimize import linprog
A_ub = [[ 20, 5, 10, 2],
[-10, -20, -20, -15] ]
b_ub = [ 200 , -80 ]
A_eq = [ [1, 1, 1, 1] ]
b_eq = [20]
c = [ 3000, 20000, 30000, 10000 ]
results = linprog(c, A_ub=A_ub, A_eq=A_eq,
    b_eq=b_eq, b_ub=b_ub,
    integrality=[1, 1, 1, 1],
    method="Highs")
print(results)