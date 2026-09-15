from scipy.optimize import linprog
A_ub = [
[ 3000, 20000, 30000, 10000, 37777.77],
[ 20, 5, 10, 2, 250],
[ -10, -20, -20, -15, 50],
[ 0, 0, 0, 0, 1]
]
b_ub = [137777.77, 500, -50, 1]
A_eq = [[ 1, 1, 1, 1, 5 ]]
b_eq = [ 25 ]
c = [0, 0, 0, 0, -1]
results = linprog(c=c, A_ub=A_ub, b_ub=b_ub,
A_eq=A_eq, b_eq=b_eq,
method="Highs")
print(results)