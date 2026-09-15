from pulp import LpProblem, LpMaximize, LpVariable, LpStatus
c = LpProblem('Problema1', LpMaximize)
x = LpVariable.dicts('x', [1, 2, 3, 4], lowBound = 0, cat = 'Integer')
alpha = LpVariable.dicts('alpha', [5], lowBound = 0, upBound = 1, cat = 'Continuous')
c += 0*x[1] + 0*x[2] + 0*x[3] + 0*x[4] + 1*alpha[5]
c += 3000*x[1] + 20000*x[2] + 30000*x[3] + 10000*x[4] + 37777.77*alpha[5] <= 137777.77
c += x[1] + x[2] + x[3] + x[4] + 5*alpha[5] == 25
c += 20*x[1] + 5*x[2] + 10*x[3] + 2*x[4] + 250*alpha[5] <= 500
c += -10*x[1] - 20*x[2] - 20*x[3] - 15*x[4] + 50*alpha[5] <= -50
status = c.solve()
resultado_alpha = c.objective
print(resultado_alpha)
f_objetivo = 0
for var, coef in c.objective.items():
    f_objetivo += coef * var.varValue
print(f'\nf.objetivo(x*)= alpha= {f_objetivo}')
lista_x = []
for i, var in x.items():
    if 'x' in str(var):
        lista_x.append(var.varValue)
print(f'vetor x= {lista_x}')