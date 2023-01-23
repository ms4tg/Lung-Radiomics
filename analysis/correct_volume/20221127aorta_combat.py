from neuroCombat import neuroCombat
import pandas as pd
import numpy as np



#blacklist = ["0","BEPre","BJPre", "DCPreN1", "HAPreN1", "HWPreN7","LKPreN6", "SBPre","SJPreN2","SWPre", "SWPreN1"]
data = pd.read_csv("original.csv", header = 0)

#print(data)

#header = header.remove("0")
column = data["0"]
data = data.drop(columns = "0", axis =1)
header = list(data)
#print(data)

#header = header.remove(p for p in blacklist)
#print(data.iloc[:,0].head)

# Specifying the batch (scanner variable) as well as a biological covariate to preserve:
covars = {'batch':[14,9,13,13,11,11,11,3,1,5,11,1,10,14,10,10,12,11,12,12,6,7,12,2,3,3,2,5,1,4,6,7,13,14,13,12,4,13,14,8,10,9,6,10,7,6,9,10,9,9,5,3,8,11,8,8,12,14,7,5,14,13,7,14,5,8,11,9,7,9,2,1,3,4,4,5,3,7,4,11,12,12,5,6,9,8,5,8,10,1,4,9,2,6,1,2,6,1,1,4,1,3,13,11,14,3,13,14,5,13,7,13,10,12,11,6,3,3,6,1,4,8,7,8,5,4,4,2,2,4,9,12,14,7,1,2,2,3,6,2,10,8,2,10]}
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
df.to_csv('aorta_combat_data.csv', index=True, header=True, sep=',')
#np.savetxt("combat_estimate.csv", data_estimate, delimiter=",")
