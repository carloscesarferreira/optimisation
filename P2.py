from pulp import *

# Initialize CBss
model = LpProblem("P2", LpMinimize)

# Define Decision Variables

B = LpVariable('B', lowBound=0, cat='Integer')
C = LpVariable('C', lowBound=0, cat='Integer')
P = LpVariable('P', lowBound=0, cat='Integer')

# Define Objective Function

model += 0.5*B + 0.6*C + 0.7*P

# Define Constraints

model += 75*B + 60*C + 85*P >= 78*(B+C+P)
model += 15*B + 20*C + 18*P >= 16*(B+C+P)
model += B <= 1500
model += C <= 1200
model += P <= 2000
model += B+C+P >= 4000

# Solve Model

model.solve()
print("Use {} kg of Brazilian Coffee".format(B.varValue))
print("Use {} kg of Colombian Coffee".format(C.varValue))
print("Use {} kg of Peruvian Coffee".format(P.varValue))
