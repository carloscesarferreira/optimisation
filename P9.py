from pulp import *

arcs = ['AB', 'AC', 'BD', 'CB', 'CD', 'CE', 'DC', 'DE', 'DF', 'EF']
length = {'AB':15, 'AC':9, 'BD':2, 'CB':4, 'CD':3, 'CE':16, 'DC':3, 'DE':6, 'DF':21, 'EF':7}

#Initialize Class

model = LpProblem("P9", LpMinimize)

#Define Decision Variables

x = LpVariable.dicts('Use_', arcs, cat = 'Binary')

#Define Objective Function

model += lpSum([length[i]*x[i] for i in arcs])


#Define Constraints

model += x['AB'] + x['CB'] == x['BD']
model += x['AC'] + x['DC'] == x['CB'] + x['CD'] + x['CE']
model += x['BD'] + x['CD'] == x['DE'] + x['DF']
model += x['CE'] + x['DE'] == x['EF']

#One path must leave node A

model += x['AB'] + x['AC'] == 1

#One path must reach node F

model += x['DF'] + x['EF'] == 1


#Solve Model

model.solve()
for i in arcs: print("{} status {}".format(i,x[i].varValue))

print("Min Path A-F =",value(model.objective))
print("Status:", LpStatus[model.status])
