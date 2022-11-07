import pandas as pd
import numpy as np
import pydicom

#patients_dir="/media/sf_research/krishni/dataset/CT/"
#patients = ["SW","HD"]
patients_dir="/media/sf_research/krishni/dataset/rider_data/"
patients = list(range(1,25))
patients = [str(p) for p in patients]

ITV={p:pd.read_csv(patients_dir+str(p)+"/GTVp_test_auto.csv", header = None, index_col=0) for p in patients}

data_list = []
for p in patients:
    header=[]
    timesteps = ITV[p].iloc[0] #save the number of timesteps
    for timestep in timesteps:
        header.append (p+timestep) #rename each column patient name + timesteps
    ITV[p].iloc[0,:] = header
    data_list.append(ITV[p])
data_merged = pd.concat(data_list, axis = 1)

#make the first row into header
new_header = data_merged.iloc[0]
data_merged = data_merged[1:]
data_merged.columns = new_header
    #print(ITV)
    #data.index = list(ITV.index)
    #output = pd.merge(data, ITV,how = "left")
print(data_merged)
data_merged.to_csv("rider_data.csv")
