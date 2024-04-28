from pulp import *

# Initialize CBss
model = LpProblem("P3", LpMaximize)

# Define Decision Variables

x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')

# Define Objective Function

model += 6*(9*x1+5*x2)+9*(7*x1+9*x2)

# Define Constraints

model += 5*x1+3*x2 <= 1500
model += 7*x1+9*x2 <= 1900
model += 2*x1+2*x2 <= 1000

model += 9*x1+5*x2 >= 500
model += 7*x1+9*x2 >= 300


# Solve Model

model.solve()
print("Produce {} cycles in the Old Unit".format(x1.varValue))
print("Produce {} cycles in the New Unit".format(x2.varValue))
