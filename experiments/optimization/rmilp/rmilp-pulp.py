from pulp import LpProblem, LpMinimize, LpVariable, LpStatus
c = LpProblem("Problema1", LpMinimize)
x = LpVariable.dicts("x", [1, 2, 3, 4], lowBound=0, cat="Integer")
y = LpVariable.dicts("y", [5], lowBound=0, upBound=1, cat="Continuous")
c += 3000*x[1] + 20000*x[2] + 30000*x[3] + 10000*x[4]
c += x[1] + x[2] + x[3] + x[4] + 5*y[5] == 25
c += 20*x[1] + 5*x[2] + 10*x[3] + 2*x[4] + 250*y[5] <= 500
c += -10*x[1] - 20*x[2] - 20*x[3] - 15*x[4] + 50*y[5] <= -50
status = c.solve()
resultado_x = c.objective
print(f'Resultado de y= {y[5].varValue}')
f_objetivo = 0
for var, coef in c.objective.items():
    f_objetivo += coef * var.varValue
print(f'\nf.objetivo(x*)= {f_objetivo}')
lista_x = []
for i, var in x.items():
    if 'x' in str(var):
        lista_x.append(var.varValue)
print(f'vetor x= {lista_x}')