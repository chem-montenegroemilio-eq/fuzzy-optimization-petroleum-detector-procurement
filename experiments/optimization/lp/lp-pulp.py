from pulp import * 

c = LpProblem('Problema1', LpMinimize)
x = LpVariable.dicts('x', [1, 2, 3, 4], lowBound = 0, cat = 'Continuous')

c += 3000*x[1] + 20000*x[2] + 30000*x[3] + 10000*x[4]  
c += x[1] + x[2] + x[3] + x[4] == 20
c += 20*x[1] + 5*x[2] + 10*x[3] + 2*x[4] <= 200
c += -10*x[1] - 20*x[2] - 20*x[3] - 15*x[4] <= -80

status = c.solve()
print(LpStatus[status])

f_objetivo = 0
print(c.objective.items())
for var, coef in c.objective.items():
    print(f'{var.name} = {var.varValue}')
    f_objetivo += coef * var.varValue

print('\nf.objetivo(x*)=',f_objetivo)