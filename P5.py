from pulp import *

# Initialize CBss
model = LpProblem("P5", LpMaximize)

# Define Decision Variables

xs = LpVariable('xs', lowBound=0, cat='Integer')
xm = LpVariable('xm', lowBound=0, cat='Integer')
xl = LpVariable('xl', lowBound=0, cat='Integer')

# Define Objective Function

model += 310*xl + 230*xm + 200*xs

# Define Constraints

model += xs + xm + xl <= 30
model += 5000*xl + 3800*xm + 2000*xs <= 112000
model += 5*xl + 4*xm + 3*xs <= 120

model += xl + xm >= xs
model += xs + xm >= 8*xl


# Solve Model

model.solve()
print("Buy {} Small Planes".format(xs.varValue))
print("Buy {} Medium Planes".format(xm.varValue))
print("Buy {} Large Planes".format(xl.varValue))
