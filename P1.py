from pulp import *

# Initialize Class
model = LpProblem("P1", LpMaximize)

# Define Decision Variables

LA = LpVariable('LA', lowBound=0, cat='Integer')
LB = LpVariable('LB', lowBound=0, cat='Integer')
LC = LpVariable('LC', lowBound=0, cat='Integer')

# Define Objective Function

model += 4*LA + 2*LB + 3*LC

# Define Constraints

model += 7*LA + 3*LB + 6*LC <= 150
model += 4*LA + 4*LB + 5*LC <= 200
model += LA <= 10
model += LB <= 15
model += LC <= 10
model += LA >= 0.25*(LA+LB+LC)
model += LB >= 0.25*(LA+LB+LC)
model += LC >= 0.25*(LA+LB+LC)

# Solve Model

model.solve()
print("Produce {} kg of Lotion A".format(LA.varValue))
print("Produce {} kg of Lotion B".format(LB.varValue))
print("Produce {} kg of Lotion C".format(LC.varValue))
