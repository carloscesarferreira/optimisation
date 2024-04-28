from pulp import *

cut = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']

options = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']

# Initialize Class

model = LpProblem("6.1", LpMinimize)

# Define Decision Variables

xcut = LpVariable.dicts('Cut_', cut, cat = 'Binary')

xopt = LpVariable.dicts('Option_', options, cat='Integer')

# Define Objective Function

model += lpSum([xopt[j] for j in options])

# Define Constraints

model += xopt['x1'] + xopt['x2'] + 2*xopt['x3'] >= 30
model += xopt['x1'] + 3*xopt['x4'] + xopt['x5'] + 2*xopt['x6'] >= 60
model += 2*xopt['x2'] + 2*xopt['x5'] + xopt['x6'] + 4*xopt['x7'] >= 48

model += xopt['x1'] >= 15*xcut['C1']
model += xopt['x2'] >= 15*xcut['C2']
model += xopt['x3'] >= 15*xcut['C3']
model += xopt['x4'] >= 15*xcut['C4']
model += xopt['x5'] >= 15*xcut['C5']
model += xopt['x6'] >= 15*xcut['C6']
model += xopt['x7'] >= 15*xcut['C7']

model += xopt['x1'] <= 1500*xcut['C1']
model += xopt['x2'] <= 1500*xcut['C2']
model += xopt['x3'] <= 1500*xcut['C3']
model += xopt['x4'] <= 1500*xcut['C4']
model += xopt['x5'] <= 1500*xcut['C5']
model += xopt['x6'] <= 1500*xcut['C6']
model += xopt['x7'] <= 1500*xcut['C7']

# Solve Model

model.solve()

print("Use {} times combination 1".format(xopt['x1'].varValue))
print("Use {} times combination 2".format(xopt['x2'].varValue))
print("Use {} times combination 3".format(xopt['x3'].varValue))
print("Use {} times combination 4".format(xopt['x4'].varValue))
print("Use {} times combination 5".format(xopt['x5'].varValue))
print("Use {} times combination 6".format(xopt['x6'].varValue))
print("Use {} times combination 7".format(xopt['x7'].varValue))

for i in cut:
    print("{} status {}".format(i,xcut[i].varValue))        


print("Min Sites Number =",value(model.objective))
print("Status:", LpStatus[model.status])

