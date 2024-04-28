from pulp import *

# Initialize CBss
model = LpProblem("P4", LpMinimize)

# Define Decision Variables

x11 = LpVariable('x11', lowBound=0, cat='Integer')
x12 = LpVariable('x12', lowBound=0, cat='Integer')
x13 = LpVariable('x13', lowBound=0, cat='Integer')
x21 = LpVariable('x21', lowBound=0, cat='Integer')
x22 = LpVariable('x22', lowBound=0, cat='Integer')
x31 = LpVariable('x31', lowBound=0, cat='Integer')


# Define Objective Function

model += 28*(x11 + x21 + x31) + 40*(x12 + x22) + 50*(x13)

# Define Constraints

model += x11 + x12 + x13 >= 1500
model += x12+x13+x21 + x22 >= 500
model += x13+x22+x31 >= 5000

# Solve Model

model.solve()
print("Rent {} m2 in month 1 for 1 month".format(x11.varValue))
print("Rent {} m2 in month 1 for 2 months".format(x12.varValue))
print("Rent {} m2 in month 1 for 3 months".format(x13.varValue))
print("Rent {} m2 in month 2 for 1 month".format(x21.varValue))
print("Rent {} m2 in month 2 for 2 months".format(x22.varValue))
print("Rent {} m2 in month 3 for 1 month".format(x31.varValue))

