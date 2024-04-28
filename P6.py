from pulp import *

# Initialize CBss
model = LpProblem("P6", LpMinimize)

# Define Decision Variables

x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')
x3 = LpVariable('x3', lowBound=0, cat='Integer')
x4 = LpVariable('x4', lowBound=0, cat='Integer')
x5 = LpVariable('x5', lowBound=0, cat='Integer')
x6 = LpVariable('x6', lowBound=0, cat='Integer')
x7 = LpVariable('x7', lowBound=0, cat='Integer')

# Define Objective Function

model += x1+x2+x3+x4+x5+x6+x7

# Define Constraints

model += x1+x2+2*x3 >= 30
model += x1+3*x4+x5+2*x6 >= 60
model += 2*x2+2*x5+x6+4*x7 >= 48


# Solve Model

model.solve()
print("Use {} times combination 1".format(x1.varValue))
print("Use {} times combination 2".format(x2.varValue))
print("Use {} times combination 3".format(x3.varValue))
print("Use {} times combination 4".format(x4.varValue))
print("Use {} times combination 5".format(x5.varValue))
print("Use {} times combination 6".format(x6.varValue))
print("Use {} times combination 7".format(x7.varValue))

print("Min Cuts Number =",value(model.objective))
print("Status:", LpStatus[model.status])
