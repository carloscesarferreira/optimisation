from pulp import *

arcs = ['AB', 'AC', 'BC', 'BD', 'CD']

#Initialize Class

model = LpProblem("P8", LpMaximize)

#Define Decision Variables

Flow = LpVariable.dicts('Flow_', arcs, cat = 'Integer')

#Define Objective Function

model += Flow['AB']+Flow['AC']

#Define Constraints

model += Flow['AB'] == Flow['BC']+Flow['BD']
model += Flow['AC'] + Flow['BC'] == Flow['CD']

model += Flow['AB'] <= 9
model += Flow['AC'] <= 8
model += Flow['BC'] <= 3
model += Flow['BD'] <= 7
model += Flow['CD'] <= 9


#Solve Model
model.solve()

print("Max Flow =",value(model.objective))
print("Status:", LpStatus[model.status])
