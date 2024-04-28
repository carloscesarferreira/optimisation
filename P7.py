from pulp import *

sites = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']

district1 = {'S1':0, 'S2':1, 'S3':0, 'S4':1, 'S5':0, 'S6':0, 'S7':1}
district2 = {'S1':1, 'S2':0, 'S3':0, 'S4':0, 'S5':0, 'S6':1, 'S7':1}
district3 = {'S1':0, 'S2':1, 'S3':0, 'S4':0, 'S5':0, 'S6':1, 'S7':1}
district4 = {'S1':0, 'S2':1, 'S3':1, 'S4':0, 'S5':1, 'S6':1, 'S7':0}
district5 = {'S1':1, 'S2':0, 'S3':1, 'S4':0, 'S5':1, 'S6':0, 'S7':0}
district6 = {'S1':1, 'S2':0, 'S3':0, 'S4':1, 'S5':0, 'S6':1, 'S7':0}
district7 = {'S1':1, 'S2':0, 'S3':0, 'S4':0, 'S5':0, 'S6':0, 'S7':1}
district8 = {'S1':0, 'S2':0, 'S3':1, 'S4':1, 'S5':1, 'S6':0, 'S7':0}
district9 = {'S1':1, 'S2':0, 'S3':0, 'S4':0, 'S5':1, 'S6':0, 'S7':0}

#Initialize Class

model = LpProblem("P7", LpMinimize)

#Define Decision Variables

x = LpVariable.dicts('Realize_', sites, cat = 'Binary')

#Define Objective Function

model += lpSum([x[i] for i in sites])

#Define Constraints

model += lpSum([district1[i]*x[i] for i in sites]) >= 1
model += lpSum([district2[i]*x[i] for i in sites]) >= 1
model += lpSum([district3[i]*x[i] for i in sites]) >= 1
model += lpSum([district4[i]*x[i] for i in sites]) >= 1
model += lpSum([district5[i]*x[i] for i in sites]) >= 1
model += lpSum([district6[i]*x[i] for i in sites]) >= 1
model += lpSum([district7[i]*x[i] for i in sites]) >= 1
model += lpSum([district8[i]*x[i] for i in sites]) >= 1
model += lpSum([district9[i]*x[i] for i in sites]) >= 1

model += x['S1'] + x['S3'] + x['S4'] >= 2
model += x['S5'] + x['S6'] + x['S7'] == 2
model += x['S3'] + x['S4'] <= 1
model += x['S2'] <= x['S7']

#Solve Model

model.solve()

for i in sites:
    print("{} status {}".format(i,x[i].varValue))
        


print("Min Sites Number =",value(model.objective))
print("Status:", LpStatus[model.status])



