""" FACILITY LOCATION PROBLEM """

# Define general data from DC and facilities

Facility = ['DC', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10']
Latitude = {'DC':41.18186, 'F1':41.21560, 'F2':41.22437, 'F3':41.25228, 'F4':41.19442, 'F5':41.18651, 'F6':41.19157, 'F7':41.19836, 'F8':41.20246, 'F9':41.20301, 'F10':41.18928}
Longitude = {'DC':-8.66340, 'F1':-8.67583, 'F2':-8.69788, 'F3':-8.70513, 'F4':-8.69733, 'F5':-8.67994, 'F6':-8.65760, 'F7':-8.61148, 'F8':-8.63212, 'F9':-8.63988, 'F10':-8.68655}
Weights = {'DC':16783, 'F1':3026, 'F2':11506, 'F3':10448, 'F4':10453, 'F5':14262, 'F6':17608, 'F7':12493, 'F8':16449, 'F9':9682, 'F10':1}

""" FACILITY LOCATION PROBLEM - COG METHOD"""

#Calculate variables

# Sum of the weights
SM = sum(Weights[i] for i in Facility)

# Calculate the weighted Latitude and Longitude
WGT_LT = sum(Weights[i]*Latitude[i] for i in Facility)
WGT_LG = sum(Weights[i]*Longitude[i] for i in Facility)

# Calculate new DC coordinates
NEW_LT = WGT_LT/SM
NEW_LG = WGT_LG/SM

# Calculate the sum of the weighted distances

import math

WgDist = []
for i in Facility:
    WgDist.append(Weights[i]*math.sqrt((NEW_LT - Latitude[i])**2 +  (NEW_LG - Longitude[i])**2))

SumWgDist = sum(WgDist)

# Calculate the average distance of CoG

AvrgDist = SumWgDist / SM

# Print the results

print ("The New DC Coordinates are:")
print ("Latitute = ",round(NEW_LT,5))
print ("Longitude = ",round(NEW_LG,5))
print ("CoG Weighted Average Distance = ",round(AvrgDist,5))
