from neuroCombat import neuroCombat
import pandas as pd
import numpy as np



blacklist = ["0","BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]
data = pd.read_csv("patients_data.csv", header = 0)

#print(data)

#header = header.remove(p for p in blacklist)
column = data["0"]
data = data.drop(columns = blacklist, axis =1)
header = list(data)

print(header)
print(column)
#print(data.iloc[:,0].head)

keys=[]
for i in data.index:
    try:
        val=float(data.iloc[:,0][i])

    except:
        keys.append(i)
        continue
print(keys)

# Getting example data
# 200 rows (features) and 10 columns (scans)
data = data.drop(keys, axis =0)
column = column.drop(keys)
print(column)

# Specifying the batch (scanner variable) as well as a biological covariate to preserve:
covars = {'batch':[5,5,5,1,6,6,6,12,5,5,9,9,9,9,9,8,2,3,5,4,1,1,4,10,5,5,3,5,12,13,13,5,4,11,5,5,2,5,2,2,2,4,8,7,2,8,2,2,4,5,12,12,3,11,3,3,3,2,3,2,2,2,4,2,12,12,5,12,6,5,7,2,2,13,12,12,1,1,6,2,5,2,12,12,5,1,1,2,14,12,12,5,5,5,2,2,4,2,2,2,2,10,4,2,2,2,2,5,12,14,2,2,2,2,2,5,12,12,12,5,5,1,1,1,6,6,5,6,11,2,4,4,4,4,3,4,3,7,2,2,2,2,2,2]}
covars = pd.DataFrame(covars)

# To specify names of the variables that are categorical:
categorical_cols = []

# To specify the name of the variable that encodes for the scanner/batch covariate:
batch_col = 'batch'

#Harmonization step:
data_combat = neuroCombat(dat=data,
    covars=covars,
    batch_col=batch_col,
    categorical_cols=categorical_cols)["data"]

#data_estimate = neuroCombat(dat=data,
    #covars=covars,
#    batch_col=batch_col,
    #categorical_cols=categorical_cols)["estimates"]

#print(type(data_estimate))

#add back header and columns
df = pd.DataFrame(data_combat, index = column, columns = header)
df.to_csv('combat_data.csv', index=True, header=True, sep=',')
#np.savetxt("combat_estimate.csv", data_estimate, delimiter=",")
