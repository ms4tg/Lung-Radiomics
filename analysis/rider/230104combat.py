from neuroCombat import neuroCombat
import pandas as pd
import numpy as np



#blacklist = ["0","BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]
data = pd.read_csv("original_combine_144.csv", header = 0)

#print(data)

#header = header.remove("0")
column = data["0"]
data = data.drop(columns = "0", axis =1)
header = list(data)

#print(header)
#print(column)
#print(data.iloc[:,0].head)

#keys=[]
#for i in data.index:
#    try:
#        val=float(data.iloc[:,0][i])

#    except:
#        keys.append(i)
#        continue
#print(keys)

# Getting example data
# 200 rows (features) and 10 columns (scans)
#data = data.drop(keys, axis =0)
#column = column.drop(keys)
#print(column)

# Specifying the batch (scanner variable) as well as a biological covariate to preserve:
covars = {'batch':[2,3,1,2,2,1,1,3,2,1,1,3,1,3,2,1,2,1,3,3,1,1,3,2,2,2,2,2,3,1,3,15,15,11,16,13,13,13,4,8,6,13,3,12,16,12,12,14,14,14,15,8,9,14,4,6,5,5,8,4,7,9,9,16,14,7,15,15,15,16,11,12,11,9,13,10,8,12,12,12,11,8,6,10,13,10,10,14,16,9,7,16,15,10,16,7,11,13,11,9,12,5,4,6,7,6,8,6,10,7,14,14,14,8,9,12,10,8,11,12,4,7,11,5,8,4,5,9,4,4,6,3,5,15,13,16,6,15,16,8,15,10,15,12,14,13,9,6,6,9,4,7,11,10,11,8,7,7,5,5,7,11,14,16,10,4,5,5,6,9,4,13,10,5,13]}
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
